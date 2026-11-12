# OpenLive voice loop: one user turn

Repo: github.com/katipally/openlive @ 65f2420 (Apache-2.0). Study notes only; paths are repo-relative, `file:line`.

Design in one line (docs/ARCHITECTURE.md:8-30): **thick client, thin server**. VAD, STT partials, Smart-Turn, TTS and barge-in all run in the browser renderer (`apps/web/src/lib/live/*`); the agent service (`services/agent`) only receives final text + JPEG frames over the `/live` WebSocket and streams reply text back. Native engines (sherpa-onnx / onnxruntime-node) run in the agent on CPU or a measured accelerator and are reached by the renderer over `/api/voice/*` REST and the `/voice/stream` socket. No audio ever crosses to the model.

## Process flow (one turn)

```mermaid
flowchart TD
  T(["Trigger: mic frame, 512 samples / 32 ms<br/>getUserMedia AEC+NS+AGC on"]) --> VAD{"Silero VAD v6.2<br/>vad-web MicVAD<br/>isSpeech >= 0.5?"}
  VAD -- no, idle --> NF["learn noise floor<br/>onFrame"] --> T
  VAD -- speech start --> OSS["VoiceEngine.onSpeechStart"]
  OSS --> ECHO{"agent playing and<br/>micRms <= gate*(1+2*level)?"}
  ECHO -- yes: echo --> DROP1["echo=true, segment dropped"] --> T
  ECHO -- no --> B{"reply speaking<br/>or thinking?"}
  B -- yes --> PAUSE["pauseReply: AudioPlayer.hold<br/>tentative barge"]
  B -- no --> HEAR
  PAUSE --> HEAR["hear: phase=listening<br/>stream pre-roll ring to /voice/stream if streaming engine"]
  HEAR --> FR["onFrame per 32 ms:<br/>AsrStream.send frame OR buffer curBuf"]
  FR --> PART{"captions? and<br/>>=500 ms since last"}
  PART -- yes, Whisper WebGPU / native batch --> STTP["models.stt partial<br/>onPartial grey caption"]
  PART -- streaming Nemotron --> SP["server partial via ws<br/>onPartial"]
  FR --> GATE{"voiceprint gate on?<br/>1 s and 2 s checks"}
  GATE -- other voice --> IGN["ignore: like echo,<br/>resume paused reply"] --> T
  GATE -- tentative and voiced > 1.5 s --> CUT1["bargeIn"]
  FR --> SE["VAD onSpeechEnd after<br/>redemptionMs 550 silence"]
  SE --> BLIP{"< 0.25 s or<br/>RMS < gate?"}
  BLIP -- yes --> IDLE1["drop, resume reply if paused"] --> T
  BLIP -- no --> PAR[["parallel:<br/>STT final (stream end or batch)<br/>Smart-Turn turnComplete(last 8 s)<br/>voiceprint verify whole segment<br/>side-talk judge POST /voice/addressee"]]
  PAR --> JUNK{"isJunk / backchannel<br/>over paused reply?"}
  JUNK -- yes --> RES["resumeReply"] --> T
  JUNK -- side talk --> ASIDE["onSideTalk: shown dashed,<br/>not sent"] --> T
  JUNK -- no --> DONE{"done? barged OR answersAsk<br/>OR (model complete AND<br/>not endsMidThought)"}
  DONE -- no, < 20 s --> HOLD["pending; scheduleHold holdMs 4000<br/>onHold; optional listening cue"] --> T
  DONE -- yes --> COMMIT["cutPlayingReply; phase=thinking<br/>perf.turnCommitted<br/>onUserText text, wordsAt, speaker"]
  COMMIT --> WS["LiveClient.userText:<br/>ws {t:user_text, text, frames, lang, turn, wordsAt, speaker"}]
  WS --> SRV["LiveSession.runTurn<br/>addMessage; AcpAgent.runTurn session/prompt<br/>OR TurnRunner provider loop"]
  SRV --> SSE["ws {t:sse, event:text_delta, turn"}]
  SSE --> FEED["feedAgentDelta -> SentenceChunker.push<br/>first chunk >= 24 chars at sentence end,<br/>then held sentences, 200-char cap"]
  FEED --> ENQ["enqueueSpeak: stripMarkdown -> normalizeAligned toSpeech<br/>-> speechPieces -> ttsStream"]
  ENQ --> ROUTE{"tts.variant"}
  ROUTE -- kokoro / supertonic browser --> WK["models.worker tts<br/>kokoro-js or Supertonic onnxruntime-web<br/>trimSilence KEEP_S"]
  ROUTE -- native or agent copy --> NT["POST /api/voice/tts<br/>streamed Float32 PCM chunks"]
  ROUTE -- clone --> CL["POST /api/voice/tts profileId<br/>ZipVoice one piece"]
  WK --> PLAY["AudioPlayer.play: scheduled on ctx clock,<br/>30 Hz highpass, MediaStreamDestination -> hidden audio el (AEC-visible)"]
  NT --> PLAY
  CL --> PLAY
  PLAY --> CAP["onStart: onAgentText caption + spokenText;<br/>perf.firstAudio"]
  SSE -- tool_start / acp_tool_call --> STEP["endAgentStep: flush held text"]
  SSE -- done --> END["endAgentTurn: flush tail,<br/>waitDrainThenIdle -> phase idle"]
  CAP -. user talks over .-> OSS
  CUT1 --> BI["bargeIn: cutReply -> hush<br/>epoch++, ttsAbort, player.flush, acceptingReply=false<br/>onBargeIn spoken"]
  BI --> CANCEL["ws {t:cancel, spoken"}]
  CANCEL --> ABORT["LiveSession.interrupt: ac.abort<br/>-> ACP session/cancel + terminals.killAll<br/>truncateSpokenText, Agent.cut note"]
  ABORT --> T
  SRV -- error --> ERR["sse error -> say(message), endAgentTurn"] --> T
  PAR -- STT/turn failure --> FAIL["catch: bargeIn if tentative,<br/>clear caption, idle"] --> T
```

## Numbered narrative

### 0. Setup and models
1. `useLiveSession.start` (apps/web/src/lib/live/useLiveSession.ts:536) calls `loadModels` (models.ts:152) which spawns two Web Workers: `models.worker.ts` (Whisper + Kokoro/Supertonic on WebGPU, WASM fallback, via transformers.js 4.x / kokoro-js 1.2.1 / onnxruntime-web 1.30) and `turn.worker.ts` (Smart-Turn on WASM, own thread so a Kokoro render never delays end-of-turn: turn.worker.ts:2-5). Weights are fetched from Hugging Face only after consent (`agreeTo`, `unagreed`, weights.ts:61) and cached in the browser Cache API (`transformers-cache`, `openlive-models-v1`; models.ts:98-117). A `loadedTag` `tier:stt:tts` (pipelineConfig.ts:441) decides whether the warm worker matches the config.
2. Mic: `openMic` (useLiveSession.ts:542-547) = `getUserMedia({echoCancellation, noiseSuppression, autoGainControl: true})`, optional `deviceId`. Hands-free opens once; push-to-talk opens per hold (voiceEngine.ts:361-363).
3. `VoiceEngine.start` (voiceEngine.ts:364-410) builds `MicVAD.new` from `@ricky0123/vad-web` 0.0.31: `model: "v6"|"v5"`, assets served same-origin from `/vad/` (vendored by apps/web/scripts/copy-voice-assets.mjs:24-29: `silero_vad_v6.onnx`, `silero_vad_v5.onnx`, worklet, ort wasm), `positiveSpeechThreshold` = `vad.speechThreshold` (default 0.5, clamp 0.1-0.9), `negativeSpeechThreshold` = max(0.1, thr-0.15), `minSpeechMs: 250`, `redemptionMs` = 550 default (presets patient 800 / even 550 / quick 350, pipelineConfig.ts:99-103; Flow defaults to patient 0.65/6000/800 via packages/flow-store/src/config.ts:136 and `TurnTuning`). vad-web pre-rolls 800 ms before detected speech: `PRE_SPEECH_FRAMES = floor(800/32)+1 = 26` frames of 512 samples (voiceEngine.ts:84-87). Native engines on the agent are warmed with `"Hi."` / 1600 silent samples every 60 s (`warmNativeEngines`, models.ts:428-460; keep-warm tick 2 min, voiceEngine.ts:92). The agent unloads an idle native engine after 5 min (native-worker.ts:75).

### 1. Mic capture → VAD
4. Every frame hits `onFrame` (voiceEngine.ts:596-634): smoothed `micRms`; while idle the room noise floor is learned (`noiseFloor` EWMA 0.05, cap 0.03) and the reject gate is `max(0.006, floor*1.6)` capped 0.03 (`gate()`, :687). Frames go to the streaming socket (`AsrStream.send`) or into a `FrameRing` of the last 26 frames / `curBuf`.
5. `onSpeechStart` (voiceEngine.ts:531-580): bumps `segment`, restores the floor from 26 frames back (:540), and decides barge-in (section 7).

### 2. Streaming STT and partials
6. Engine choice: `activeSttEngine()` (models.ts:396) = `stt.variant` unless it failed → `"whisper"`. Three paths:
   - **Whisper in the renderer** (`models.worker.ts:106-110`): `pipeline("automatic-speech-recognition", onnx-community/whisper-<size>[.en])`, fp32 on WebGPU / q8 on WASM, large-v3-turbo as fp16 encoder + q4 decoder (:34-35). English uses `.en` builds; other languages the multilingual build with `language` pinned (:31,67). `max_new_tokens = min(440, 16 + 32/s)` (pipelineConfig.ts:433). WASM always runs tiny (pipelineConfig.ts:425).
   - **Native batch** (Parakeet, Moonshine, Canary, non-streamed Nemotron): `nativeStt` (models.ts:470-487) POSTs raw Float32 PCM in 50 s windows to `POST /api/voice/stt?engine=&lang=` (routes.ts:309-324, 60 s cap) → `transcribe` (native.ts:76) → ASR worker thread `transcribe` (native-worker.ts:263-294). Moonshine/Canary audio is split at pauses into ≤8 s windows (`splitAtPauses`, pcm.ts). Returns `{text, at?}` with token onsets from sherpa `timestamps` (Parakeet/Nemotron only).
   - **Streaming Nemotron** (`variant.streaming`): `AsrStream` (asrStream.ts) opens `ws://<agent>/voice/stream?engine=&lang=&token=`; binary Float32 frames up, JSON `{type:"reset"}` / `{type:"end"}` up; `{type:"ready"}`, `{type:"partial", text}`, `{type:"final", text, at}`, `{type:"error", error}` down (native.ts:248-283; worker session ops native-worker.ts:435-464). At speech start the 26-frame pre-roll ring is drained into the socket (voiceEngine.ts:592). Partials come from `decodeSession` (native-worker.ts:423-433) as sherpa decodes each chunk; endpoints (rule1 2.4 s, rule2 1.2 s, rule3 20 s; native-models.ts:374) only commit text and reset the stream. `end` pads chunk+0.42 s of silence (up to 2 s) so held-back words emit (native-worker.ts:102-138); finals measured 120-185 ms (asrStream.ts:9), timeout 3 s then batch fallback.
7. Interim captions (`maybePartial`, voiceEngine.ts:693-716): only when `captions()` (:718) — native engine or WebGPU Whisper; never on WASM Whisper. Re-transcribes the whole utterance so far, spaced `max(500 ms, 2× last partial cost)`; aborted when the segment ends so the final is never queued behind it (:778). Over a paused reply partials decide nothing (:695,:723).

### 3. End of turn (Smart-Turn)
8. VAD `onSpeechEnd(audio)` → `VoiceEngine.onSpeechEnd` (voiceEngine.ts:766-925). Blips (<0.25 s = `MIN_UTTER_SAMPLES`, or RMS under gate) are dropped (:787). Audio is concatenated onto any `pending` held thought (:783). If a previous segment is still finalizing the new one is deferred and merged, never dropped (:782, :914-923).
9. In parallel (`Promise.all`, :833-838): the transcript (`final` from the stream joined onto held text, else `stt(combined)`), `turnComplete(combined, threshold)` (Smart-Turn), the voiceprint verdict `named`, and the side-talk verdict `side`.
   - **Smart-Turn v3** (turn.worker.ts): weights `pipecat-ai/smart-turn-v3/smart-turn-v3.2-cpu.onnx` (weights.ts:13), features = Whisper log-mel from `onnx-community/whisper-tiny.en` `AutoProcessor`, cropped to `[1,80,800]` over the **last 8 s** (zero-padded at the front, :18,:44-55); output is already a sigmoid, `> threshold` ⇒ complete (:60-67). Threshold = `turn.threshold` default 0.5 (presets 0.35/0.5/0.65). Runs on ORT WASM, 1 thread. If the model failed to load, `turnComplete` returns true and the VAD's silence endpointing decides (:57, models.ts:809-817). `turn.engine: "silence"` skips it entirely (voiceEngine.ts:801).
   - Skipped when `ptt` or `barged` (talk over the agent is "act now", :797-801).
10. `done = barged || answersAsk(text) || (modelComplete && !endsMidThought(text, lang))` (:874). `endsMidThought` (voiceText.ts:98-107): English trailing-word list (`to, the, and, because, um, …`); other languages only a trailing comma/ellipsis. Not done and <20 s total → **mid-thought hold**: `pending` kept, `scheduleHold()` arms `holdMs` (default 4000, clamp 1000-8000) and `onHold({until})` shows "waiting… tap to send"; `flushPending` (:935-957) reuses the cached transcript rather than re-running STT. Optional listening cue (`turn.backchannels`, off by default): one of `LISTENING[lang]` ("Mm-hmm.", "Yeah.") rendered once per voice at gain 0.4 on a separate `cuePlayer`, after 3 s of speech, ≤1 per 8 s, never after a question (`cue`, :748-758).
11. `isJunk` drops empties and Whisper silence hallucinations ("thank you", "thanks for watching", …; voiceText.ts:82-90).

### 4. The model turn (renderer → agent)
12. Commit (voiceEngine.ts:889-902): `cutPlayingReply()`, phase `thinking`, `replyOpen=true`, `acceptingReply=true`, `perf.turnCommitted(sttEndpointMs)`, then `h.onUserText(text, heard.at, speaker, judged)`. `heard.at` = per-word onsets (engine token times, else `heardOnsets` placed on the mic audio; models.ts:581).
13. `handleUserText` (useLiveSession.ts:734-755): if a permission/elicitation modal is open the utterance is the modal's answer and never a prompt (`answerModalByVoice`, `classifyYesNo` in modalAnswer.ts). Otherwise grabs the freshest camera/screen JPEG from the ~1 fps buffer (cameraCapture.ts) and calls `LiveClient.userText`.
14. **Wire (client→server)** `packages/shared/src/live-events.ts:194-256`, JSON over `ws://localhost:<agentPort>/live?chat=&token=&lang=&flow=1&device=1` (liveClient.ts:110):
    - `{t:"user_text", text, frames?:[{data(b64), mime, source:"camera"|"screen"|"attachment"}], lang?, turn, wordsAt?, speaker?, aside?, typed?}`
    - `{t:"cancel", spoken?}` — barge-in
    - `{t:"control", action:"camera_on"|"camera_off"|"screen_on"|"screen_off"|"end"}`
    - `{t:"frame_response", reqId, failed?}` then a binary frame tagged `0x02` (the `look` tool)
    - `{t:"tool_bridge_result", reqId, output}`, `{t:"bind", agentId|null, cwd, resumeSessionId?}`, `{t:"permission_response", reqId, optionId}`, `{t:"elicitation_response", reqId, action, content?}`, `{t:"set_model"|"set_mode"|"set_option", …}`
    - Flow: `{t:"flow_text", text, context?, lang?, turn, wordsAt?, speaker?, quiet?, aside?}`, `{t:"flow_cancel", spoken?, close?}`, `{t:"flow_resume", sessionId}`, `{t:"flow_new"}`
    - User turns are queued (max 8) across a reconnect and flushed after `bind` (liveClient.ts:172-180).
15. **Server** `LiveSession.onText` (services/agent/src/live/session.ts:237-286) → `runTurn` (:302-431): an utterance during an active turn is queued and merged (:307-325); the user message is persisted with `wordsAt`/`speaker` (:344); the text is sent either to the bound coding agent (`AcpAgent.runTurn` → ACP `session/prompt`, language line prepended by `withReplyLanguage`, acp-agent.ts:823) or to the built-in provider loop (`TurnRunner.runTurn`, turn-runner.ts). Emits are wrapped by `wrapEmitWithNarration` + `createCommentaryGate` (narrator.ts) so only the opening line and final answer are spoken; mid-tool commentary goes to the reasoning channel; long tool runs get one `say` status line after 1.5 s, ≤4 per turn, ≥8 s apart.
16. **Wire (server→client)** live-events.ts:97-182: `{t:"sse", event, turn}` wrapping the SSE union (sse-events.ts:11-44: `text_delta{text}`, `reasoning_delta`, `tool_start{id,tool,summary}`, `tool_done`, `acp_tool_call{call}`, `acp_tool_update{delta}`, `term_output`, `term_exit`, `todos`, `usage`, `status{text}`, `say{text}`, `done`, `error{message,code}`); plus `need_frame{reqId}`, `tool_bridge{reqId, op, arg, turn}`, `permission{reqId, question, options[{id,label,kind}], expiresAt, toolCallId, turn}`, `permission_resolved`, `agent_meta{models, modes, options, commands, …}`, `elicitation`, `elicitation_resolved`, `reload_history`, `bound_state{agentId, cwd, agentActive}`, `flow{event, turn}`, `error`, `reminder{title, body}`. The `turn` number echoes the client's counter so a cancelled turn's stragglers are dropped (`LiveClient.current`, liveClient.ts:170).

### 5. Streaming TTS
17. `onSse` (useLiveSession.ts:387-454): `text_delta` → `engine.feedAgentDelta`; `say` → `engine.say` (voiced, never persisted); `tool_start`/`acp_tool_call` → `engine.endAgentStep` (flush held text before dead air); `done` → `engine.endAgentTurn`; `error` → `endAgentTurn` + `say(message)`; permission → `engine.ask(question)` (all of it voiced now, :318).
18. `feedAgentDelta` (voiceEngine.ts:1136-1145): fixes `replyVoice` at the first delta (engine/voice/speed/lang/compiled lexicon) and pushes text through `SentenceChunker.push` (voiceText.ts:288-375). Chunking rules: the **first chunk goes at ≥24 chars** (`FIRST_TTS_CHARS`) but only at a sentence end (`SENTENCE_END` regex incl. 。！？।); afterwards whole sentences are **held** and released by `take()` only when the audio queued ahead is about to run out — `feed()`/`slack()` (:1148-1165): `ahead − 2×synthPace×chars − 1 s`, paces learned per voice as an EWMA (0.3) after the first warm render (:1280-1283); `MIN_TTS_CHARS` 40, `MAX_CHUNK_CHARS` 200 (120 for zh/ja/ko), abbreviations/decimals/code spans never split, fenced code blocks are never spoken. A short trailing sentence joins the chunk ahead of it while that one has not started synthesizing (`joinChunks`, :1209-1214). Bars scale by language speaking rate (`LANG_TEXT`, voiceText.ts:47-53).
19. `enqueueSpeak` (:1203-1309) per chunk, serialized on `ttsChain`: `stripMarkdown` → `normalizeAligned` (packages/shared/src/speech/normalize.ts: numbers, dates, money, units, URLs, versions spelled out via n2words + Intl, user lexicon) → `speechPieces` (≤400 chars English) → `ttsStream(piece, {engine, voice, speed, lang}, onChunk, abort)`.
20. `ttsStream` (models.ts:694-757) routes:
    - **Native engine or agent copy of Supertonic**: `POST /api/voice/tts {engine, text, voice?, speed, lang}` (same-origin Next proxy apps/web/src/app/api/voice/[...path]/route.ts → agent `nativeTts`, routes.ts:380-416) which streams raw little-endian Float32 PCM with header `x-sample-rate`; the worker posts `start` when synthesis begins then `chunk` per sentence (`maxNumSentences: 1`, native-models.ts:388-393; native-worker.ts:320-353). Renderer decodes with `pcmDecoder` (pcm.ts) and hands each chunk straight to the player — **speech starts before the sentence is finished**. Guards: start within 10 s (`TTS_START_MS`), stall = 4 s + 50 ms/char (`ttsStallMs`), 2 attempts, 2 hung sentences ⇒ fallback to browser voice for the call.
    - **Clone**: `POST /api/voice/tts {text, profileId, speed}` → ZipVoice (engine.ts), one piece back.
    - **Browser**: worker message `{type:"tts", text, engine, voice, speed, lang}` → kokoro-js `generate` or `Supertonic.synthesize` (8 flow steps, seeded noise 0.8, short-chunk stretch ≤15%; packages/shared/src/speech/supertonic.ts:22-40), then `trimSilence(KEEP_S)` (keep 0.05 s lead, 0.35/0.45 s tail; trim.ts:14).
21. **Playback** `AudioPlayer.play` (audioPlayback.ts:81-105): each Float32 buffer scheduled back-to-back on the AudioContext clock (`nextAt`), explicit `stop()` at its end (Chromium buzz fix), through one 30 Hz highpass (DC offset in Kokoro/Kitten), into a `MediaStreamDestination` → hidden `<audio>` element so Chrome's AEC3 references it (:5-9). `onStart` fires when the chunk actually begins playing → `onAgentText(spoken, onsets)` reveals the caption word by word (timing from `placeWords`/`paceWords` in packages/shared/src/speech/timing.ts) and appends to `spokenText`; `perf.firstAudio()` closes the latency record (perf.ts: stt+endpoint, model-to-first-token, tts-to-first-audio; medians/p95 shown in the call bar).
22. First-audio tricks, summarized: low 24-char first bar; agent engines stream per sentence while rendering; synthesis runs ahead and held text is fed by the slack calculation so chunks are long (one-voice prosody) but never late; warm-ups keep agent engines loaded; Smart-Turn on its own worker; the `/live` connect carries `?lang=` to warm the prompt cache (session.ts:202); a pre-call `LiveClient` is reused so Start is instant (useLiveSession.ts:636-642).

### 6. End of reply
23. `endAgentTurn` (:1181-1191) flushes the chunker tail, clears `replyVoice`, `replyOpen=false`; once `ttsChain` drains and `player.playing()` is false, `waitDrainThenIdle` sets phase `idle` (or `thinking` if an ask is open). Reminders arriving mid-reply are held and said in a gap (`announce`, :1326-1340).

### 7. Barge-in
24. Decision at `onSpeechStart` (voiceEngine.ts:546-577): `speaking = phase==="speaking" || player.playing()`; `echoSafe = !speaking || micRms > gate()*(1+2*player.level())` (speaker leak gate; headphones barge instantly); `ONSET_GRACE_MS` 250 after speech start; `holding = holdBargeIn()` (a permission/elicitation is pending → the speech is the answer, never a cancel; the question audio is only `hush`ed locally, :565-571).
25. First response is a **pause, not a cut**: `pauseReply()` → `AudioPlayer.hold()` suspends the context (caption freezes, :1360-1366). The words decide: a final that is junk or a backchannel (`isBackchannel`, per-language lists + laugh/throat-sound regex, voiceText.ts:114-157) → `resumeReply()` from the same sample (:1371-1382). Any other final, or >1.5 s of voiced talk before words are in (`BACKCHANNEL_MAX_MS`, :627-628; waits for the voiceprint's 2 s check when gated, never past 3 s; with side-talk "ignore" on it waits for the words) → `bargeIn()`.
26. `bargeIn` → `cutReply` (:1410-1416): `spokenSoFar()` = whole sentences voiced + the words of the playing sentence revealed by now (`heardText`); `acceptingReply=false` so late deltas are ignored until the next turn; `hush()` (:1346-1358) increments `epoch` (stale TTS/audio dropped), aborts the in-flight `ttsStream`, `player.flush(epoch)` stops every scheduled source, clears the chunker and feed timer. `h.onBargeIn(spoken)` → `LiveClient.cancel(spoken)` (useLiveSession.ts:600-620) and the transcript is snapped to `spoken`.
27. Server `cancel` (session.ts:249-255): if a turn is active `bargeSpoken = spoken` and `interrupt()` aborts the turn's `AbortController` → ACP `session/cancel` notification + `terminals.killAll()` (acp-agent.ts:812-817); the provider loop's fetch is aborted. In `finally` (:403-407) the assistant blocks are truncated to `spoken` (`truncateSpokenText`), the built-in brain's history is cut, and `Agent.cut(spoken, cancelled)` leaves a note for the coding agent's next prompt ("[The user cut you off. Of your last reply they heard only: …]", acp-agent.ts:192-197), also saved as setting `agentCut:<chat>` for reconnects. A cancel after the reply was saved cuts the saved message (`cutSavedReply`, :447-455). Hanging up sends the same cut.
28. The barged utterance itself is sent as the next `user_text` with no mid-thought hold (`barged` ⇒ `done`, :874) and queued server-side if the old turn has not fully settled (:307).

### Push-to-talk vs hands-free
- Hands-free (default): VAD listens continuously; Smart-Turn + hold decide the end; mute = `setMuted`.
- Push-to-talk (`talk.mode === "ptt"`, Fn / Right Ctrl, or the Hold-to-talk button): `setGate(true)` closes the VAD between holds so nothing is heard and nothing barges (voiceEngine.ts:1122-1133). `beginPtt` (:992-999) cuts any reply, opens the mic, and starts a **tape** (`tapeOf`, ScriptProcessor at 16 kHz, :146-174) from the first frame because the VAD worklet loads late; `watchLive`/`holdVerdict` decide if the device stayed silent (300 ms wired, 2.5 s Bluetooth, holdLive.ts). No end-of-turn decision while held: segments accumulate into `pending` (:862-867). `endPtt(now)` (:1023-1079) sets `redemptionMs 0` so the segment closes on the next quiet frame, finds speech on the tape with a separate Silero session (`speechFrom`, 3 frames ≥ threshold, 300 ms pre-roll; tapeSpeech.ts), transcribes once, and sends. PTT is never judged for side talk and never turned away by the voiceprint, only labelled (:862-864, :476).

### The three evals / gates ("is this for me?")
| Check | Decides | Where it runs | Model | How the engine uses it |
|---|---|---|---|---|
| **voiceprint** (`voiceprint: off/label/gate`, default off) | Is this segment the enrolled user? Labels turns "you" / "other N"; in `gate` mode only the user may start turns or barge in | agent, `POST /voice/voiceprint/verify?mic=&voiced=` (routes.ts:332-347 → voiceprint.ts:90-101), speaker worker thread | 3D-Speaker CAM++ zh-en advanced, 192-dim, 28 MB, Apache-2.0 (native-models.ts:288-293) | Checks at 1 s and 2 s voiced (`GATE_MS`, voiceEngine.ts:104, `checkEarly` :641-658) then the whole segment at its end (`recheck` :674-683). Thresholds by voiced length `[0,-0.085],[1,0.087],[2,0.286],[4,0.4]` (voiceprint.ts:26); segments ≥0.6 cosine with ≥2 s speech adapt the print; explicit ~15 s enrollment, gate on at 10 s; prints per mic, max 6. Other voices clustered at cosine 0.35 (`OtherVoices`). Failure/timeout (1.5 s) ⇒ speech passes. |
| **addressee / side talk** (`sideTalk: off/shadow/ignore`, default off) | Was this finished sentence said to the app, or to someone else / no one? | agent, `POST /voice/addressee {text, reply, speaker, feats, id?, mode?}` (routes.ts:361-374 → addressee.ts:113-123), addressee worker on onnxruntime-node | Xenova paraphrase-multilingual-mpnet-base-v2 int8 (296 MB, Apache-2.0) + logistic head `HEAD` (threshold 1.51359; packages/shared/src/speech/addressee-head.ts) or a user-trained `addressee-head.json` | Judged in parallel with Smart-Turn (voiceEngine.ts:823-832), 800 ms timeout ⇒ addressed. Rules first and only toward "addressed": a sentence after a reply that ended on `?` is its answer, naming "OpenLive" is for it, an open ask takes every sentence, PTT never judged; other voice shifts +1 log-odds. Verdict `side` → `onSideTalk` (dropped, shown dashed with "Send it" → `sendAside`), over a paused reply it resumes the reply. Audio features `Feats` (relative loudness, pitch, rate, gap since agent voice, …; `speechStats`) ride along; `shadow` logs without dropping. Eval: ~23% English side talk caught at ≤1% addressed ignored (ARCHITECTURE.md:457-462). |
| **converse** (`tools/converse`, `pnpm converse:eval`) | Not a runtime check: a scripted-conversation eval of turn-taking and the optional listening cues (`turn.backchannels`) | dev tool, macOS `say` → real `VoiceEngine` + Silero + Smart-Turn on onnxruntime-node + agent Nemotron over `/voice/stream` + `/live` | — | Measures end-of-speech → first reply audio latency, cue timing (8 cues in 30 turns, p50 820 ms after the pause, 0 overlapping the user) and overlap (`measure.ts`). |

### Failure exits (where a turn ends without a reply)
- Blip / silence / junk / backchannel-only: dropped, phase idle, paused reply resumed (voiceEngine.ts:784-787, 854-858, 870).
- Other voice (gate on): ignored (`ignore`, :662-670; :843-849).
- Side talk: `onSideTalk`, not sent (:853, :891).
- STT or Smart-Turn threw / timed out (12 s `CALL_TIMEOUT_MS`, 60 s cold native fallback, models.ts:266,:466): `catch` clears the caption, idles; if a reply was paused it is cut because the words are unknown (:903-908).
- Native STT lasting failure (400/404/409/502, nativeFailure.ts): `nativeSttFailed` swaps to Whisper for the rest of the call, asking to download it if missing (models.ts:407-421). Streaming socket refused (1008) does the same (asrStream.ts:48-56).
- Native TTS lasting failure or two hung sentences: `ttsFallback` → browser Kokoro (en) / Supertonic (other langs) for the call; a one-off failure retries once then leaves that sentence unspoken rather than changing voice mid-reply (models.ts:730-748). Clone failure → browser voice (:618-642). No browser voice for the language (zh): sentence goes to the caption only (:655-666, voiceEngine.ts:1298-1302).
- Agent error SSE: spoken via `say`, reply ended (useLiveSession.ts:390-397). Socket drop: turns queued and flushed on reconnect (liveClient.ts:114-119).

# File → feature index: voice loop and speech engines

OpenLive @ 65f2420. Every file read for `foxmap/voice-loop.md` and `foxmap/engines.md`. Format: `path | feature | one-line role`.

## Docs
- `README.md` | overview | Product framing: cascaded on-device pipeline, engine list, ten languages, PTT vs hands-free, data folder layout, download sizes.
- `docs/ARCHITECTURE.md` (§ "The voice loop", "Voice cloning", lines 138-597) | voice loop | Authoritative narrative of one turn, chunker rules, barge-in, model licenses, Supertonic-on-agent, native engine benchmarking, voiceprint and side-talk evals with measured numbers.
- `CONTRIBUTING.md` (lines 195-260) | regress / bake-off | How to run `voice:regress`, `voice:bakeoff`, tiers, caches.
- `THIRD_PARTY_NOTICES` | licenses | Adapted source code only (Orca, Cua Driver, Orb wave orb); no model licenses here.

## Renderer: `apps/web/src/lib/live/`
- `voiceEngine.ts` | voice loop core | `VoiceEngine`: Silero MicVAD wiring, echo gate, pause-then-cut barge-in, partials, Smart-Turn + mid-thought hold, PTT tape, voiceprint gate, side-talk hook, SentenceChunker feed/slack, TTS chain, captions, listening cues, announcements.
- `models.ts` | engine facade | Main-thread facade over the two workers; routes STT/TTS to browser worker, agent native engines, agent copy of Supertonic, or ZipVoice; consent-gated downloads; fallback state (`sttFallback`, `ttsFallback`); warm-ups; `/api/voice` client (engines, perf, download).
- `models.worker.ts` | renderer STT/TTS | Whisper (transformers.js) + kokoro-js + Supertonic on WebGPU/WASM; serialized GPU jobs; trimSilence per render.
- `turn.worker.ts` | end-of-turn | Smart-Turn v3.2 ONNX on WASM: Whisper-tiny log-mel over last 8 s, sigmoid threshold.
- `supertonic.ts` | renderer TTS | Loads Supertonic files through Cache API onto onnxruntime-web (webgpu→wasm).
- `weights.ts` | model manifest (browser) | Hub repos/paths for Whisper, Kokoro, Supertonic, Smart-Turn; cache checks; size lookup via HF tree API; consent (`unagreed`, `ModelsNotDownloaded`).
- `pipelineConfig.ts` | config + catalog | `PipelineConfig` defaults/clamps, turn presets, Whisper sizes, VAD models, voice lists, STT/TTS family catalog mirroring the agent, restricted-license logic, `LANGUAGE_DEFAULTS`, `pickCompatible`, `whisperCheckpoint`, `workerTag`.
- `asrStream.ts` | streaming STT client | `AsrStream` over `/voice/stream`: frames up, partial/final down, 3 s final timeout, refusal handling.
- `audioPlayback.ts` | playback / barge-in | `AudioPlayer`: gap-free scheduling, epoch flush, hold/release, 30 Hz highpass, MediaStreamDestination→`<audio>` for AEC, level/spectrum taps.
- `voiceText.ts` | text → speech prep | `SentenceChunker` (24/40/200-char bars, held sentences, fences), `stripMarkdown`, `isJunk`, `isBackchannel`, `endsMidThought`, `LISTENING` cues, `speechPieces`, language rates.
- `pcm.ts` | PCM plumbing | `pcmDecoder` for streamed Float32 bytes; `FrameRing` pre-roll buffer.
- `nativeFailure.ts` | fallback policy | Which HTTP statuses mean a native engine failure will repeat (400/404/409/502).
- `voiceprint.ts` | voiceprint client | `verifyVoice`/`enrollVoice`/status calls with a 1.5 s verdict timeout; null = let speech through.
- `addressee.ts` | side-talk client | `sideTalk` POST with 800 ms timeout (fail-open), `labelJudgment`, status/log deletion.
- `perf.ts` | latency budget | Per-turn stt+endpoint / model / tts / voice-to-voice, medians and p95, `openlivePerf.summary()`.
- `tapeSpeech.ts` | PTT tape VAD | Separate Silero session to find speech start on a hold's tape (3 frames, 300 ms pre-roll).
- `holdLive.ts` | PTT mic wake | Per-device wait (300 ms wired, 2.5 s Bluetooth) before a hold counts as silent.
- `holdCue.ts` | PTT cues | Sine blip tones at hold start/stop.
- `ttsCapture.ts` | debug capture | Records each played piece + manifest to the agent for `voice:capture` analysis.
- `warmup.ts` | startup warm-up | Background model load + mic spin after launch (quiet, no permission prompt).
- `engineMenu.ts` | settings copy | Language labels, `licenseTag` classification, engine switch notices, missing-engine lists.
- `useLiveSession.ts` | call orchestration | React hook wiring `VoiceEngine` ↔ `LiveClient`: mic constraints, SSE → feed/say/endAgentStep/endAgentTurn, barge-in → cancel, permission/elicitation voice answers, frames per turn, PTT key handling.
- `liveClient.ts` | `/live` client | WebSocket to the agent: `user_text`, `cancel`, `control`, `bind`, permission/elicitation responses, Flow messages, frame upload, reconnect queue, turn numbering.
- `modalAnswer.ts` | voice answers | Classifies a spoken yes/no for a permission ask.
- `cameraCapture.ts` | vision frames | ~1 fps JPEG buffer; freshest frame attached to each turn; hi-res `look`.
- `spectrum.ts` | orb visuals | Octave-band fold of analyser data for mic/agent waveforms.
- `timeline.ts`, `toolMeta.ts`, `composer.ts`, `callFact.ts`, `linkStatus.ts`, `micCopy.ts`, `liveStore.ts`, `panelBridge.ts`, `devices.ts`, `keyTargets.ts`, `usePtt.ts`, `useApiModeChoice.ts`, `chatReadiness.ts`, `lobbyGap.ts`, `howItRuns.ts`, `speechFacts.ts` | UI glue | Transcript layout, tool labels, typed composer, telemetry facts, link banner, mic copy, call store, orb bridge, device lists, PTT key hook, readiness checks (not on the audio path).
- `apps/web/scripts/copy-voice-assets.mjs` | VAD assets | Vendors `silero_vad_v6.onnx`, `silero_vad_v5.onnx`, vad worklet and ORT wasm into `public/vad/`.
- `apps/web/src/app/api/voice/[...path]/route.ts` | proxy | Same-origin proxy to the agent's `/voice/*`, injects the shared secret, streams bodies.
- `apps/web/src/lib/flow/useFlowOwner.ts` (line 336-363) | Flow voice | Second `VoiceEngine` for Flow with `TurnTuning` from flow-store and `backchannels: false`.
- `packages/flow-store/src/config.ts` (line 136) | Flow turn defaults | threshold 0.65, holdMs 6000, redemptionMs 800 (overridable).

## Shared: `packages/shared/src/`
- `live-events.ts` | wire protocol | Zod schemas of every `/live` client→server and server→client message, language codes, `withReplyLanguage`, binary tag 0x02.
- `sse-events.ts` | reply stream | SSE event union wrapped in `{t:"sse"}`: text_delta, tool events, say, done, error.
- `speech/supertonic.ts` | TTS engine | Shared Supertonic synthesis (4 ONNX graphs, 8 flow steps, seeded noise, short-chunk stretch) for onnxruntime-web and -node.
- `speech/trim.ts` | TTS post-processing | `trimSilence` at -50 dBFS with `KEEP_S` lead/tail per engine.
- `speech/normalize.ts` | TTS text | `toSpeech`/`normalizeAligned`: numbers, dates, money, units, URLs spelled out per language (n2words + Intl).
- `speech/timing.ts` | captions | Word onset placement on synthesized or mic audio (`placeWords`, `paceWords`, `heardOnsets`, `tokenOnsets`, `heardText`).
- `speech/lexicon.ts` | pronunciations | User dictionary compiled to regexes.
- `speech/voiceprint.ts` | speaker math | cosine, `fold`, `bestScore`, `OtherVoices` clustering at 0.35.
- `speech/addressee.ts` | side talk | Context rules (`askedBack`, named, open ask), `Feats` audio features (`speechStats`), logistic scoring.
- `speech/addressee-head.ts` | side talk | Shipped logistic head weights + threshold 1.51359 (written by `addressee:eval --write`).

## Agent: `services/agent/src/`
- `voice/native-models.ts` | **engine manifest** | Every native variant: id, family, kind, type, URL, bytes, quality, languages, license, files, voices; Piper table; `sherpaConfig`; `downloadEngine`; `speakable`.
- `voice/native-worker.ts` | engine runtime | Worker thread owning sherpa/ORT handles: batch STT, streaming sessions, per-sentence TTS streaming (NaN guard, peak limit, runaway budget, edge fitting), embeddings, benchmark mode, LRU of 2 models, 5 min idle unload.
- `voice/native.ts` | engine host | One worker per kind, request/response plumbing, accelerator retirement on failure, child-process benchmarks, idle-triggered bench queue, `/voice/stream` WebSocket upgrade.
- `voice/routes.ts` | REST surface | `/voice/engines`, `/engines/:id/download`, `/stt`, `/tts` (native streaming + clone), `/perf*`, `/voiceprint*`, `/addressee*`, ZipVoice model + profiles, debug capture sink.
- `voice/engine.ts` | voice cloning | ZipVoice via sherpa `OfflineTts`, per-call reference audio, serialized queue, idle unload.
- `voice/accel.ts` | accelerator choice | Benchmark store (`voice-accel.json`), `chooseProvider` (20% RTF gain), overrides, failure marking, sibling skip, fixed bench inputs.
- `voice/device.ts` | device probe | OS/CPU/GPU/RAM/power probe, ONNX Runtime provider detection for sherpa and onnxruntime-node, `threadsFor`, `tier`, fingerprint.
- `voice/voiceprint.ts` | voiceprint | Enrollment, verify with length-based thresholds, adaptive prints per mic, storage in settings.
- `voice/addressee.ts` | side talk | Judge with shipped or personal head, judgment log (JSONL, 5000 cap), labels.
- `voice/pcm.ts` | PCM helpers | `pcmFromBytes`, `pcmBytes`, `splitAtPauses`, `fitSilence`, `limitPeak`, `SAMPLE_RATE` 16000.
- `voice/bench.ts` | dev tool | `pnpm --filter @openlive/agent bench:voice`: prints the P0 benchmark for every installed engine.
- `live/ws.ts` | sockets | Attaches `/live` and `/voice/stream` upgrades to the HTTP server; secret/origin gate.
- `live/session.ts` | turn server | `LiveSession`: parses client messages, `runTurn` (persist, ACP or provider turn, narration gate), `cancel` → abort + spoken-text truncation + `Agent.cut`.
- `live/narrator.ts` | spoken progress | `wrapEmitWithNarration` (one `say` status line per long tool) and `createCommentaryGate`.
- `live/turn-runner.ts` | built-in brain | Provider turn loop (not read in depth; referenced for the non-ACP path).
- `agents/acp-agent.ts` (lines 185-215, 810-840) | ACP driver | `cut()` note for the next prompt; abort → `session/cancel` + terminal kill.
- `server.ts` (line 38-39) | mount | `app.route("/voice", voiceRoutes)`.

## Tools
- `tools/voice-regress/src/run.ts` | regression | Streams corpus through the chunker and engines, compares joins against one-go renders, gates and baselines.
- `tools/voice-regress/src/engines.ts` | regression engines | Per-engine adapters (native worker, kokoro-js, Supertonic), pinned SHA-256 sums, tiers/slack/limits.
- `tools/voice-regress/src/summary.ts` | metrics | `METRICS` thresholds, delta simulation, summarize.
- `tools/voice-regress/src/analyze.ts` | metrics | Join analysis (pitch, pause, loudness, lead/tail, broken samples).
- `tools/voice-regress/src/bakeoff.ts` | bake-off | P0 benchmark per provider, renders, WER/UTMOS/CED scoring, table output.
- `tools/voice-regress/src/chatterbox.ts` | bake-off candidate | Chatterbox-Turbo ONNX pipeline on onnxruntime-node.
- `tools/voice-regress/src/capture.ts` | playback analysis | Reads `ttsCapture` manifests, reports clicks/gaps/DC steps, writes reconstruction.wav.
- `tools/voice-regress/{corpus.json,bakeoff.json,baseline/*.json}` | fixtures | 14 replies; normalized/expressive lines; per-engine baselines.
- `tools/voiceprint/src/run.ts` | eval | Speaker-model eval on LibriSpeech + agent voices under noise/room conditions; picked CAM++.
- `tools/addressee/src/{run,train,simulate,head,data}.ts` | eval | Side-talk model eval, personal head training, simulated log; writes `addressee-head.ts`.
- `tools/converse/src/run.eval.ts` | eval | Scripted conversations through the real `VoiceEngine` + Silero + Smart-Turn + Nemotron stream + `/live`, measuring latency and listening-cue overlap.

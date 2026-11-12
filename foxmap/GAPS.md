# OpenLive vs Fox — gap check (WINGSCRUM-557, 12 Nov 2026)

OpenLive @ 65f2420 (read, not run — the Mini is paging, swap 83%). Fox today = `voice-v1-base` (`~/fox` tag, commit 9383643) + the live gateway plugin, CuaDriver for 555, kura-r2 for Kura. "Beats" claims about engines are from OpenLive's own measured numbers in code; nothing was benchmarked here.

Legend for the last column: **Adopt** = take their approach or component; **Borrow** = take the idea, write ours; **Skip** = not for Fox.

## 1. Koe voice (voice-v1-base, gaps 1 / 5 / 7)

| Feature | OpenLive | Fox today | Gap | Adopt / borrow / skip |
|---|---|---|---|---|
| Where the loop runs | Renderer (Electron/Next): VAD, STT partials, Smart-Turn, TTS, barge-in all client-side; server gets text | Gateway plugin on the Mini; the iPhone Talk Mode client is OpenClaw's; Whisper :3211 + Kokoro :3216 loopback | Architecture opposite: theirs is thick-client, ours is server-side so the phone stays thin | **Skip** the thick client — Fox's client is the phone. Keep server-side loop. |
| VAD | Silero v6.2 via vad-web, 32 ms frames, thr 0.5, redemption 550 ms (presets 350/550/800), 800 ms pre-roll, learned noise floor | Silero (VAD_CTX=64 prepend), tuned thresholds (24 of them, drift-tested) | Equal. Their noise-floor EWMA + reject gate (`gate()` = max(0.006, floor×1.6)) is cleaner than our fixed `bargeMinRms 900` | **Borrow** the learned noise floor for gap 5 |
| STT | Whisper WebGPU, or native sherpa engines: **Nemotron streaming** (partials while talking, finals 120–185 ms after end), Parakeet, Moonshine, Canary; partials re-transcribe every ≥500 ms | whisper.cpp batch (:3211), partial captions by re-transcribing (gap 6 done) | Streaming STT with real partials is the one engine-level thing we lack | **Adopt** Nemotron-en streaming int8 (464 MB, NVIDIA Open Model License) behind the same :3211 shape — needs a sherpa-onnx service, not a whisper.cpp flag |
| End of turn | Smart-Turn v3.2 on its own WASM worker, parallel with final STT + voiceprint + side-talk; "not done" or trailing filler → 4 s mid-thought hold, 20 s max | Smart Turn v3.2, `completeProb 0.95`, `maxSilenceMs 2500` | Same model. Their **hold** (keep listening, don't cut) is the shape of our gap 7 (merge quick follow-ups) | **Borrow** the pending/hold merge (`onSpeechEnd` concatenates onto `pending`) for gap 7 |
| Barge-in | Speech over a reply **pauses** playback first (`AudioPlayer.hold`); words decide: backchannel/cough → resume from the same sample; real words or >1.5 s voiced → cut, `cancel{spoken}`, server truncates the saved reply to what was voiced and leaves "[user cut you off]" for the next prompt | Cut on `bargeMinWords 6` + RMS; echo gate (voiceloop idea); AC19 cut maps audio fraction → text | Their pause-classify-resume IS gap 5, already built and tuned | **Adopt** the pause-then-decide state machine (ours in JS, their names: `pauseReply`/`resumeReply`/`cutReply`) |
| Echo of her own voice | Player routes through `MediaStreamDestination` → hidden `<audio>` so Chrome AEC3 cancels it; plus `micRms ≤ gate×(1+2×level)` echo check | `echoVerdict` gate, `rememberSpoken` per clip; 0.975 abandoned | Theirs leans on browser AEC — not available server-side on the phone path | **Skip** (platform-specific); keep ours |
| Voiceprint / side-talk | CAM++ speaker embedding (28 MB, EER 0.8 % whole utterance); addressee classifier (MPNet int8 296 MB, AUC 0.895) decides "talking to me?"; aside shown dashed, not sent | None | Two whole subsystems we don't have; side-talk matters on an iPhone speaker in a family room | **Borrow** later (PI4): voiceprint first, addressee second; both run on CPU on the Mini |
| TTS streaming | Sentence chunker: first chunk ≥24 chars at a sentence end, later sentences released by a slack rule (queued audio vs 2× synth pace + 1 s), 200-char cap; native engines stream Float32 PCM per sentence | `stream/sentences.js` (P3): first audio 217 ms live; Kokoro does not stream (measured) | Equal in effect. Their **slack release** keeps prosody across sentences; ours releases every sentence | **Borrow** the slack rule (≈40 lines) |
| Text → speech normalising | `toSpeech`: numbers, URLs, code, emoji spelled/stripped before any engine; `speakable()` strips emoji for espeak | Transcript cleaner (byte-frozen) | Partial overlap | **Borrow** their table for URLs/numbers |
| Captions | Word onsets placed on synthesized audio; captions reveal word-by-word | Caption per clip (gap 2) + user partials (gap 6) | Theirs are finer (word-level on Fox's speech) | Borrow later, cosmetic |
| First-turn lag (gap 1) | n/a — they have no 31k system prompt; provider loop or ACP adapter is warm; native engines warmed every 60 s with "Hi." | 3.9 s fixed overhead per session key; needs 514 warm CLI | Not solved by OpenLive; their engine keep-warm tick is worth copying | **Borrow** keep-warm pings for Whisper/Kokoro; gap 1 stays 514 |
| Thinking feedback | Spoken "narrated progress" (plan steps read aloud) + orb states | Chime + dots (gap 4 done) | Different choice, ours is lighter | Skip |
| PTT vs hands-free | Both; Fn hold on Mac; PTT tape via a second VAD session | Phone Talk Mode (hands-free) | Equal | Skip |
| Regression harness | `tools/voice-regress`: bake-off + regress with measured joins (`roughJoins`, `f0JumpSt`, `pauseMs`), PR-CI gates per engine | `koe-drift.test.js` (thresholds + byte-identity), `test.mjs` 7/8 | We test that nothing moved; they test that it still sounds right | **Adopt** the idea of acoustic regress metrics (joins/pitch jumps) for the sentence pipeline |

## 2. Speech engines — who beats Kokoro and Pocket on the Mini

Fox today: Kokoro af_heart on :3216 (24 kHz, Apache-2.0, ~8.6× realtime, no streaming); Pocket TTS was the earlier read-back plan. Whisper.cpp for STT.

| Engine | Kind | Size | Their measured speed | Quality / license | Beats what we run? |
|---|---|---|---|---|---|
| Nemotron streaming en int8 | STT | 464 MB | finals 120–185 ms after end; partials live | 0.6B, English, token onsets; NVIDIA Open Model License | **Beats whisper.cpp** on latency (streaming) — the only engine that changes the feel |
| Nemotron 3.5 multilingual int8 | STT | 475 MB | same; 84 % word-exact in their sim | 28 languages incl. Hindi; OpenMDW-1.1 | Beats whisper for Hindi/Marathi-adjacent later; 3.3 GB RAM with Parakeet loaded — **too heavy for the Mini today** |
| Parakeet 0.6b v2 int8 | STT batch | 483 MB | not stated (their recommended en engine) | CC-BY-4.0, token onsets | Likely beats whisper-base on accuracy at similar cost; unverified here |
| Moonshine base int8 | STT batch | 111 MB | not stated | MIT, English | Cheaper than whisper; not better |
| Supertonic-3 (agent copy) | TTS | 401 MB | "faster/lower-latency than Kokoro"; CoreML compile 8.4 s on M4; 44.1 kHz | 10 styles, 9 languages, **OpenRAIL-M** (use restrictions) | **Beats Kokoro on quality (44.1 kHz) and speed** per their notes; license needs a read before Fox ships it |
| Kokoro native (sherpa) | TTS | 103–350 MB | cold 6 s, warm 1–2 s/sentence | same weights as ours; 48 voices | Equal — same model, different runtime |
| Kitten nano int8 | TTS | 31 MB | 0.4–0.85 s per short sentence, ~10 ms/char | Apache-2.0, 8 voices | Beats Kokoro on **size/speed**, not quality |
| Pocket TTS int8 | TTS | 98 MB | first chunk 0.3–0.5 s | **restricted** (ONNX export non-commercial); "babbles 3–10× its text" — needs a runaway budget | Does not beat Kokoro; confirms parking Pocket |
| Piper | TTS | 13–67 MB | — | per-voice licenses, half restricted | Sachin already judged Piper robotic — skip |
| Matcha | TTS | 131 MB | loudness jumps 4–5 dB | 1 voice | Skip |
| ZipVoice clone | TTS clone | 208 MB | 0.22× realtime (slower than real time) | weights unlicensed, NC data — **restricted** | Skip for Fox |
| Silero VAD v6.2 | VAD | small | 32 ms frames | MIT | Same family as ours (we run v5-era weights with VAD_CTX=64) — retrained weights worth an A/B |
| Smart-Turn v3.2 | EOT | not stated | — | BSD-2 | Same as ours |
| CAM++ voiceprint | speaker | 28 MB | 6–23 ms per utterance on M4 | Apache-2.0 | New capability, cheap |
| MPNet addressee int8 | side-talk | 296 MB | 3.5 ms/sentence | Apache-2.0 | New capability |

Net: **two engines earn a place** — Nemotron streaming (latency) and Supertonic-3 (voice quality, license check first). Everything else is equal or worse than Kokoro, and the RAM budget on a 16 GB Mini that already pages allows one new ~0.5 GB model, not three.

## 3. Kagami — eyes and hands (CuaDriver, WINGSCRUM-555)

| Feature | OpenLive | Fox today | Gap | Adopt / borrow / skip |
|---|---|---|---|---|
| Computer-use helper | `openlive-cu`: Rust helper, own TCC identity via disclaim re-spawn, NDJSON over Unix socket, AX tree rendered as numbered lines (1,200 nodes / 64 levels) + 1280 px picture; model sends `elementIndex`; `AXPress → AXConfirm → AXOpen` then click at centre; app resolution exact bundle id → name → unique substring; password managers blocked | **CuaDriver 0.5.8** (`com.trycua.driver`), already granted Accessibility + Screen Recording, AX tree with `[element_index N]`, `som/vision/ax` capture, click/type/hotkey/set_value, recording + replay | Same lineage (THIRD_PARTY_NOTICES: `openlive-cu` consulted and adapted parts of Cua Driver — the project CuaDriver ships). CuaDriver already covers 555; theirs adds nothing we lack except Windows/Linux backends | **Skip** `openlive-cu` — we have the original. Borrow their tool-list shape (`listApps/listWindows/getAppState/click/setValue/typeText/pressKey/hotkey/scroll/drag`) as the contract for Kagami's tool names |
| Electron/Cowork AX blindness | Chromium AX "nudge" + fallback to posted click; no fix for web content | Measured: Cowork AX tree = menus only; `vision` capture works | Same wall, same fallback | Skip |
| Screenshots / OCR | `ol-input` 1024×768 capture, Vision OCR on macOS; helper has no OCR | CuaDriver `zoom` crops; no OCR tool in Fox | OCR on screen text is missing in Fox | **Borrow**: Vision-framework OCR via a tiny Swift CLI (their `ol-input/src` shows the call) |
| Text-only model sees | `resolveVision()` picks a separate vision model; screenshots described (800 tokens, positional) and memoised per call | Not built | Needed for Sonnet-on-voice driving a screen | **Borrow** the describer prompt (`tool-images.ts`) |
| Consent | Asks once ("is it alright to act on this machine"), 20 s silence = no, persisted; Stop button; caption names the next action | 555 has no consent layer yet | Gap | **Adopt** the once-then-remember consent + spoken caption of the next action |
| Safety | Password-manager bundle ids blocked; UIPI refusal on Windows; secure-input detection on macOS | None | Gap | **Borrow** the block list + secure-input check |

## 4. The one conversation log

| Feature | OpenLive | Fox today | Gap | Adopt / borrow / skip |
|---|---|---|---|---|
| Shape | Three histories (Chat / Flow / Dictate) in SQLite + JSON under `~/.openlive`; Chat sessions live in the **agent's own** store (`~/.claude/projects/…`) and resume from either side; OpenLive's History merges its SQLite with Claude JSONL / Codex rollouts / Cursor / OpenCode | OpenClaw gateway: many sessions keyed by `sessionKey` (`agent:main:ios-<uuid>` per app connection), fork/archive/snooze; a single timeline only by pinning `mainSessionKey` | Neither is "one log". Theirs is closer: one conversation = one agent session, reused with `claude --resume` | **Borrow** "the session is the agent's own, resumed by id" — it is what makes 514's warm CLI and one log the same problem |
| Cut-off handling | Reply truncated to what was voiced; "[user cut you off after: …]" note on the next prompt | AC19 cut fraction → text | Equal; their note-to-the-model is a nice touch | Borrow (one line) |
| Retention | Per mode: forever / 1-7-30 days / clear-all; open sessions never deleted | Not defined | Gap, product-level | Borrow the retention table |
| Export | Conversation → Markdown | Not built | Minor | Later |

## 5. Blob / orb UI

| Feature | OpenLive | Fox today | Gap | Adopt / borrow / skip |
|---|---|---|---|---|
| The orb | 416×460 transparent click-through window over the dock; states listening (teal) / thinking (violet) / acting (magenta + caption strip + Stop) / speaking (blue) / error (dark red + card); hover controls; tray mirror. Wave orb adapted from a third party (THIRD_PARTY_NOTICES "Orb") | Blob service :3212 (dead), the Fox app vision: one screen, blob, text box, mic→Enter; Talk Mode on the phone | Theirs is a finished state machine with failure cards; ours is a vision | **Borrow** the five states + failure-card pattern as the spec for Fox's blob; UI code itself is React/Electron — reuse the idea, not the component |
| Summon | Double-tap Control anywhere (Rust `ol-input` hook, 2 taps ≤400 ms) | Whisper dictation app for PTT; no global summon for Fox | Gap on the Mac | **Adopt** the double-tap pattern (hotkey from `ol-input` is ~200 lines of Rust) |
| Caption strip | Live word-by-word captions + "next action" caption while acting | Captions in Talk Mode (gaps 2/6) | Equal on the phone; missing on the Mac | Borrow |
| Mode switch | Chat / Flow / Dictate, each with Ready-at-a-glance and a one-tap fix | Not applicable yet | — | Borrow "Ready + the one thing missing as a button" |

## 6. Kura memory

| Feature | OpenLive | Fox today | Gap | Adopt / borrow / skip |
|---|---|---|---|---|
| Store | `memory.json`: ≤300 notes × ≤240 chars, newest-first 2,000-char prompt budget; no decay, no embeddings | kura-r2: 9,708 utterances / 511 episodes / 354 topics, FTS5, bitemporal HLC; consolidation tables empty | Theirs is a notes jar; ours is a real store with a retrieval problem | **Skip** their store |
| Writer | Only the `remember(note)` tool (any brain, incl. coding agents over MCP) or the user; **no automatic extraction** | Dream nightly + seeded ingest; no fact extractor either | Same gap on both sides | — |
| Injection | Rendered block in every system prompt ("WHAT YOU REMEMBER ABOUT THIS USER … use naturally, don't recite"), ACP preamble once per session | Retrieval over bootstrap (189) in progress | Their budgeting rule (walk newest-first, stop at first non-fit) is the right shape for a 2 k-char slot | **Borrow** the budget walk + the prompt wording |
| Shared across brains | Coding agents told to use OpenLive's `remember`, "never your own memory files" | Three agents (Raven/Fox/Sky) write to one store — the K5 goal | Their loopback MCP is exactly how to give Claude Code a `remember` that lands in Kura | **Adopt** the pattern: Kura as an MCP tool pair (`remember`/`recall`) served loopback |
| Edit / forget | Settings → Memory, `/memory` routes | Not built | Gap | Borrow |

## 7. Plumbing worth noting (ACP, MCP, store)

| Feature | OpenLive | Fox today | Gap | Adopt / borrow / skip |
|---|---|---|---|---|
| Driving Claude Code by voice | ACP over stdio: `initialize` → `session/resume` → `session/load` → `session/new`; one `session/prompt` per turn; `session/cancel` on barge-in; supervisor (60 s start / 30 s first output / 60 s stall, one restart re-seeded with last 40 turns); permission relay spoken, yes = `allow_once` never `allow_always`, 120 s auto-deny | Fox calls the claude shim per turn (`chie/call.js`), 3.9 s fixed overhead; no ACP | ACP's `session/resume` + `persistSession` is a **warm, resumable** Claude Code — the thing 514 is trying to build | **Adopt** ACP (`claude-agent-acp` adapter, pinned 0.100.0) as the warm-CLI mechanism; measure first-token on the Mini before committing |
| Tools reach both brains | One `ToolRegistry` → `ToolSet`; `serveMcp` publishes it as a loopback MCP server `openlive` and passes it in `session/new mcpServers` | fox-gate + wingman MCP :5691 | Same idea as our wingman MCP, done generically | Borrow the registry → loopback shape |
| Connector imports | Reads Claude Desktop / Claude Code (`~/.claude.json`) / Codex / Cursor / Gemini / VS Code MCP configs; OAuth tokens never reach the agent process | Hand-wired `oc mcp` | Convenience | Later |
| Secrets | AES-256-GCM `iv:tag:data`, key from env or `secrets/.enc-key` (randomBytes + `linkSync` race guard); malformed key = hard fail | `.fox-secrets` files mode 600 | Theirs is better hygiene for API keys | Borrow if Fox ever stores provider keys |
| Telemetry | Anonymous counts, on by default in packaged builds, `OPENLIVE_TELEMETRY=0` / `DO_NOT_TRACK=1`; **a fork built from source sends nothing** | — | Confirms the fork is safe to run | — |

## Where they are ahead, where we are ahead

**Ahead of us:** streaming STT with live partials; pause-classify-resume barge-in (our gap 5); mid-thought hold/merge (gap 7); voiceprint + side-talk; the acoustic regress harness; a finished orb state machine with failure cards; consent-once for computer use; ACP as a warm resumable brain; a generic tool registry served to every brain over loopback MCP.

**Ahead of them:** a real memory store (kura-r2 bitemporal FTS vs a 300-note jar); the phone as client (their loop needs a desktop renderer — there is no iOS app, and the thick-client design does not port); CuaDriver is the project their helper borrowed its layout from; our thresholds are tuned on Sachin's real speaker clips; one voice chosen; the kids-tutor guard stack; no telemetry decisions to make.

## The two options

| | A) OpenLive as Fox's voice + vision layer | B) Keep ours, pull in their best parts |
|---|---|---|
| What it means | Run the fork's agent service beside the gateway; Fox's brain answers over its provider adapter or ACP; the desktop app becomes Fox's Mac client | voice-v1-base stays; port five components (below) into `~/fox/modules/koe` and Kagami |
| Effort | 3–4 weeks: port the thick-client loop off Electron for the phone (there is none), rewire Kura in place of memory.json, re-tune 24 thresholds inside their state machine, carry 943 files and a pnpm/Rust toolchain | 1–2 weeks: each part is 40–400 lines, provenance-recorded under Apache-2.0 |
| Risk | High: the phone path is unsolved (no iOS client, loop lives in a browser renderer); two memory stores; our tuned numbers lost; a second gateway-sized service on a paging Mini; drift from upstream (689→731 commits in weeks) | Low: each borrow is tested against `koe-drift` and the speaker test; nothing replaces the gateway |
| Impact | Gaps 5 and 7 solved by their code; Mac orb + Flow for free; but gap 1 (first-turn lag) is **not** solved by it, and Talk Mode on the phone regresses | Gaps 5 and 7 solved by porting their state machine; streaming STT lands; Kura stays canonical; 514 can use ACP |
| **Recommendation** | No | **Yes** |

## Top 5 to take first (option B)

1. **Pause-classify-resume barge-in** (gap 5): `pauseReply` / `resumeReply` / `cutReply` + the learned noise floor — `apps/web/src/lib/live/voiceEngine.ts` (barge section), ported into `modules/koe/voice/index.js` behind a config key, drift test extended.
2. **Mid-thought hold and merge** (gap 7): `pending` + `scheduleHold` (4 s hold, 20 s max) from `onSpeechEnd` — same file; closes "quick follow-ups merged into one turn".
3. **Nemotron streaming STT** as a sherpa-onnx service on the Mini next to Whisper (464 MB; keep Whisper as fallback) — their `native-worker.ts` session logic (pre-roll drain, 0.42 s end pad, 3 s timeout → batch fallback) is the spec. Measure RAM first; it is the one new model the Mini can afford.
4. **ACP as the warm brain** for 514: `claude-agent-acp@0.100.0` driven like `acp-agent.ts` (`session/resume`, `persistSession`, `allowedTools`), measured against the 5.9 s / 2.0 s floor before any gateway fork.
5. **Kura over loopback MCP** (`remember` / `recall`) so Claude Code, Fox and Raven write to one store — `capabilities/mcp.ts serveMcp` is the shape; plus their newest-first 2 k-char budget walk for injection.

Then, cheap and later: Supertonic-3 after a license read; the five orb states + failure cards as the blob spec; consent-once + spoken next-action caption for Kagami; acoustic regress metrics; `evalstate/mcp-webcam` stays a candidate camera for the robot table (not used by OpenLive — their camera is `getUserMedia` in the renderer).

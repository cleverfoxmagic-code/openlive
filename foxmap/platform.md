# Platform — store, harness, wire protocol, history, desktop shell, Dictate

HEAD 65f2420. Everything OpenLive owns lives in one home folder; two local servers (Next web, Hono agent) plus an Electron shell; no native module in the servers except the optional sherpa-onnx voice path.

## 1. The store (`packages/db`, `packages/shared/src/home`)

### Layout (`home/index.mjs:38-67`, `docs/ARCHITECTURE.md:1346-1369`)

```
~/.openlive/                     (OPENLIVE_HOME; legacy OPENLIVE_DATA_DIR; dev checkout = <repo>/data)
  settings.json                  plain key/value; per-chat keys bind:/agentCwd:/acpSession:/agentCut:<chatId>
  mcp.json                       connectors {"mcpServers": …}
  memory.json                    [{ id, text, at }]
  skills/                        user Agent Skills (OPENLIVE_SKILLS_DIR)
  secrets/ (0700)                .enc-key, providers.json, connectors.json, settings.json, backup/
  data/                          openlive.db (+ -wal/-shm), voice-profiles.json, voice-accel.json, models/, voices/, addressee-*
  flow/                          config.json, sessions/<stamp>_<id>.jsonl, assets/<id>/, lease.json, dictations.jsonl
  state/                         ui.json, skills.json, reminders.json, window-state.json, appearance.json, preferences.json,
                                 once.json, server-pids.json, telemetry.json, telemetry-queue.jsonl, telemetry-off, portal-token, migration.json
  logs/                          agent.log (5 MB rotation, 2 kept)
  cache/                         debug/, scratch/, checkpoints/<ws-hash>/{blobs,journal.json}
  workspace/                     Flow's / Dictate's agent cwd
```

`resolveHome` (`index.mjs:30-35`): `OPENLIVE_HOME` → `OPENLIVE_DATA_DIR` → `~/.openlive` when packaged (only Electron main knows, it passes `OPENLIVE_HOME` to both servers, `main.cjs:372, 389`) → `<repo>/data` in dev. `PATHS` is resolved once at import in `packages/db/src/paths.ts:40` and `migrateHome` runs right there (line 42).

### Schema

- **SQLite** (`node:sqlite`, built into Node ≥22.13, no native dep; `sqlite.ts:131-184`): `meta(key,value)`, `chats(id, title, created_at, updated_at, agent_id, cwd, agent_session_id)`, `messages(seq AUTOINCREMENT, id UNIQUE, chat_id FK CASCADE, role, content JSON MessageBlock[], live, created_at)`, index on `(chat_id, seq)`. PRAGMAs: WAL, busy_timeout 5000, synchronous NORMAL, foreign_keys, `secure_delete ON`; deletes also `wal_checkpoint(TRUNCATE)` so freed pages and WAL copies are scrubbed (`scrubDeleted`, 199-201). Two processes (web + agent) each hold one lazy connection; `withBusyRetry` retries one SQLITE_BUSY.
- **JSON files** (`store.ts`): atomic temp+rename writes (`writeAtomic`, mode 0600); every read-modify-write through `updateJson` under `proper-lockfile` on `<file>.lock` (stale 15 s, update 2.5 s, 15 retries) plus an in-process promise chain per file (lines 95-129). A hand-broken JSON file is never overwritten (line 123).
- **Providers** (`queries.ts:15, 28-106`): `[{id, name, kind, apiKeyCiphertext, keyLast4, isDefault}]` in `secrets/providers.json`; the UI only ever sees `keyLast4`/`hasKey`; `getProviderApiKey` decrypts server-side only.
- **Settings** (`queries.ts:226-259`): plain in `settings.json`; keys in `SECRET_SETTINGS = ["exa_api_key", "voiceprint"]` (`index.mjs:19`) are routed transparently to `secrets/settings.json` encrypted.
- **ui.json** (`db/src/ui-state.ts`, `/api/ui-state`): renderer zustand groups `ui / disclosure / voice / sessions / onboarding`, patched under the same lock, broadcast to other windows; a corrupt file is set aside as `ui.json.corrupt`.

### AES-256-GCM key handling (`home/index.mjs:84-127`, `db/src/crypto.ts`)

- Key precedence: `OPENLIVE_ENC_KEY` (must be exactly 64 hex chars; malformed **throws** rather than falling back, so data is never encrypted under an unintended key) → `secrets/.enc-key`, auto-created with `randomBytes(32)`; written to a temp file and `linkSync`ed into place so two processes racing on first boot both end up with the same key (lines 105-110).
- Ciphertext format `iv(12B):tag:data`, all hex (`encrypt`, 114-119). Key is loaded lazily once per process (`crypto.ts:9-10`).
- A value that no longer decrypts (key changed) is skipped, never thrown: provider key → null, connector secret → left out, secret setting → undefined (`queries.ts:102-106, 228-231`; `connectors.ts:168-175`).

### Migration (`home/index.mjs:165-368`)

`migrateHome(home, {from, userData})` runs once (marker `state/migration.json`), under a `mkdir`-based folder lock (30 s stale takeover). Moves the old flat `data/` entries into `secrets/ data/ state/ cache/` (`DATA_MOVES`), Electron userData files into `state/`, splits `settings.json` (`agent_notes` → `memory.json`, secret settings → encrypted `secrets/settings.json`, backups to `secrets/backup/`), and `connectors.json` → `mcp.json` + `secrets/connectors.json` (ciphertext moved as-is). Every step is a rename or a byte-verified copy (`sameTree`), so a crash leaves each file in exactly one place and the next start finishes. `MIGRATED.txt` is left in the old folders. `~/.openlive` itself is never reshaped in place. A separate one-time import moves legacy `conversations.json` into SQLite under its own lock (`migrate-conversations.ts`, renamed to `.migrated.bak`).

Reset: Settings → About → Reset local data → `wipeHome` refuses roots, relative paths and anything containing the user's home (`wipeRefusal`, 136-145); `main.cjs:1434-1450` clears Chromium storage, wipes, re-writes `telemetry-off` / `once.json` and relaunches.

## 2. Harness (`packages/harness`)

- **Providers** (`registry.ts:13-…`, 15 built in): Anthropic, OpenAI, MiniMax (Anthropic protocol with quirks `noCacheControl, noThinking, bearerAuth`), Ollama local (`openai` /responses, keyless, URL from `ollamaBaseUrl` setting), Ollama Cloud, Groq, OpenRouter, DeepSeek, Mistral, xAI, Google Gemini (OpenAI-compat endpoint), Together, Fireworks, Cerebras, Perplexity. `ProviderInfo { id, name, protocol, baseURL, envKeys?, keyless?, quirks?, custom? }` (`types.ts:89-102`).
- **Three wire adapters**, selected by `protocol` (`index.ts:152-161`): `anthropic` → `/messages` (`anthropic.ts`, with `cache_control: ephemeral` on system, last tool and last lasting message, transient tails placed after the cache breakpoint, lines 23-103), `openai` → `/responses` (`openai-responses.ts`), `openai-chat` → `/chat/completions` (`openai-chat.ts`). A 400 that tools may have caused is retried once without tools and the model remembered for the session (`streamOpenAICompatible`, 165-189).
- **Streaming shape**: `streamProvider(provider, apiKey, ChatRequest, signal): AsyncGenerator<ProviderEvent>` where `ProviderEvent = text | reasoning | reasoning_signature | tool_start{index,id,name} | tool_delta{argsDelta} | tool_stop | usage{input,output} | done{stopReason}` (`types.ts:121-130`). `ChatRequest { model, messages: Message[], tools: ToolDef[], effort?, reasoningEffort?, maxTokens?, toolChoice?: "none" }`; `Message` = system | user{text, images?, transient?} | assistant{text?, reasoning?, reasoningSignature?, toolCalls?} | tool{callId, name, result, isError?, images?} (36-66).
- **Effort** (`effort.ts`): `Effort = low|medium|high|xhigh|max`; Anthropic budget map 2048…16384 tokens or adaptive `output_config.effort` per model family (`anthropicThinkingForm`, 227-233); OpenAI collapses xhigh/max to high; chat-completions providers expose no knob. `isReasoningModel(id)` (237-240). Live mode defaults to minimal/none for latency (`providers.ts:73-76`).
- **Model listing** (`models.ts:80-97`): live `/models` (Anthropic `/models?limit=1000` with `x-api-key`) enriched from the models.dev catalog (`catalog.ts`, cached 24 h in `cache/models.json`), filtered of non-chat ids, fallback to catalog then `MODEL_SNAPSHOT`. `ModelInfo` carries `contextWindow, maxOutput, reasoning, vision, cost{input,output per 1M}, live`.
- **Retry** (`retry.ts`): pre-stream fetch retry with backoff on 5xx/429/529 and `retry-after`, never after bytes streamed.
- **Cost**: ACP `usage_update.cost.amount` → `usage.costUsd`; the API path reports `costUsd: 0` (`turn-runner.ts:246`) with token counts; `ModelInfo.cost` is for the picker.

## 3. Shared wire protocol (`packages/shared/src/live-events.ts`, `sse-events.ts`)

One `/live` WebSocket per renderer (chat: `?chat=<id>&lang=&device=1`; Flow: `?flow=1`), authenticated by `x-openlive-secret` header or `?token=` (`live/ws.ts:47-57`).

Client → server (`liveClientMsgSchema`, 194-256): `user_text{text, frames[], lang, turn, wordsAt, speaker, aside, typed}`, `cancel{spoken}`, `control{camera_on|camera_off|screen_on|screen_off|end}`, `frame_response`, `tool_bridge_result`, `bind{agentId, cwd, resumeSessionId}`, `permission_response{reqId, optionId}`, `elicitation_response{reqId, action, content}`, `set_model`, `set_mode`, `set_option`, Flow: `flow_text`, `flow_cancel`, `flow_resume`, `flow_new`. Binary frame tag `0x02` = JPEG for `look` (line 45).

Server → client (`liveServerMsgSchema`, 97-182): `sse{event, turn}` wrapping the chat SSE union, `need_frame`, `tool_bridge{op: clipboard_read|clipboard_write|open_url|flow_insert|flow_insert_end|flow_context|flow_device|flow_dictate}`, `permission{reqId, question, options[{id,label,kind}], expiresAt, toolCallId, turn}`, `permission_resolved`, `agent_meta{models, currentModelId, modes, currentModeId, options, commands, resumeAcrossRestart}`, `elicitation` / `elicitation_resolved`, `reload_history`, `bound_state{agentId, cwd, agentActive}`, `flow{event}`, `error`, `reminder{title, body}`.

SSE event union (`sse-events.ts:11-44`): `text_delta`, `reasoning_delta`, `tool_start{id,tool,summary}` / `tool_done`, `acp_tool_call{call}` / `acp_tool_update{delta}`, `term_output` / `term_exit`, `todos`, `usage{contextTokens, outputTokens?, contextSize?, costUsd}`, `status`, `say` (voiced, never persisted), `done`, `error{message, code}`. Every event echoes the client's `turn` number so a cancelled turn's late events never land in the next.

Flow has its own event union (`flowEventSchema`, 71-91) and the shared `MessageBlock`/`ToolCallState` persistence types (`types.ts`, `tool-call.ts`).

## 4. History

- **Chat**: SQLite chats/messages; `chatHistory` setting ∈ `off|day|week|month|forever` (`flow-store/src/shared.ts:9-16`), pruned by `deleteChatsBefore` when History is read and as a call starts, never the open chat (`session.ts:188-189`, `history/route.ts:24-26`); per-chat settings keys are deleted with the chat (`queries.ts:168-188`). Empty chats (lobby connects) are hidden. `GET /api/history` groups workspace → chats and merges the agents' own on-disk sessions deduped by `agent_session_id` (`history/route.ts:34-58`). Discovery parsers per registry `sessionParser` (`agentSessions.ts:182-189`): Claude JSONL (cwd + first non-boilerplate user text from the first 1 MB), Codex rollouts (`session_meta`), Cursor `meta.json`, OpenCode/Hermes read-only sqlite; plus the agent's own ACP `session/list` with a 2.5 s wait (`readListedAgentSessions`, 222-235). External sessions can be deleted for Claude/Codex/Cursor only (`deleteExternalSession`, 241-281).
- **Flow**: `flow/sessions/<UTC stamp>_<id>.jsonl` append-only logs (header line, then entries `message|tool_call|tool_result|session_state|context|compaction|cut|cancel|custom`, `flow-store/src/types.ts:125-162`), assets per session, a `lease.json` for ownership; listing is a name sort plus bounded head reads (`history.ts:17-23`); retention `config.history` applied by `keepSessions` on first page read and session open (`history.ts:165-168`); cuts are resolved on load (118-134).
- **Dictate**: `flow/dictations.jsonl`, one line per dictation `{id, at, raw, cleaned, final, app?, windowId?, command?, copied?}`, cap 1000, 4000 chars per field, rewritten (temp + rename) on delete/clear/expiry (`dictations.ts`); retention from Settings → Dictate.

## 5. Desktop shell (`apps/desktop/main.cjs`)

**Process tree.** Electron main → `utilityProcess.fork` of `resources/agent/agent.mjs` and `resources/web/server.js` (Next standalone) with `stdio: inherit` (`spawnServer`, lines 308-361) → the agent's own children (ACP adapters in their own process groups, stdio connectors, computer-use helper, native voice workers). Dev (`ELECTRON_DEV=1`) spawns nothing: `pnpm desktop:dev` runs web+agent via concurrently (`package.json:29`).

**Ports.**

| Port | Role | Where |
|---|---|---|
| 3000 | Next web dev (`pnpm dev`) | `free-ports.mjs:21`, `server.ts:21` default `WEB_PUBLIC_URL` |
| 8787 | agent default (`AGENT_PORT`) | `server.ts:99` |
| 47833 / 47834 | agent / web under `pnpm desktop:dev` | `package.json:29`, `main.cjs:61-62` |
| 47823 / 47824 | agent (preferred, may move) / web (fixed) in the packaged app | `main.cjs:60-62` |
| 9333 | Chrome DevTools Protocol for the dev Electron (`--remote-debugging-port`) | `apps/desktop/package.json:11`; disables telemetry (`telemetry/config.cjs:38`) |

`ensurePortsFree` (`main.cjs:248-279`): reaps pids recorded in `state/server-pids.json` from a previous killed run (`prev-exit.cjs` classifies clean / os_restart / killed / unknown), kills a holder only when it is one of **our** service names, moves the agent to a random free loopback port if a foreign app holds 47823, and refuses to start if the web port is foreign. `scripts/free-ports.mjs --sweep 3000 8787 47834 47833 9333` runs before `pnpm dev` / `desktop:dev` (lsof/ss/netstat + kill). Service crash policy: backoff `500,1000,2000,4000,8000,15000` ms, reset after 60 s uptime, then a Retry/Quit dialog (`service-restart.cjs`, `main.cjs:340-359`).

**Security plumbing.** Per-launch `AGENT_TOKEN` (24 random bytes) handed to both servers as `OPENLIVE_AGENT_SECRET` and to renderers via argv `--openlive-agent-port/--openlive-agent-token` (`main.cjs:74, 420-422`); a second `SETTINGS_TOKEN` only the web server sees, proving a native dialog confirmed a non-local Ollama URL (line 79). Agent binds `127.0.0.1` only; a non-loopback bind without a secret exits (`server.ts:105-110`).

**Windows.** Splash (`createSplash`), main `BrowserWindow` (1180×800 default, `titleBarStyle: hidden` on macOS, frameless elsewhere, sandboxed preload, `backgroundThrottling: false` so the voice loop keeps running minimized, external links to the OS browser, navigation pinned to `WEB_URL`; lines 599-690), the hidden Flow **owner** window loading `/flow-owner` (480×320, never shown, runs the voice loop; `createOwnerWindow`, 785-796), and the **orb** panel window loading `/flow` (`makePanelWindow`: transparent, frameless, `focusable: false`, macOS `type: "panel"`, always-on-top "floating", visible on all workspaces; click-through with pointer polling so the orb takes clicks back; sized 416×460 centred over the dock, `flowBounds`, 801-810). Both Flow windows are created at boot so a summon is an animation, not a load (`boot`, 1715-1716).

**Media permissions.** `wirePermissions` (`main.cjs:132-137`): `setPermissionRequestHandler` grants `media`, `clipboard-read`, `clipboard-sanitized-write`; `setPermissionCheckHandler` grants `media` only. OS-level mic/camera/accessibility/screen-recording grants are the app's own (Welcome walks through them); the computer-use helper is a separate signed app so its TCC grants are its own.

**Tray.** `tray-menu.cjs` builds the menu as data: Flow status line + hotkey, Dictate line, Open OpenLive, New call, Start Flow, Turn Flow on/off, Turn Dictate on/off, How you talk (Hands-free / Push to talk), Allow Accessibility… when needed, Settings…, Quit (lines 73-103). Closing the main window hides to the tray; `before-quit` on macOS with the Dock visible closes to the menu bar instead (`main.cjs:1752-1757`); only the tray's Quit quits. `killChildren` SIGTERMs the service trees, waits 2 s, SIGKILLs survivors and deletes the pid file (1737-1746).

**Telemetry switch.** Main is the only sender (`telemetry/index.cjs`). Active only when packaged, a stamped `telemetry-config.json` exists (endpoint https, UUID clientId), `ELECTRON_DEV` is off, no `--remote-debugging`/`--inspect`, no `OPENLIVE_FLOW_HOME`, and neither `OPENLIVE_TELEMETRY` (anything but `1|true|on`) nor `DO_NOT_TRACK` opts out (`config.cjs:28-47`, fails closed). The user's off switch persists as `state/telemetry-off` (survives Reset, `main.cjs:1443`). Agent events arrive over `process.parentPort` (`spawnServer` line 318-322, which also carries `allow-foreground` and reminder `notify` messages).

**Boot order** (`boot`, 1660-1721): telemetry.start → menu, tray, appearance, permissions, IPC wiring → ol-input hotkey bindings from Flow config → optional login-item default → splash (unless launched at login) → `startServers` → `waitForServers` (poll both URLs up to 60 s) → main window → owner + orb windows → auto-update.

## 6. Dictate

Pipeline (`docs/DICTATE.md:420-546`, code in `apps/web/src/lib/dictate/`, `services/agent/src/dictate/`):

1. **Hotkey.** The Rust `ol-input` hook (`native/ol-input/src/coordinator.rs`) reports `double_tap` for Dictate's toggle binding (default Option/Alt) or `hold_start/hold_end/hold_cancel` for the push-to-talk key (Fn on macOS, Right Ctrl elsewhere; `flow-store/src/shared.ts:24-38`); main registers bindings on every config change (`flow-input.cjs`) and routes effects to the owner renderer (`main.cjs:977-983`).
2. **Routing.** `createTalk` (`lib/flow/talk.ts`) owns one open session; `useFlowOwner` hands each finished utterance to Dictate first while it is active, so it never reaches Flow's brain.
3. **STT.** The same `VoiceEngine` (`beginPtt`/`endPtt`), tape checked for speech with Silero before transcribing (`lib/live/tapeSpeech.ts`); captions from the tape.
4. **Local rules** (`lib/dictate/cleanup.ts:259`): one O(n) pass per rule — fillers (`dropFillers`), backtrack ("actually", "no wait", "scratch that"), lists, numbers (≥10 → digits), punctuation/capitals (English rules; other languages get a capital and a closing mark only). Then the user's dictionary and snippets (`words.ts`, limits `DICTATE_LIMITS` words 2000 / snippets 500), spoken commands, and `needsSpace` (`spacing.ts`) using the field's text before the caret from ol-input `focusEditable()`.
5. **Typing.** `insertBegin/Push/End` → ol-input paste or type (clipboard restored); inside OpenLive's own window `webContents.insertText`; a secure (password) field types nothing, copies nothing, logs nothing. No focused text box → clipboard + "Copied instead." (`run.ts:125-126`).
6. **AI polish / edit by voice** (off by default): `POST /api/dictate/rewrite` → agent `/dictate/rewrite` (`dictate/routes.ts:18-40`) answering NDJSON `{delta}`… then `{text}` or `{error}`; `rewrite()` (`rewrite.ts:186-199`) picks the brain from `dictateBrain(flowConfig, settings)` (its own, else Flow's, else the default): API → `streamProvider` with `tools: []` (`apiRewrite`, 105-115); ACP → a warm `AcpAgent` started toolless in `~/.openlive/workspace` with Dictate's own preamble, no MCP servers, every permission refused (`startAgent`, 149-162), kept 5 idle minutes / 20 turns, one turn at a time. Prompts carry tone (`natural|casual|formal`) and a guarded `<context>` block (≤320 chars before the cursor, last 5 dictations ≤1200 chars, never followed as instructions, `contextBlock`, 39-59). Client deadlines: polish 25 s, command 45 s (`run.ts:141-143`); on failure the cleaned words are typed instead and the full text is copied.
7. **History.** `addDictation` to `flow/dictations.jsonl` per Settings → Dictate retention; `GET /api/dictate/history`.

The `set_dictation(on)` tool (`capabilities/text.ts:126`) lets any brain toggle hands-free Dictate through the `flow_dictate` bridge op.

## Surprises

- The agent's port can move at launch (47823 taken → random), so the renderer learns it from argv; the web port never moves because the origin keys localStorage and the cached voice models.
- `secure_delete` + WAL truncate on every delete: "deleted" chats are scrubbed from disk, not just unlinked.
- A malformed `OPENLIVE_ENC_KEY` crashes on purpose rather than silently generating a file key.
- Telemetry is off by construction in any dev build, any build with a debugging port, and any build without the release-time stamped config.

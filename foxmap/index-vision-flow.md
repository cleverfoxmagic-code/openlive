# OpenLive — file → feature index (vision, Flow, native addons)

Repo: github.com/katipally/openlive @ 65f2420. Every file read for `vision.md` and `flow.md`. Paths relative to the repo root.

| path | feature | one-line role |
|---|---|---|
| README.md | overview | Product pitch; "It can see" (L120-122), Flow summary (L168-215), privacy, repo map (L457-475) |
| docs/FLOW.md | Flow | User + developer guide: summoning, orb states, tool table, consent, failure cards, platform matrix, architecture diagram (L478-561) |
| docs/ARCHITECTURE.md | all | Voice loop step 4 (frames ride `/live`, L148-157), Tools registry (L612-671), Computer use helper (L673-900), Flow (L1272-1297) |
| THIRD_PARTY_NOTICES | provenance | Orca (tree heuristics, AX-first click, helper launch), Cua (WGC capture sequence, a11y switch), Orb (wave orb preset) |
| apps/web/src/lib/live/cameraCapture.ts | vision A/B | `CameraCapture`: getUserMedia/getDisplayMedia, 1 fps sampler, 6-frame buffer, `captureFreshest`, `captureHiRes(1280, 0.86)` |
| apps/web/src/lib/live/useLiveSession.ts | vision A/B | Attaches freshest camera/screen frame to each turn (L734-755); answers `need_frame` with a hi-res grab (L467-476); camera/screen toggles; `camera_frame` via share |
| apps/web/src/lib/live/liveClient.ts | wire | `/live` client: `user_text` with `frames[]`, `flow_text`, `control`, `frame_response`, binary `0x02` frame, `tool_bridge_result`, permission messages |
| apps/web/src/lib/look.ts | not vision | Glass/Flat appearance "look" (unrelated to the `look` tool) |
| apps/desktop/look.cjs | not vision | Pure Glass/Flat support decision for Electron main (unrelated to the `look` tool) |
| services/agent/src/capabilities/assistant.ts | vision B | `look` tool definition (L69-88) plus `delegate`, `update_todos`, `remember` |
| services/agent/src/live/session.ts | vision A/B | Chat `LiveSession`: `share` port (L159), frame intake and barge-in frame merging, `requestFrame` handshake (L722-734), `onBinary`, `frame_response` |
| services/agent/src/live/turn-runner.ts | vision A/C1 | Provider brain: `describeFrames` (L24-35), transient view tail (`withView`), vision-model borrow, `[The user's camera came with this…]` notes |
| services/agent/src/agents/acp-agent.ts | vision A/C1 | ACP brain: `supportsImages` from prompt capabilities; image blocks or vision description or "can't view images" note (L773-805) |
| services/agent/src/providers.ts | vision C | `resolveVision()` reads `visionProviderId`/`visionModel` settings (L56-66) |
| services/agent/src/tool-images.ts | vision C2 | `takesImages` probe (Ollama / models.dev / heuristic); `prepareToolImages` rewrites tool pictures into descriptions or a blind note |
| services/agent/src/flow/retention.ts | vision/Flow | `KEEP_IMAGES = 3`, `trimImages` |
| apps/web/src/components/settings/ModelsSettings.tsx | vision C | Settings UI for the dedicated vision model (L50-83) |
| packages/shared/src/live-models.ts | vision | Model picker `vision` badge hints |
| apps/web/src/lib/flow/useFlowOwner.ts | Flow | Hidden owner renderer: open/close, health, mic/engine, `flowText`, Flow events → orb snapshot, tool bridge (`flow_insert`, `flow_dictate`, `flow_context`, `flow_device`, `camera_frame`), permission UI, Stop/close, power |
| apps/web/src/lib/flow/talk.ts | Flow | `createTalk`: double-tap and push-to-talk routing between Flow and Dictate, close-after-silence |
| apps/web/src/lib/flow/types.ts | Flow | `FlowPhase`, `FlowFailureCode`, `FlowSnapshot`, `TalkSnapshot`, `DictateSnapshot` |
| apps/web/src/lib/flow/bridge.ts | Flow | Renderer-side typed view of `window.openlive.flow` (permissions, insertion, context, signals, capabilities, device, summon/dismiss, effects) |
| apps/web/src/lib/flow/failure.ts | Flow | `deriveFailure`, `turnFailure`, model download offers: every failure card's code/title/fix |
| apps/web/src/lib/flow/quiet.ts | Flow | Auto-quiet decision (meeting app, mic busy, DND) |
| apps/web/src/components/flow/FlowOrb.tsx | Flow | Orb window: state mapping, caption strip + Stop, permission/failure cards, hover controls, `data-hit` click-through hit test |
| apps/web/src/lib/waveOrb.ts | Flow | WebGL wave orb; `WAVE_ORB_STATES` per phase (ported from LerSent001/orb) |
| services/agent/src/live/flow-ws.ts | Flow | `FlowLiveSession`: `flow_text`/`flow_cancel`, `run()` turn, `toolSession`, `brainFor` (LocalBrain vs AcpBrain + MCP), consent remember, asks, session persistence, asset cap 60 |
| services/agent/src/live/ws.ts | Flow | `/live` upgrade; `?flow=1` → `FlowLiveSession` (L63-66) |
| services/agent/src/flow/loop.ts | Flow | `runFlow`: the tool loop (context, trim, compact, stream, streamed insert_text, dispatch, state tail, no step budget) |
| services/agent/src/flow/brain.ts | Flow | `LocalBrain` (provider stream + `prepareToolImages`), `AcpBrain` (agent over ACP), `createProviderMapper`, `acpTurnInput` |
| services/agent/src/flow/prompt.ts | Flow | Flow system prompt `BASE`, `formatContext`, `buildFlowPrompt`, `buildFlowAcpPreamble` with namespaced MCP tool names |
| services/agent/src/flow/types.ts | Flow | `Brain`, `BrainEvent`, `FlowEvent`, `Msg`, `Usage` types |
| services/agent/src/capabilities/profiles.ts | tools | `CHAT` and `FLOW` profiles: tool order, prompt builder, approval policy |
| services/agent/src/capabilities/approval.ts | Flow | `consentApprove` (ask once, 20 s, remember) and `askEach` (Chat) |
| services/agent/src/capabilities/registry.ts | tools | One registry; `machine()` chooses CU tools + non-superseded ol-input tools; `unavailableTools` |
| services/agent/src/capabilities/dispatch.ts | tools | `dispatch` pipeline, `ToolSet`, `newestState` WeakMap and `asStateTail` (transient window state), `offerOf` |
| services/agent/src/capabilities/types.ts | tools | `Tool`, `Session` (share, device, computer, insert, foreground, clipboard, dictate, workspace…) |
| services/agent/src/capabilities/device.ts | ol-input seam | `DevicePort`, `ShotGeometry`, `ControlAction` union, `bridgedDevice()` over the tool bridge, `DEVICE_TIMEOUT_MS 40 s` |
| services/agent/src/capabilities/device-tools.ts | ol-input tools | `screenshot`, `read_screen_text`, `wait`, `list_windows`, `get_window`, `camera_frame`, control table (click…open_url), `shell`, auto-screenshot wrapper, capability refusals |
| services/agent/src/capabilities/text.ts | tools | `insert_text` (`ForwardOnlyInsertion`), `read_selection`, `clipboard_read/write`, `get_context`, `set_dictation` |
| services/agent/src/capabilities/groups.ts | tools | Tool groups and the Settings off-switch |
| services/agent/src/capabilities/input-lock.ts | tools | One machine-wide input lock across sessions |
| services/agent/src/capabilities/files.ts | tools | `list_dir`, `read_file`, `write_file`, `edit_file` |
| services/agent/src/capabilities/find.ts | tools | `find_files` (Spotlight / Windows Search / Everything) |
| services/agent/src/capabilities/checkpoints.ts | tools | `list_edits`, `undo_edit` |
| services/agent/src/capabilities/web.ts | tools | Worker tools `web_search`, `fetch_url` behind `delegate` |
| services/agent/src/capabilities/on-demand.ts | tools | `find_tools` / `read_tool` / `use_tool` wrappers for connector tools |
| services/agent/src/reminders/tools.ts | tools | `set_timer`, `remind`, `list_reminders`, `cancel_reminder` |
| services/agent/src/skills/tools.ts | tools | `activate_skill`, `read_skill_file`, `save_skill` |
| services/agent/src/connectors/setup.ts | tools | `list_connectors`, `add_connector`, `connector_sign_in`, `reconnect_connector` |
| services/agent/skills/computer-use/SKILL.md | CU | Prompt how-to the model loads before driving an app (adapted from Orca) |
| services/agent/src/telemetry/facts.ts | telemetry | Tool buckets incl. `t_look` |
| services/agent/src/computer/helper.ts | CU client | `ComputerHelper`: locate, spawn with `--socket --token-file`, NDJSON client, timeouts/restarts, `foregroundGrant` (Windows) |
| services/agent/src/computer/tools.ts | CU tools | `list_apps`, `list_windows`, `get_app_state`, `wait`, `read_screen_text`, `click`, `perform_action`, `set_value`, `type`, `keypress`, `scroll`, `move`, `mouse_down`, `mouse_up`, `drag`; `SUPERSEDED`; `outcome()` |
| services/agent/src/computer/routes.ts | CU | HTTP routes for helper permissions (not read in depth) |
| apps/desktop/main.cjs | Flow | Owner window (`/flow-owner`) and orb window (`/flow`): size, placement over dock, click-through, pointer polling, summon/dismiss IPC (L725-870) |
| apps/desktop/preload.cjs | Flow | `window.openlive` bridge: `bridge`, `panelState`, `flow.*` IPC names (`openlive:flow-device`, `openlive:flow-summon`, …) |
| apps/desktop/flow-input.cjs | ol-input bridge | Loads the addon, installs the hook, bindings (flow/dictate/ptt), armed switch, permissions, insertion IPC, secure-input poll |
| apps/desktop/flow-runtime.cjs | ol-input bridge | Context capture, auto-quiet signals, capabilities, `deviceCall` dispatcher (capture, OCR, windows, control, shell), OCR warm-up |
| apps/desktop/flow-cursor.cjs | Flow | Cursor halo overlay during device actions; transparent, click-through, hidden from capture |
| apps/desktop/flow-cursor-preload.cjs | Flow | Preload for the halo window |
| apps/desktop/linux-input.cjs | ol-input | `/dev/input` access probe → `not_in_group / needs_relogin / no_devices / sandboxed` |
| apps/desktop/orb-pointer.cjs | Flow | Pointer mode per platform (`forward` / `poll` / `solid`), window hit math |
| native/ol-input/Cargo.toml | ol-input | Crate deps: napi, handy-keys, arboard, png; objc2 (macOS), windows 0.62, x11rb |
| native/ol-input/index.d.ts | ol-input | The addon's full TypeScript surface (hook, insertion, permissions, capture, OCR, windows, input, capabilities) |
| native/ol-input/src/hook.rs | ol-input | Global keyboard hook on handy-keys; manager thread, bindings, suspend/resume |
| native/ol-input/src/coordinator.rs | ol-input | Pure double-tap / hold state machine; `DEBOUNCE`, `RELEASE_GRACE`, `TAP_MAX`, `DOUBLE_TAP` |
| native/ol-input/src/inject.rs | ol-input | Text insertion methods (paste/type), streaming insertion session, layout-resolved paste keycode |
| native/ol-input/src/paste_tx/mod.rs | ol-input | Receipt-sequenced lazy clipboard: restore only after the app read the paste |
| native/ol-input/src/clipboard.rs | ol-input | Save/restore user clipboard (text or image) via arboard |
| native/ol-input/src/capture.rs | ol-input | Display/window/region capture → PNG + `Shot`, capped 1024×768 |
| native/ol-input/src/coords.rs | ol-input | `Shot`/`ShotPoint`/`ScreenPoint`, `MODEL_MAX_WIDTH/HEIGHT`, the one pixel→screen conversion |
| native/ol-input/src/ocr.rs | ol-input | OCR facade returning boxes in image pixels |
| native/ol-input/src/motion.rs | ol-input | Bezier pointer glide at 125 Hz |
| native/ol-input/src/secure_input.rs | ol-input | macOS Secure Event Input detection |
| native/ol-input/src/platform/macos.rs | ol-input | CGEvent/Carbon/TIS FFI for hook shadowing, layout, posting |
| native/ol-input/src/platform/linux.rs | ol-input | Linux typing tool chain (`kwtype/wtype/dotool/ydotool/xdotool`), keysym helpers |
| native/ol-input/src/platform/desktop/macos.rs | ol-input | CGWindowList capture, window list, NSWorkspace open, AX selection, Vision OCR |
| native/ol-input/src/platform/desktop/windows.rs | ol-input | GDI capture, UIA selection, ShellExecute, Windows OCR, UIPI elevation check |
| native/ol-input/src/platform/desktop/linux.rs | ol-input | Screenshot tools, xdotool window control, xclip/xsel/wl-paste selection, AT-SPI python probes, tesseract OCR |
| native/openlive-cu/crates/core/src/protocol.rs | CU | Wire types: `Request`, `Response`, `ErrorCode`, `Handshake`, `Grant`, `AppInfo`, `WindowInfo`, `Snapshot`, `ActionReport`, `ActionResult`; `PROTOCOL_VERSION 1` |
| native/openlive-cu/crates/core/src/serve.rs | CU | Method table and per-connection loop; settle, re-resolve, snapshot after every action; pixel→desktop via last picture |
| native/openlive-cu/crates/core/src/backend.rs | CU | `Backend` trait, `Action`/`ClickAt`, `BLOCKED_APPS`, `refuse_blocked`, own-root detection |
| native/openlive-cu/crates/core/src/auth.rs | CU | Token file take-and-delete, constant-time compare |
| native/openlive-cu/crates/core/src/tree.rs | CU | Indexed accessibility-tree text renderer (caps, elision, compact tabs, line format, actions) |
| native/openlive-cu/crates/core/src/image.rs | CU | Picture policy: 1280 long edge, 900 KB, PNG→JPEG q90→shrink 0.8 |
| native/openlive-cu/crates/core/src/framing.rs | CU | NDJSON line framing (4 MiB cap) |
| native/openlive-cu/crates/core/src/keys.rs | CU | Chord parsing (`cmdorctrl`, modifiers) |
| native/openlive-cu/crates/core/src/geometry.rs | CU | `ShotGeometry`, `fit` |
| native/openlive-cu/crates/helper/src/main.rs | CU | Binary: `--socket --token-file`, private listener, 30 s unclaimed exit, owner-left exit |
| native/openlive-cu/crates/helper/src/disclaim.rs | CU (macOS) | TCC responsibility disclaim re-spawn so grants attach to "OpenLive Computer Use" |
| native/openlive-cu/crates/platform-macos/src/lib.rs | CU (macOS) | AX backend: `find_app`, `resolve`, `observe` (Chromium nudge), `act` (AXPress→Confirm→Open, set_value verify, replace-selection, select-all), grants via TCC |
| native/openlive-cu/crates/platform-macos/src/capture.rs | CU (macOS) | ScreenCaptureKit `SCScreenshotManager` window picture |
| native/openlive-cu/crates/platform-macos/src/ax.rs | CU (macOS) | AX attribute/action helpers |
| native/openlive-cu/crates/platform-macos/src/input.rs | CU (macOS) | CGEvent click/type/key posting |
| native/openlive-cu/crates/platform-windows/src/backend.rs | CU (Windows) | UIA backend: session-0 check, grants always-on, focus via SetForegroundWindow+SetFocus, UIPI refusal |
| native/openlive-cu/crates/platform-windows/src/uia.rs | CU (Windows) | UIA tree walk with CacheRequest; click pattern order Select→Invoke→Toggle→ExpandCollapse |
| native/openlive-cu/crates/platform-windows/src/capture.rs | CU (Windows) | Windows.Graphics.Capture (border off where possible) with PrintWindow fallback |
| native/openlive-cu/crates/platform-linux/src/backend.rs | CU (Linux) | AT-SPI backend for X11/Wayland: grants (`IsEnabled`, portal), resolve, observe, act, portal input, wl-clipboard paste |
| native/openlive-cu/crates/platform-linux/src/atspi.rs | CU (Linux) | AT-SPI tree source over zbus |
| native/openlive-cu/crates/platform-linux/src/desktop.rs | CU (Linux) | `org.a11y.Status.IsEnabled` switch, Cinnamon exception |
| native/openlive-cu/crates/platform-linux/src/portal.rs | CU (Linux) | xdg-desktop-portal RemoteDesktop/ScreenCast session, restore token |
| native/openlive-cu/crates/platform-linux/src/pipewire.rs | CU (Linux) | dlopen'd PipeWire frame grab for Wayland pictures |
| native/openlive-cu/crates/platform-linux/src/x11.rs | CU (Linux) | X11 windows, `GetImage` capture, XTEST input, keysym typing |
| native/openlive-cu/crates/platform-linux/src/ewmh.rs | CU (Linux) | EWMH window list and frame extents |
| native/openlive-cu/crates/platform-linux/src/roles.rs | CU (Linux) | AT-SPI role/action → AX vocabulary mapping; click action order |
| native/openlive-cu/crates/platform-linux/src/clipboard.rs | CU (Linux) | Clipboard ownership and restore after paste |

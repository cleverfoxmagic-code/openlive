# Index — ACP driving, MCP/skills/memory, platform (store, harness, protocol, history, desktop, Dictate)

`path | feature | one-line role` for every file read for `acp-driving.md`, `mcp-memory.md` and `platform.md` (HEAD 65f2420).

## Docs

| path | feature | role |
|---|---|---|
| `README.md` | overview | what OpenLive is, agent list, repo layout, port/dev notes |
| `docs/ARCHITECTURE.md` | architecture | ACP driver, resume, tools/MCP/connectors/skills/memory/reminders/find+undo, home layout, telemetry |
| `docs/CHAT.md` | chat | who answers, History drawer and retention |
| `docs/DICTATE.md` | dictate | cleanup rules, AI polish flow, developer architecture (hook → engine → rewrite → insert) |
| `CONTRIBUTING.md` | dev | dev ports (9333 CDP), evals, data folder |

## ACP agent driving (`services/agent/src/agents`, `packages/shared`)

| path | feature | role |
|---|---|---|
| `packages/shared/src/agent-registry.ts` | registry | `AGENT_REGISTRY`: 9 agents, adapter commands (pinned npx), bins, install/login, credProbe, sessionsDir/parser, ACP quirks (preamble, mcp, terminal, env, toolless) |
| `packages/shared/src/agent-start.ts` | start failures | `startReason` from stderr/exit code; `startMessage` wording; `AgentStartError` |
| `packages/shared/src/node/agent-node.ts` | node helpers | `widenedPath`, `commandOnPath`, `evalCredProbe` (file/json/fileMatch/keychain/anyOf), `terminalCommand` |
| `services/agent/src/agents/acp-agent.ts` | ACP driver | spawn adapter, `initialize`/`session/resume`/`session/load`/`session/new`, `_meta.claudeCode.options`, `session/prompt`, update mapping, permission relay, terminals, elicitations, `session/cancel`, `session/list`, dispose |
| `services/agent/src/agents/supervisor.ts` | reliability | per-turn watchdogs (start/first-output/stall), restart-once with text history seed, spoken failure |
| `services/agent/src/agents/types.ts` | types | `Agent`, `TurnInput`, `AskPermission`, `PERMISSION_CANCELLED`, `AgentMeta`, `ReplayMessage` |
| `services/agent/src/agents/index.ts` | binding | `boundAgent`, `agentCwd` (realpath), `createBoundAgent` (supervisor + AcpAgent + MCP wire), `flowAgentCwd` |
| `services/agent/src/agents/mcp-config.ts` | .mcp.json passthrough | `readProjectMcpServers` (cap 20, http/sse gated), `hostedBy` title match |
| `services/agent/src/agents/pi-bridge.ts` | Pi | temp 0700 dir with launcher + `pi.registerMcpServer` extension carrying OpenLive's servers |
| `services/agent/src/agents/proc.ts` | process trees | `track` + exit reaping, `killTree` (PG SIGTERM→SIGKILL, taskkill /T) |
| `services/agent/src/agents/terminal-manager.ts` | ACP terminals | client-hosted `terminal/*`: spawn, tail-capped output, 80 ms live flush, kill/release |
| `services/agent/src/agents/models-route.ts` | probes | `GET /agents/models` (session/new probe, 5 min cache), `GET /agents/sessions` (initialize-only `session/list`, 60 s cache, PATH-gated) |
| `services/agent/src/live/session.ts` | LiveSession | `/live` chat session: bind, turn, permission/elicitation relay (120 s), barge-in cut, replay ingest, MCP server, persistence |
| `services/agent/src/live/narrator.ts` | spoken progress | `wrapEmitWithNarration` (`say` lines) and `createCommentaryGate` |
| `services/agent/src/live/turn-runner.ts` | API brain | provider turn loop (6 steps + tool-free last), `describeFrames`, history cap |
| `services/agent/src/live/worker.ts` | delegate worker | web subagent (`web_search`/`fetch_url`, 5 steps), narration lines |
| `services/agent/src/live/ws.ts` | /live gate | secret/token check, loopback origin rule, chat vs flow session dispatch |
| `services/agent/src/live/flow-ws.ts` (lines 685-750) | Flow ACP brain | `serveMcp` + `AgentSupervisor(AcpAgent)` with `buildFlowAcpPreamble`, `AcpBrain` |
| `services/agent/src/flow/brain.ts` | Flow brains | `LocalBrain` provider mapper, `AcpBrain` |
| `services/agent/src/flow/prompt.ts` | Flow prompt | `buildFlowPrompt`, `buildFlowAcpPreamble`, namespaced tool names |
| `services/agent/src/flow/retention.ts` | Flow context | `trimImages` keeps the 3 newest screenshots |
| `apps/web/src/lib/live/modalAnswer.ts` | voice yes/no | `classifyYesNo`, `optionForVerdict` (kind first, allow_once), `buildElicitationAnswer` |
| `apps/web/src/lib/live/useLiveSession.ts` (lines 310-336, 650-705) | client asks | speak permission, 30 s reminder, route utterances to the open modal |
| `apps/web/src/app/api/agents/route.ts` | Agents panel | installed (which/where), version, credState, commands, hidden |
| `apps/web/src/app/api/agents/action/route.ts` | Agents panel | streamed install/uninstall/update/login/logout, EACCES help, terminal fallback |
| `apps/web/src/app/api/agents/agents.ts` | Agents panel | `actionCommand`, `installDisplay`, `installHint` |

## Tools, MCP, connectors, skills, memory (`services/agent/src/capabilities`, `connectors`, `skills`, `memory`)

| path | feature | role |
|---|---|---|
| `services/agent/src/capabilities/types.ts` | tool model | `Tool`, `Session`, `ToolCtx`, `ToolResult`, `Approve`, `Emit` |
| `services/agent/src/capabilities/registry.ts` | registry | `ToolRegistry.tools(profile, session)`, builtins provider, `builtinCatalog`, machine tools selection |
| `services/agent/src/capabilities/dispatch.ts` | dispatch | `ToolSet` (loose lookup + aliases), `normalizeArgs`, `validateArgs`, `dispatch`/`dispatchAll`, on-demand unwrap, `offerOf` |
| `services/agent/src/capabilities/approval.ts` | approval | `askEach` (call), `consentApprove` (Flow one-time consent), `allowAll` |
| `services/agent/src/capabilities/mcp.ts` | loopback MCP | `mcpServer` (low-level Server, tools/list + tools/call), `serveMcp` (random port+path, Host check, `toolsChanged`) |
| `services/agent/src/capabilities/groups.ts` | tool groups | `GROUPS` table, `disabledToolGroups` setting, `groupTools` for Settings |
| `services/agent/src/capabilities/profiles.ts` | profiles | `CHAT`/`FLOW` ordering, prompt builder, approval policy |
| `services/agent/src/capabilities/on-demand.ts` | connector loading | `find_tools`/`read_tool`/`use_tool`, `AUTO_THRESHOLD` 40 tools / 8k tokens |
| `services/agent/src/capabilities/routes.ts` | /capabilities | list groups, toggle group, on-demand mode, write-only Exa key |
| `services/agent/src/capabilities/assistant.ts` | built-ins | `delegate`, `update_todos`, `remember`, `look` |
| `services/agent/src/capabilities/web.ts` | worker tools | `web_search` (Exa), `fetch_url` (SSRF guard, DNS pinning), `params` zod→JSON Schema |
| `services/agent/src/capabilities/text.ts` | built-ins | `insert_text`, `read_selection`, `clipboard_read/write`, `get_context`, `set_dictation` |
| `services/agent/src/capabilities/files.ts` | built-ins | `list_dir`, `read_file`, `write_file`, `edit_file` (workspace-fenced, checkpointed) |
| `services/agent/src/capabilities/find.ts` | built-ins | `find_files` backends (mdfind / Windows Search / fd+locate / walk) |
| `services/agent/src/capabilities/checkpoints.ts` | built-ins | `list_edits`, `undo_edit`, checkpoint journal |
| `services/agent/src/capabilities/device-tools.ts` | built-ins | ol-input tools (screenshot, click, type, windows, shell, open_url…) |
| `services/agent/src/computer/tools.ts` | built-ins | computer-use helper tools (get_app_state, click, perform_action…) |
| `services/agent/src/reminders/tools.ts` | built-ins | `set_timer`, `remind`, `list_reminders`, `cancel_reminder`, `clockNote` |
| `services/agent/src/prompt.ts` | prompts | `PERSONA`, `LIVE_RULES`, `WORKER_PROMPT`, `SHARED_MEMORY`, `rememberedNotes`, `customInstructions`, `buildLivePrompt` |
| `services/agent/src/providers.ts` | provider resolution | `resolveLive`, `resolveVision`, `liveReasoning`, provider key lookup |
| `services/agent/src/server.ts` | agent boot | Hono app, secret gate, route mounts, registry registration of connector/skill tools, mcp.json watcher, loopback bind guard |
| `services/agent/src/connectors/manager.ts` | MCP client | one client per connector, stdio/StreamableHTTP/SSE negotiation, backoff, tool list cache, elicitation routing |
| `services/agent/src/connectors/tools.ts` | connector tools | `<slug>__<tool>` naming, `toResult` caps, readOnly trust |
| `services/agent/src/connectors/import.ts` | imports | Claude Desktop / Claude Code / Codex / Cursor / Gemini / VS Code paths and parsers, dedupe preview |
| `services/agent/src/connectors/oauth.ts` | OAuth | PKCE provider, loopback redirect, CIMD / dynamic registration, per-issuer storage |
| `services/agent/src/connectors/spawn.ts` | stdio spawn | env + widened PATH for cross-spawn |
| `services/agent/src/connectors/setup.ts` | built-ins | `list_connectors`, `add_connector`, `connector_sign_in`, `reconnect_connector` |
| `services/agent/src/skills/catalog.ts` | skills | scan bundled/user/workspace folders, mtime cache, precedence |
| `services/agent/src/skills/parse.ts` | skills | SKILL.md frontmatter parsing (lenient YAML) |
| `services/agent/src/skills/tools.ts` | skills | `activate_skill`, `read_skill_file`, `save_skill`, `slashSkill` |
| `services/agent/skills/*/SKILL.md` | bundled skills | `computer-use`, `research`, `skill-creator`, `connector-setup` |
| `packages/shared/src/skills.ts` | skills wire | name rule, `SkillSource`, `SkillWire` |
| `services/agent/src/memory/notes.ts` | memory | `parseNotes`, `budgeted`, `notesInUse`, `addNote`/`editNote`/`deleteNote`/`clearNotes` under lock |
| `services/agent/src/memory/routes.ts` | /memory | list/add/edit/delete/clear, whole list back |
| `packages/shared/src/memory.ts` | memory limits | 240 chars/note, 300 notes, 2000-char prompt budget, `MemoryWire` |
| `services/agent/src/dictate/routes.ts` | /dictate | `rewrite` NDJSON stream, `warm` |
| `services/agent/src/dictate/rewrite.ts` | Dictate brain | prompts, context guard, `apiRewrite`, `agentRewrite`, warm toolless ACP agent |

## Store, harness, protocol, history (`packages/*`, `apps/web/src/app/api`)

| path | feature | role |
|---|---|---|
| `packages/shared/src/home/index.mjs` | home | `resolveHome`, `layout`, `writeAtomic`, `loadKey`/`encrypt`/`decrypt` (AES-256-GCM), `wipeHome`, `migrateHome` |
| `packages/shared/src/home/mcp.mjs` | mcp.json | read/write of the `{mcpServers}` file with `openlive` block and `${secret:}` refs (used, not read in full) |
| `packages/db/src/paths.ts` | store | `PATHS` from `layout(resolveHome())`, runs `migrateHome` at import, `skillsDir` |
| `packages/db/src/crypto.ts` | secrets | `encryptSecret`/`decryptSecret` over the lazily loaded key |
| `packages/db/src/store.ts` | JSON store | `readJson`/`writeJson`, `withFileLock` (proper-lockfile + in-process chain), `updateJson` |
| `packages/db/src/sqlite.ts` | SQLite | schema (chats, messages, meta), PRAGMAs, `scrubDeleted`, busy retry |
| `packages/db/src/queries.ts` | queries | providers (encrypted keys), chats/messages, voice profiles, settings (secret routing), memory raw access |
| `packages/db/src/connectors.ts` | connectors store | rows over mcp.json + secrets, OAuth per issuer, consent, tool cache |
| `packages/db/src/skills.ts` | skills state | `state/skills.json` disabled set |
| `packages/db/src/reminders.ts` | reminders store | `state/reminders.json` |
| `packages/db/src/migrate-conversations.ts` | migration | legacy conversations.json → SQLite |
| `packages/db/src/env.ts` | dev | `.env` loader |
| `packages/db/src/reset.ts` | dev | clear local data script |
| `packages/db/src/index.ts` | exports | package surface |
| `packages/harness/src/types.ts` | harness | `Message`, `ChatRequest`, `ProviderInfo`, `ModelInfo`, `ProviderEvent`, `Protocol` |
| `packages/harness/src/index.ts` | harness | `streamProvider` dispatch, tools-refused retry |
| `packages/harness/src/registry.ts` | providers | `BUILTIN_PROVIDERS` (15), snapshots, Ollama URL, `resolveApiMode` |
| `packages/harness/src/effort.ts` | effort | thinking budgets, OpenAI effort map, `anthropicThinkingForm`, `isReasoningModel` |
| `packages/harness/src/models.ts` | model listing | live `/models` + models.dev enrichment |
| `packages/harness/src/catalog.ts` | catalog | models.dev cache (24 h) |
| `packages/harness/src/anthropic.ts` | adapter | `/messages` with cache_control placement (grep'd) |
| `packages/harness/src/retry.ts` | adapter | pre-stream retry/backoff (grep'd) |
| `packages/shared/src/live-events.ts` | wire | `/live` client/server message unions, language codes, Flow event union |
| `packages/shared/src/sse-events.ts` | wire | SSE event union (text, reasoning, tool, acp_tool, term, todos, usage, say, error) |
| `packages/shared/src/tool-call.ts` | wire | `ToolKind`, `ToolStatus`, `ToolContent`, `ToolCallState`/delta merge |
| `packages/shared/src/types.ts` | types | `Provider`, `ChatSummary`, `HistoryChat`, `ChatMessage`, Dictate limits |
| `packages/flow-store/src/shared.ts` | flow/dictate config | `HISTORY_KEEPS`/`KEEP_MS`, PTT/toggle key rules, `defaultBrain`/`flowBrain`/`dictateBrain` |
| `packages/flow-store/src/paths.ts` | flow store | `flow/` dir, sessions, assets, lease paths |
| `packages/flow-store/src/types.ts` | flow store | session file format v1 (header, entries, states) |
| `packages/flow-store/src/history.ts` | flow history | list/search/load/delete/prune/rename sessions |
| `packages/flow-store/src/dictations.ts` | dictate history | `dictations.jsonl` append, fold, cap 1000, retention rewrite |
| `packages/flow-store/src/config.ts` | flow config | versioned `FlowConfig` (v9) with migrations (outline only) |
| `apps/web/src/app/api/history/route.ts` | history API | merge OpenLive chats with agents' own sessions, retention, clear all |
| `apps/web/src/app/api/history/agentSessions.ts` | discovery | Claude JSONL / Codex rollout / Cursor meta / OpenCode & Hermes sqlite parsers, `mergeListed`, delete external |
| `apps/web/src/app/api/history/session/route.ts` | history API | delete an agent's own session |
| `apps/web/src/app/api/settings/route.ts` | settings API | plain settings GET/PUT, settings secret for off-machine Ollama (grep'd) |

## Desktop shell (`apps/desktop`)

| path | feature | role |
|---|---|---|
| `apps/desktop/main.cjs` | Electron main | ports/tokens, home + migration, `utilityProcess` servers, port sweep/reaping, crash restart, windows (splash/main/owner/orb), permissions, tray, Flow summon, reset, quit |
| `apps/desktop/service-restart.cjs` | restart policy | backoff 500→15000 ms, reset after 60 s uptime |
| `apps/desktop/prev-exit.cjs` | pid file | classify previous exit (clean/os_restart/killed/unknown) |
| `apps/desktop/tray-menu.cjs` | tray | menu template, status lines, hotkey labels |
| `apps/desktop/telemetry/config.cjs` | telemetry | stamped config validation, `isActive` kill switches |
| `apps/desktop/package.json` | dev | `start:dev` with `--remote-debugging-port=9333` |
| `scripts/free-ports.mjs` | dev | kill stale listeners on 3000/8787/47833/47834/9333, sweep dev supervisors |
| `package.json` | scripts | `dev`, `desktop:dev` (AGENT_PORT=47833 WEB_PORT=47834), pre-sweeps |

## Dictate client (surveyed, not read line by line)

| path | feature | role |
|---|---|---|
| `apps/web/src/lib/dictate/run.ts` | dictate | `createDictate` orchestration, deadlines (POLISH_MS 25 s, COMMAND_MS 45 s), copy/secure messages |
| `apps/web/src/lib/dictate/cleanup.ts` | rules | tokenize → fillers → backtrack → lists → numbers → punctuate |
| `apps/web/src/lib/dictate/words.ts` | dictionary/snippets | user word lists and spoken commands |
| `apps/web/src/lib/dictate/spacing.ts` | typing | `needsSpace` from text before the caret |
| `apps/web/src/lib/dictate/hotkey.ts`, `history.ts`, `recent.ts`, `strip.ts`, `sessionStats.ts` | dictate | key handling, history client, recent dictations context, code-fence strip, stats |
| `apps/web/src/lib/flow/talk.ts` | talk | one open session, hold latching, Close after silence |

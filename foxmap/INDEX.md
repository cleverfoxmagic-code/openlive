# File → feature index (all 943 tracked files)

OpenLive @ 65f2420. Deep rows (`feature | role`) come from the three area reads; every other file carries its area. Graphify per-file symbols: `graphify-out/file_index.json`.

## web lib (95 files)

| path | feature | role |
|---|---|---|
| `apps/web/src/lib/agentActions.test.ts` | web lib | — |
| `apps/web/src/lib/agentActions.ts` | web lib | — |
| `apps/web/src/lib/api.ts` | web lib | — |
| `apps/web/src/lib/capabilities.test.ts` | web lib | — |
| `apps/web/src/lib/capabilities.ts` | web lib | — |
| `apps/web/src/lib/chatStore.test.ts` | web lib | — |
| `apps/web/src/lib/chatStore.ts` | web lib | — |
| `apps/web/src/lib/clearAll.test.ts` | web lib | — |
| `apps/web/src/lib/clearAll.ts` | web lib | — |
| `apps/web/src/lib/cn.ts` | web lib | — |
| `apps/web/src/lib/commandPalette.test.ts` | web lib | — |
| `apps/web/src/lib/commandPalette.ts` | web lib | — |
| `apps/web/src/lib/connectors.test.ts` | web lib | — |
| `apps/web/src/lib/connectors.ts` | web lib | — |
| `apps/web/src/lib/deferredDelete.test.ts` | web lib | — |
| `apps/web/src/lib/deferredDelete.ts` | web lib | — |
| `apps/web/src/lib/dictate/cleanup.test.ts` | web lib | — |
| `apps/web/src/lib/dictate/cleanup.ts` | rules | tokenize → fillers → backtrack → lists → numbers → punctuate |
| `apps/web/src/lib/dictate/history.test.ts` | web lib | — |
| `apps/web/src/lib/dictate/history.ts` | web lib | — |
| `apps/web/src/lib/dictate/hotkey.test.ts` | web lib | — |
| `apps/web/src/lib/dictate/hotkey.ts` | web lib | — |
| `apps/web/src/lib/dictate/recent.test.ts` | web lib | — |
| `apps/web/src/lib/dictate/recent.ts` | web lib | — |
| `apps/web/src/lib/dictate/run.test.ts` | web lib | — |
| `apps/web/src/lib/dictate/run.ts` | dictate | `createDictate` orchestration, deadlines (POLISH_MS 25 s, COMMAND_MS 45 s), copy/secure messages |
| `apps/web/src/lib/dictate/sessionStats.test.ts` | web lib | — |
| `apps/web/src/lib/dictate/sessionStats.ts` | web lib | — |
| `apps/web/src/lib/dictate/spacing.test.ts` | web lib | — |
| `apps/web/src/lib/dictate/spacing.ts` | typing | `needsSpace` from text before the caret |
| `apps/web/src/lib/dictate/strip.test.ts` | web lib | — |
| `apps/web/src/lib/dictate/strip.ts` | web lib | — |
| `apps/web/src/lib/dictate/words.test.ts` | web lib | — |
| `apps/web/src/lib/dictate/words.ts` | dictionary/snippets | user word lists and spoken commands |
| `apps/web/src/lib/disclosure.ts` | web lib | — |
| `apps/web/src/lib/featureUse.test.ts` | web lib | — |
| `apps/web/src/lib/featureUse.ts` | web lib | — |
| `apps/web/src/lib/feedbackPrompt.test.ts` | web lib | — |
| `apps/web/src/lib/feedbackPrompt.ts` | web lib | — |
| `apps/web/src/lib/gsap.ts` | web lib | — |
| `apps/web/src/lib/hints.test.ts` | web lib | — |
| `apps/web/src/lib/hints.ts` | web lib | — |
| `apps/web/src/lib/historyList.test.ts` | web lib | — |
| `apps/web/src/lib/historyList.ts` | web lib | — |
| `apps/web/src/lib/historyOverrides.ts` | web lib | — |
| `apps/web/src/lib/keepScroll.test.ts` | web lib | — |
| `apps/web/src/lib/keepScroll.ts` | web lib | — |
| `apps/web/src/lib/log.ts` | web lib | — |
| `apps/web/src/lib/look.test.ts` | web lib | — |
| `apps/web/src/lib/look.ts` | web lib | — |
| `apps/web/src/lib/memory.test.ts` | web lib | — |
| `apps/web/src/lib/memory.ts` | web lib | — |
| `apps/web/src/lib/migrateLocal.test.ts` | web lib | — |
| `apps/web/src/lib/migrateLocal.ts` | web lib | — |
| `apps/web/src/lib/modelsError.test.ts` | web lib | — |
| `apps/web/src/lib/modelsError.ts` | web lib | — |
| `apps/web/src/lib/motion.test.ts` | web lib | — |
| `apps/web/src/lib/motion.ts` | web lib | — |
| `apps/web/src/lib/persist.test.ts` | web lib | — |
| `apps/web/src/lib/persist.ts` | web lib | — |
| `apps/web/src/lib/platform.ts` | web lib | — |
| `apps/web/src/lib/prefs.test.ts` | web lib | — |
| `apps/web/src/lib/prefs.ts` | web lib | — |
| `apps/web/src/lib/privacyNotice.test.ts` | web lib | — |
| `apps/web/src/lib/privacyNotice.ts` | web lib | — |
| `apps/web/src/lib/rendererError.test.ts` | web lib | — |
| `apps/web/src/lib/rendererError.ts` | web lib | — |
| `apps/web/src/lib/repo.test.ts` | web lib | — |
| `apps/web/src/lib/repo.ts` | web lib | — |
| `apps/web/src/lib/reportProblem.test.ts` | web lib | — |
| `apps/web/src/lib/reportProblem.ts` | web lib | — |
| `apps/web/src/lib/settingChanges.test.ts` | web lib | — |
| `apps/web/src/lib/settingChanges.ts` | web lib | — |
| `apps/web/src/lib/settingsSearch.test.ts` | web lib | — |
| `apps/web/src/lib/settingsSearch.ts` | web lib | — |
| `apps/web/src/lib/skills.test.ts` | web lib | — |
| `apps/web/src/lib/skills.ts` | web lib | — |
| `apps/web/src/lib/telemetry.test.ts` | web lib | — |
| `apps/web/src/lib/telemetry.ts` | web lib | — |
| `apps/web/src/lib/telemetryIds.ts` | web lib | — |
| `apps/web/src/lib/toast.ts` | web lib | — |
| `apps/web/src/lib/truncated.test.ts` | web lib | — |
| `apps/web/src/lib/truncated.ts` | web lib | — |
| `apps/web/src/lib/uiStore.ts` | web lib | — |
| `apps/web/src/lib/useAppVersion.ts` | web lib | — |
| `apps/web/src/lib/useBrainId.ts` | web lib | — |
| `apps/web/src/lib/useFocusTrap.ts` | web lib | — |
| `apps/web/src/lib/useHydrated.ts` | web lib | — |
| `apps/web/src/lib/useMenuKeys.ts` | web lib | — |
| `apps/web/src/lib/usePointerDrag.ts` | web lib | — |
| `apps/web/src/lib/usePopIn.ts` | web lib | — |
| `apps/web/src/lib/waveOrb.test.ts` | web lib | — |
| `apps/web/src/lib/waveOrb.ts` | web lib | — |
| `apps/web/src/lib/windowShown.test.ts` | web lib | — |
| `apps/web/src/lib/windowShown.ts` | web lib | — |

## UI components (94 files)

| path | feature | role |
|---|---|---|
| `apps/web/src/components/CommandPalette.tsx` | UI components | — |
| `apps/web/src/components/ConnectionBanner.tsx` | UI components | — |
| `apps/web/src/components/FeedbackPrompt.tsx` | UI components | — |
| `apps/web/src/components/HistorySidebar.tsx` | UI components | — |
| `apps/web/src/components/OpenLiveMark.tsx` | UI components | — |
| `apps/web/src/components/OpenLiveOrb.tsx` | UI components | — |
| `apps/web/src/components/PrivacyNotice.tsx` | UI components | — |
| `apps/web/src/components/ShortcutsSheet.tsx` | UI components | — |
| `apps/web/src/components/SkipSetup.tsx` | UI components | — |
| `apps/web/src/components/SpotlightTour.tsx` | UI components | — |
| `apps/web/src/components/Toasts.tsx` | UI components | — |
| `apps/web/src/components/Welcome.tsx` | UI components | — |
| `apps/web/src/components/WindowControls.tsx` | UI components | — |
| `apps/web/src/components/dictate/DictateHome.tsx` | UI components | — |
| `apps/web/src/components/live/AgentBar.tsx` | UI components | — |
| `apps/web/src/components/live/AgentControls.tsx` | UI components | — |
| `apps/web/src/components/live/AgentIcon.tsx` | UI components | — |
| `apps/web/src/components/live/AskLine.tsx` | UI components | — |
| `apps/web/src/components/live/CameraPiP.tsx` | UI components | — |
| `apps/web/src/components/live/ChatStatus.tsx` | UI components | — |
| `apps/web/src/components/live/Composer.tsx` | UI components | — |
| `apps/web/src/components/live/DiffView.tsx` | UI components | — |
| `apps/web/src/components/live/DownloadOffer.tsx` | UI components | — |
| `apps/web/src/components/live/ElicitationPrompt.tsx` | UI components | — |
| `apps/web/src/components/live/EndCallButton.tsx` | UI components | — |
| `apps/web/src/components/live/HintChips.tsx` | UI components | — |
| `apps/web/src/components/live/HoldToSend.tsx` | UI components | — |
| `apps/web/src/components/live/InCall.tsx` | UI components | — |
| `apps/web/src/components/live/LiveDock.tsx` | UI components | — |
| `apps/web/src/components/live/LiveStage.tsx` | UI components | — |
| `apps/web/src/components/live/Lobby.tsx` | UI components | — |
| `apps/web/src/components/live/ModalVoiceInput.tsx` | UI components | — |
| `apps/web/src/components/live/ModelQuickPick.tsx` | UI components | — |
| `apps/web/src/components/live/Orb.tsx` | UI components | — |
| `apps/web/src/components/live/ScreenTile.tsx` | UI components | — |
| `apps/web/src/components/live/SetupControls.tsx` | UI components | — |
| `apps/web/src/components/live/TerminalView.tsx` | UI components | — |
| `apps/web/src/components/live/ToolCallCard.tsx` | UI components | — |
| `apps/web/src/components/live/ToolGlyph.tsx` | UI components | — |
| `apps/web/src/components/live/TopBar.tsx` | UI components | — |
| `apps/web/src/components/live/TranscriptPanel.tsx` | UI components | — |
| `apps/web/src/components/settings/AboutSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/AgentsSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/AudioBar.tsx` | UI components | — |
| `apps/web/src/components/settings/CapabilitiesSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/ChatSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/ConnectorsSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/DictateHistory.tsx` | UI components | — |
| `apps/web/src/components/settings/DictateSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/DictateWords.tsx` | UI components | — |
| `apps/web/src/components/settings/GeneralSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/HistorySection.tsx` | UI components | — |
| `apps/web/src/components/settings/HowYouTalk.tsx` | UI components | — |
| `apps/web/src/components/settings/MemorySettings.tsx` | UI components | — |
| `apps/web/src/components/settings/ModelsSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/PipelineSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/PrivacySettings.tsx` | UI components | — |
| `apps/web/src/components/settings/PronunciationSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/ProviderKeyField.tsx` | UI components | — |
| `apps/web/src/components/settings/Section.tsx` | UI components | — |
| `apps/web/src/components/settings/SettingsPage.tsx` | UI components | — |
| `apps/web/src/components/settings/SharedSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/SkillsSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/SurfaceSpeech.tsx` | UI components | — |
| `apps/web/src/components/settings/ToolsSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/VoiceSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/VoicesSettings.tsx` | UI components | — |
| `apps/web/src/components/settings/WhoAnswers.tsx` | UI components | — |
| `apps/web/src/components/settings/common.tsx` | UI components | — |
| `apps/web/src/components/settings/nav.tsx` | UI components | — |
| `apps/web/src/components/ui/Advanced.tsx` | UI components | — |
| `apps/web/src/components/ui/Button.tsx` | UI components | — |
| `apps/web/src/components/ui/Checkbox.tsx` | UI components | — |
| `apps/web/src/components/ui/Chip.tsx` | UI components | — |
| `apps/web/src/components/ui/ConfirmButton.tsx` | UI components | — |
| `apps/web/src/components/ui/Disclosure.tsx` | UI components | — |
| `apps/web/src/components/ui/InfoTip.tsx` | UI components | — |
| `apps/web/src/components/ui/Input.tsx` | UI components | — |
| `apps/web/src/components/ui/Keycap.tsx` | UI components | — |
| `apps/web/src/components/ui/ListRow.tsx` | UI components | — |
| `apps/web/src/components/ui/Menu.tsx` | UI components | — |
| `apps/web/src/components/ui/Notice.tsx` | UI components | — |
| `apps/web/src/components/ui/Radio.tsx` | UI components | — |
| `apps/web/src/components/ui/SearchSelect.tsx` | UI components | — |
| `apps/web/src/components/ui/Segmented.tsx` | UI components | — |
| `apps/web/src/components/ui/Select.tsx` | UI components | — |
| `apps/web/src/components/ui/SidePanel.tsx` | UI components | — |
| `apps/web/src/components/ui/Slider.tsx` | UI components | — |
| `apps/web/src/components/ui/Swap.tsx` | UI components | — |
| `apps/web/src/components/ui/Switch.tsx` | UI components | — |
| `apps/web/src/components/ui/Tooltip.tsx` | UI components | — |
| `apps/web/src/components/ui/focus.test.ts` | UI components | — |
| `apps/web/src/components/ui/focus.ts` | UI components | — |
| `apps/web/src/components/ui/index.ts` | UI components | — |

## desktop shell (80 files)

| path | feature | role |
|---|---|---|
| `apps/desktop/README.md` | desktop shell | — |
| `apps/desktop/build/entitlements.mac.plist` | desktop shell | — |
| `apps/desktop/build/icon.ico` | desktop shell | — |
| `apps/desktop/build/icon.png` | desktop shell | — |
| `apps/desktop/build/icons/1024x1024.png` | desktop shell | — |
| `apps/desktop/build/icons/128x128.png` | desktop shell | — |
| `apps/desktop/build/icons/16x16.png` | desktop shell | — |
| `apps/desktop/build/icons/20x20.png` | desktop shell | — |
| `apps/desktop/build/icons/24x24.png` | desktop shell | — |
| `apps/desktop/build/icons/256x256.png` | desktop shell | — |
| `apps/desktop/build/icons/32x32.png` | desktop shell | — |
| `apps/desktop/build/icons/40x40.png` | desktop shell | — |
| `apps/desktop/build/icons/48x48.png` | desktop shell | — |
| `apps/desktop/build/icons/512x512.png` | desktop shell | — |
| `apps/desktop/build/icons/64x64.png` | desktop shell | — |
| `apps/desktop/build/tray.png` | desktop shell | — |
| `apps/desktop/build/tray@2x.png` | desktop shell | — |
| `apps/desktop/build/trayTemplate.png` | desktop shell | — |
| `apps/desktop/build/trayTemplate@2x.png` | desktop shell | — |
| `apps/desktop/electron-builder.yml` | desktop shell | — |
| `apps/desktop/external-url.cjs` | desktop shell | — |
| `apps/desktop/external-url.test.ts` | desktop shell | — |
| `apps/desktop/flow-cursor-preload.cjs` | desktop shell | — |
| `apps/desktop/flow-cursor.cjs` | desktop shell | — |
| `apps/desktop/flow-cursor.html` | desktop shell | — |
| `apps/desktop/flow-input.cjs` | desktop shell | — |
| `apps/desktop/flow-input.test.ts` | desktop shell | — |
| `apps/desktop/flow-runtime.cjs` | desktop shell | — |
| `apps/desktop/gpu-flags.cjs` | desktop shell | — |
| `apps/desktop/gpu-flags.test.ts` | desktop shell | — |
| `apps/desktop/license-texts/client-only/MIT.txt` | desktop shell | — |
| `apps/desktop/license-texts/csukuangfj__sherpa-onnx/Apache-2.0.txt` | desktop shell | — |
| `apps/desktop/license-texts/doumanash__clipboard-win/BSL-1.0.txt` | desktop shell | — |
| `apps/desktop/license-texts/madsmtm__objc2/Apache-2.0.txt` | desktop shell | — |
| `apps/desktop/license-texts/madsmtm__objc2/MIT.txt` | desktop shell | — |
| `apps/desktop/license-texts/madsmtm__objc2/Zlib.txt` | desktop shell | — |
| `apps/desktop/license-texts/microsoft__onnxruntime/MIT.txt` | desktop shell | — |
| `apps/desktop/license-texts/napi-rs__napi-rs/MIT.txt` | desktop shell | — |
| `apps/desktop/license-texts/nicolasdeveloper__guid-typescript/ISC.txt` | desktop shell | — |
| `apps/desktop/license-texts/ricky0123__vad/ISC.txt` | desktop shell | — |
| `apps/desktop/license-texts/vercel__next.js/MIT.txt` | desktop shell | — |
| `apps/desktop/linux-input.cjs` | desktop shell | — |
| `apps/desktop/linux-input.test.ts` | desktop shell | — |
| `apps/desktop/login-item.cjs` | desktop shell | — |
| `apps/desktop/login-item.test.ts` | desktop shell | — |
| `apps/desktop/look.cjs` | desktop shell | — |
| `apps/desktop/look.test.ts` | desktop shell | — |
| `apps/desktop/main.cjs` | Electron main | ports/tokens, home + migration, `utilityProcess` servers, port sweep/reaping, crash restart, windows (splash/main/owner/orb), permissions, tray, Flow summon, reset, quit |
| `apps/desktop/orb-pointer.cjs` | desktop shell | — |
| `apps/desktop/orb-pointer.test.ts` | desktop shell | — |
| `apps/desktop/orb-show.cjs` | desktop shell | — |
| `apps/desktop/orb-show.test.ts` | desktop shell | — |
| `apps/desktop/package.json` | dev | `start:dev` with `--remote-debugging-port=9333` |
| `apps/desktop/packaging.test.ts` | desktop shell | — |
| `apps/desktop/preload.cjs` | desktop shell | — |
| `apps/desktop/preload.test.ts` | desktop shell | — |
| `apps/desktop/prev-exit.cjs` | pid file | classify previous exit (clean/os_restart/killed/unknown) |
| `apps/desktop/prev-exit.test.ts` | desktop shell | — |
| `apps/desktop/scripts/check-native.cjs` | desktop shell | — |
| `apps/desktop/scripts/gen-telemetry-schema.cjs` | desktop shell | — |
| `apps/desktop/scripts/pack-agent.cjs` | desktop shell | — |
| `apps/desktop/scripts/pack-licenses.cjs` | desktop shell | — |
| `apps/desktop/scripts/pack-native.cjs` | desktop shell | — |
| `apps/desktop/scripts/pack-release-marker.cjs` | desktop shell | — |
| `apps/desktop/scripts/pack-telemetry.cjs` | desktop shell | — |
| `apps/desktop/scripts/pack-web.cjs` | desktop shell | — |
| `apps/desktop/scripts/smoke-servers.cjs` | desktop shell | — |
| `apps/desktop/service-restart.cjs` | restart policy | backoff 500→15000 ms, reset after 60 s uptime |
| `apps/desktop/service-restart.test.ts` | desktop shell | — |
| `apps/desktop/splash.html` | desktop shell | — |
| `apps/desktop/talk.cjs` | desktop shell | — |
| `apps/desktop/talk.test.ts` | desktop shell | — |
| `apps/desktop/telemetry-map.cjs` | desktop shell | — |
| `apps/desktop/telemetry-map.test.ts` | desktop shell | — |
| `apps/desktop/tray-menu.cjs` | tray | menu template, status lines, hotkey labels |
| `apps/desktop/tray-menu.test.ts` | desktop shell | — |
| `apps/desktop/update-gate.cjs` | desktop shell | — |
| `apps/desktop/update-gate.test.ts` | desktop shell | — |
| `apps/desktop/window-state.cjs` | desktop shell | — |
| `apps/desktop/window-state.test.ts` | desktop shell | — |

## voice loop (74 files)

| path | feature | role |
|---|---|---|
| `apps/web/src/lib/live/addressee.ts` | voice loop | — |
| `apps/web/src/lib/live/asrStream.ts` | voice loop | — |
| `apps/web/src/lib/live/audioPlayback.test.ts` | voice loop | — |
| `apps/web/src/lib/live/audioPlayback.ts` | voice loop | — |
| `apps/web/src/lib/live/callFact.test.ts` | voice loop | — |
| `apps/web/src/lib/live/callFact.ts` | voice loop | — |
| `apps/web/src/lib/live/cameraCapture.ts` | voice loop | — |
| `apps/web/src/lib/live/chatReadiness.ts` | voice loop | — |
| `apps/web/src/lib/live/composer.test.ts` | voice loop | — |
| `apps/web/src/lib/live/composer.ts` | voice loop | — |
| `apps/web/src/lib/live/devices.test.ts` | voice loop | — |
| `apps/web/src/lib/live/devices.ts` | voice loop | — |
| `apps/web/src/lib/live/engineMenu.test.ts` | voice loop | — |
| `apps/web/src/lib/live/engineMenu.ts` | voice loop | — |
| `apps/web/src/lib/live/fixtures/ok.wav` | voice loop | — |
| `apps/web/src/lib/live/fixtures/thanks.wav` | voice loop | — |
| `apps/web/src/lib/live/fixtures/yes.wav` | voice loop | — |
| `apps/web/src/lib/live/holdCue.test.ts` | voice loop | — |
| `apps/web/src/lib/live/holdCue.ts` | voice loop | — |
| `apps/web/src/lib/live/holdLive.test.ts` | voice loop | — |
| `apps/web/src/lib/live/holdLive.ts` | voice loop | — |
| `apps/web/src/lib/live/howItRuns.test.ts` | voice loop | — |
| `apps/web/src/lib/live/howItRuns.ts` | voice loop | — |
| `apps/web/src/lib/live/keyTargets.test.ts` | voice loop | — |
| `apps/web/src/lib/live/keyTargets.ts` | voice loop | — |
| `apps/web/src/lib/live/linkStatus.test.ts` | voice loop | — |
| `apps/web/src/lib/live/linkStatus.ts` | voice loop | — |
| `apps/web/src/lib/live/liveClient.test.ts` | voice loop | — |
| `apps/web/src/lib/live/liveClient.ts` | voice loop | — |
| `apps/web/src/lib/live/liveStore.test.ts` | voice loop | — |
| `apps/web/src/lib/live/liveStore.ts` | voice loop | — |
| `apps/web/src/lib/live/lobbyGap.test.ts` | voice loop | — |
| `apps/web/src/lib/live/lobbyGap.ts` | voice loop | — |
| `apps/web/src/lib/live/micCopy.ts` | voice loop | — |
| `apps/web/src/lib/live/modalAnswer.test.ts` | voice loop | — |
| `apps/web/src/lib/live/modalAnswer.ts` | voice yes/no | `classifyYesNo`, `optionForVerdict` (kind first, allow_once), `buildElicitationAnswer` |
| `apps/web/src/lib/live/models.test.ts` | voice loop | — |
| `apps/web/src/lib/live/models.ts` | voice loop | — |
| `apps/web/src/lib/live/models.worker.test.ts` | voice loop | — |
| `apps/web/src/lib/live/models.worker.ts` | voice loop | — |
| `apps/web/src/lib/live/nativeFailure.test.ts` | voice loop | — |
| `apps/web/src/lib/live/nativeFailure.ts` | voice loop | — |
| `apps/web/src/lib/live/panelBridge.ts` | voice loop | — |
| `apps/web/src/lib/live/pcm.test.ts` | voice loop | — |
| `apps/web/src/lib/live/pcm.ts` | voice loop | — |
| `apps/web/src/lib/live/perf.test.ts` | voice loop | — |
| `apps/web/src/lib/live/perf.ts` | voice loop | — |
| `apps/web/src/lib/live/pipelineConfig.test.ts` | voice loop | — |
| `apps/web/src/lib/live/pipelineConfig.ts` | voice loop | — |
| `apps/web/src/lib/live/spectrum.ts` | voice loop | — |
| `apps/web/src/lib/live/speechFacts.ts` | voice loop | — |
| `apps/web/src/lib/live/supertonic.ts` | voice loop | — |
| `apps/web/src/lib/live/tapeSpeech.test.ts` | voice loop | — |
| `apps/web/src/lib/live/tapeSpeech.ts` | voice loop | — |
| `apps/web/src/lib/live/timeline.test.ts` | voice loop | — |
| `apps/web/src/lib/live/timeline.ts` | voice loop | — |
| `apps/web/src/lib/live/toolMeta.test.ts` | voice loop | — |
| `apps/web/src/lib/live/toolMeta.ts` | voice loop | — |
| `apps/web/src/lib/live/ttsCapture.test.ts` | voice loop | — |
| `apps/web/src/lib/live/ttsCapture.ts` | voice loop | — |
| `apps/web/src/lib/live/turn.worker.ts` | voice loop | — |
| `apps/web/src/lib/live/useApiModeChoice.ts` | voice loop | — |
| `apps/web/src/lib/live/useLiveSession.ts` | client asks | speak permission, 30 s reminder, route utterances to the open modal |
| `apps/web/src/lib/live/usePtt.test.ts` | voice loop | — |
| `apps/web/src/lib/live/usePtt.ts` | voice loop | — |
| `apps/web/src/lib/live/voiceEngine.test.ts` | voice loop | — |
| `apps/web/src/lib/live/voiceEngine.ts` | voice loop | — |
| `apps/web/src/lib/live/voiceText.test.ts` | voice loop | — |
| `apps/web/src/lib/live/voiceText.ts` | voice loop | — |
| `apps/web/src/lib/live/voiceprint.test.ts` | voice loop | — |
| `apps/web/src/lib/live/voiceprint.ts` | voice loop | — |
| `apps/web/src/lib/live/warmup.ts` | voice loop | — |
| `apps/web/src/lib/live/weights.test.ts` | voice loop | — |
| `apps/web/src/lib/live/weights.ts` | voice loop | — |

## agent service (72 files)

| path | feature | role |
|---|---|---|
| `services/agent/package.json` | agent service | — |
| `services/agent/scripts/persist.selfcheck.mjs` | agent service | — |
| `services/agent/skills/computer-use/SKILL.md` | agent service | — |
| `services/agent/skills/connector-setup/SKILL.md` | agent service | — |
| `services/agent/skills/research/SKILL.md` | agent service | — |
| `services/agent/skills/skill-creator/SKILL.md` | agent service | — |
| `services/agent/src/block-emit.test.ts` | agent service | — |
| `services/agent/src/block-emit.ts` | agent service | — |
| `services/agent/src/connectors/connectors.test.ts` | agent service | — |
| `services/agent/src/connectors/fixture-server.fixture.mjs` | agent service | — |
| `services/agent/src/connectors/fixtures/claude.json` | agent service | — |
| `services/agent/src/connectors/fixtures/claude_desktop_config.json` | agent service | — |
| `services/agent/src/connectors/fixtures/codex-config.toml` | agent service | — |
| `services/agent/src/connectors/fixtures/cursor-mcp.json` | agent service | — |
| `services/agent/src/connectors/fixtures/gemini-settings.json` | agent service | — |
| `services/agent/src/connectors/fixtures/vscode-mcp.json` | agent service | — |
| `services/agent/src/connectors/import.test.ts` | agent service | — |
| `services/agent/src/connectors/import.ts` | imports | Claude Desktop / Claude Code / Codex / Cursor / Gemini / VS Code paths and parsers, dedupe preview |
| `services/agent/src/connectors/manager.ts` | MCP client | one client per connector, stdio/StreamableHTTP/SSE negotiation, backoff, tool list cache, elicitation routing |
| `services/agent/src/connectors/oauth.test.ts` | agent service | — |
| `services/agent/src/connectors/oauth.ts` | OAuth | PKCE provider, loopback redirect, CIMD / dynamic registration, per-issuer storage |
| `services/agent/src/connectors/routes.test.ts` | agent service | — |
| `services/agent/src/connectors/routes.ts` | agent service | — |
| `services/agent/src/connectors/setup.test.ts` | agent service | — |
| `services/agent/src/connectors/setup.ts` | built-ins | `list_connectors`, `add_connector`, `connector_sign_in`, `reconnect_connector` |
| `services/agent/src/connectors/spawn.test.ts` | agent service | — |
| `services/agent/src/connectors/spawn.ts` | stdio spawn | env + widened PATH for cross-spawn |
| `services/agent/src/connectors/tools.test.ts` | agent service | — |
| `services/agent/src/connectors/tools.ts` | connector tools | `<slug>__<tool>` naming, `toResult` caps, readOnly trust |
| `services/agent/src/dictate/rewrite.test.ts` | agent service | — |
| `services/agent/src/dictate/rewrite.ts` | Dictate brain | prompts, context guard, `apiRewrite`, `agentRewrite`, warm toolless ACP agent |
| `services/agent/src/dictate/routes.test.ts` | agent service | — |
| `services/agent/src/dictate/routes.ts` | /dictate | `rewrite` NDJSON stream, `warm` |
| `services/agent/src/exa.ts` | agent service | — |
| `services/agent/src/log.test.ts` | agent service | — |
| `services/agent/src/log.ts` | agent service | — |
| `services/agent/src/memory/notes.test.ts` | agent service | — |
| `services/agent/src/memory/notes.ts` | memory | `parseNotes`, `budgeted`, `notesInUse`, `addNote`/`editNote`/`deleteNote`/`clearNotes` under lock |
| `services/agent/src/memory/routes.test.ts` | agent service | — |
| `services/agent/src/memory/routes.ts` | /memory | list/add/edit/delete/clear, whole list back |
| `services/agent/src/prompt.ts` | prompts | `PERSONA`, `LIVE_RULES`, `WORKER_PROMPT`, `SHARED_MEMORY`, `rememberedNotes`, `customInstructions`, `buildLivePrompt` |
| `services/agent/src/providers.test.ts` | agent service | — |
| `services/agent/src/providers.ts` | provider resolution | `resolveLive`, `resolveVision`, `liveReasoning`, provider key lookup |
| `services/agent/src/reminders/fire.ts` | agent service | — |
| `services/agent/src/reminders/routes.ts` | agent service | — |
| `services/agent/src/reminders/scheduler.test.ts` | agent service | — |
| `services/agent/src/reminders/scheduler.ts` | agent service | — |
| `services/agent/src/reminders/time.test.ts` | agent service | — |
| `services/agent/src/reminders/time.ts` | agent service | — |
| `services/agent/src/reminders/tools.test.ts` | agent service | — |
| `services/agent/src/reminders/tools.ts` | built-ins | `set_timer`, `remind`, `list_reminders`, `cancel_reminder`, `clockNote` |
| `services/agent/src/server.ts` | agent boot | Hono app, secret gate, route mounts, registry registration of connector/skill tools, mcp.json watcher, loopback bind guard |
| `services/agent/src/skills/bundled.test.ts` | agent service | — |
| `services/agent/src/skills/catalog.ts` | skills | scan bundled/user/workspace folders, mtime cache, precedence |
| `services/agent/src/skills/content.ts` | agent service | — |
| `services/agent/src/skills/import.ts` | agent service | — |
| `services/agent/src/skills/parse.ts` | skills | SKILL.md frontmatter parsing (lenient YAML) |
| `services/agent/src/skills/routes.test.ts` | agent service | — |
| `services/agent/src/skills/routes.ts` | agent service | — |
| `services/agent/src/skills/skills.test.ts` | agent service | — |
| `services/agent/src/skills/tools.ts` | skills | `activate_skill`, `read_skill_file`, `save_skill`, `slashSkill` |
| `services/agent/src/telemetry/emit.test.ts` | agent service | — |
| `services/agent/src/telemetry/emit.ts` | agent service | — |
| `services/agent/src/telemetry/facts.test.ts` | agent service | — |
| `services/agent/src/telemetry/facts.ts` | agent service | — |
| `services/agent/src/telemetry/limits.ts` | agent service | — |
| `services/agent/src/telemetry/payloads.test.ts` | agent service | — |
| `services/agent/src/telemetry/voice.ts` | agent service | — |
| `services/agent/src/tool-images.test.ts` | agent service | — |
| `services/agent/src/tool-images.ts` | agent service | — |
| `services/agent/src/turn.ts` | agent service | — |
| `services/agent/tsconfig.json` | agent service | — |

## computer-use helper (56 files)

| path | feature | role |
|---|---|---|
| `native/openlive-cu/.gitignore` | computer-use helper | — |
| `native/openlive-cu/Cargo.lock` | computer-use helper | — |
| `native/openlive-cu/Cargo.toml` | computer-use helper | — |
| `native/openlive-cu/crates/core/Cargo.toml` | computer-use helper | — |
| `native/openlive-cu/crates/core/src/auth.rs` | computer-use helper | — |
| `native/openlive-cu/crates/core/src/backend.rs` | computer-use helper | — |
| `native/openlive-cu/crates/core/src/framing.rs` | computer-use helper | — |
| `native/openlive-cu/crates/core/src/geometry.rs` | computer-use helper | — |
| `native/openlive-cu/crates/core/src/image.rs` | computer-use helper | — |
| `native/openlive-cu/crates/core/src/keys.rs` | computer-use helper | — |
| `native/openlive-cu/crates/core/src/lib.rs` | computer-use helper | — |
| `native/openlive-cu/crates/core/src/protocol.rs` | computer-use helper | — |
| `native/openlive-cu/crates/core/src/serve.rs` | computer-use helper | — |
| `native/openlive-cu/crates/core/src/tree.rs` | computer-use helper | — |
| `native/openlive-cu/crates/helper/Cargo.toml` | computer-use helper | — |
| `native/openlive-cu/crates/helper/build.rs` | computer-use helper | — |
| `native/openlive-cu/crates/helper/openlive-cu.exe.manifest` | computer-use helper | — |
| `native/openlive-cu/crates/helper/src/disclaim.rs` | computer-use helper | — |
| `native/openlive-cu/crates/helper/src/main.rs` | computer-use helper | — |
| `native/openlive-cu/crates/helper/tests/smoke.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/Cargo.toml` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/atspi.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/backend.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/bus.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/clipboard.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/codes.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/desktop.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/ewmh.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/geom.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/lib.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/pipewire.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/portal.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/roles.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/spa.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/wayland.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-linux/src/x11.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-macos/Cargo.toml` | computer-use helper | — |
| `native/openlive-cu/crates/platform-macos/src/ax.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-macos/src/capture.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-macos/src/cg.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-macos/src/input.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-macos/src/lib.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-windows/Cargo.toml` | computer-use helper | — |
| `native/openlive-cu/crates/platform-windows/src/backend.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-windows/src/capture.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-windows/src/codes.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-windows/src/input.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-windows/src/lib.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-windows/src/pipe.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-windows/src/roles.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-windows/src/shot.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-windows/src/uia.rs` | computer-use helper | — |
| `native/openlive-cu/crates/platform-windows/src/win.rs` | computer-use helper | — |
| `native/openlive-cu/entitlements.mac.plist` | computer-use helper | — |
| `native/openlive-cu/package.json` | computer-use helper | — |
| `native/openlive-cu/scripts/build.cjs` | computer-use helper | — |

## native input addon (37 files)

| path | feature | role |
|---|---|---|
| `native/ol-input/.gitignore` | native input addon | — |
| `native/ol-input/Cargo.lock` | native input addon | — |
| `native/ol-input/Cargo.toml` | native input addon | — |
| `native/ol-input/build.rs` | native input addon | — |
| `native/ol-input/index.d.ts` | native input addon | — |
| `native/ol-input/index.js` | native input addon | — |
| `native/ol-input/package.json` | native input addon | — |
| `native/ol-input/scripts/build.cjs` | native input addon | — |
| `native/ol-input/scripts/stale.cjs` | native input addon | — |
| `native/ol-input/scripts/stale.test.ts` | native input addon | — |
| `native/ol-input/src/binding.rs` | native input addon | — |
| `native/ol-input/src/capabilities.rs` | native input addon | — |
| `native/ol-input/src/capture.rs` | native input addon | — |
| `native/ol-input/src/clipboard.rs` | native input addon | — |
| `native/ol-input/src/control.rs` | native input addon | — |
| `native/ol-input/src/coordinator.rs` | native input addon | — |
| `native/ol-input/src/coords.rs` | native input addon | — |
| `native/ol-input/src/focus.rs` | native input addon | — |
| `native/ol-input/src/hook.rs` | native input addon | — |
| `native/ol-input/src/inject.rs` | native input addon | — |
| `native/ol-input/src/lib.rs` | native input addon | — |
| `native/ol-input/src/motion.rs` | native input addon | — |
| `native/ol-input/src/ocr.rs` | native input addon | — |
| `native/ol-input/src/paste_tx/macos.rs` | native input addon | — |
| `native/ol-input/src/paste_tx/mod.rs` | native input addon | — |
| `native/ol-input/src/paste_tx/windows.rs` | native input addon | — |
| `native/ol-input/src/perms.rs` | native input addon | — |
| `native/ol-input/src/platform/desktop/linux.rs` | native input addon | — |
| `native/ol-input/src/platform/desktop/macos.rs` | native input addon | — |
| `native/ol-input/src/platform/desktop/mod.rs` | native input addon | — |
| `native/ol-input/src/platform/desktop/windows.rs` | native input addon | — |
| `native/ol-input/src/platform/linux.rs` | native input addon | — |
| `native/ol-input/src/platform/macos.rs` | native input addon | — |
| `native/ol-input/src/platform/mod.rs` | native input addon | — |
| `native/ol-input/src/platform/windows.rs` | native input addon | — |
| `native/ol-input/src/secure_input.rs` | native input addon | — |
| `native/ol-input/src/window.rs` | native input addon | — |

## shared protocol/registry (37 files)

| path | feature | role |
|---|---|---|
| `packages/shared/package.json` | shared protocol/registry | — |
| `packages/shared/src/agent-models.test.ts` | shared protocol/registry | — |
| `packages/shared/src/agent-models.ts` | shared protocol/registry | — |
| `packages/shared/src/agent-registry.test.ts` | shared protocol/registry | — |
| `packages/shared/src/agent-registry.ts` | registry | `AGENT_REGISTRY`: 9 agents, adapter commands (pinned npx), bins, install/login, credProbe, sessionsDir/parser, ACP quirks (preamble, mcp, terminal, env, toolless) |
| `packages/shared/src/agent-start.test.ts` | shared protocol/registry | — |
| `packages/shared/src/agent-start.ts` | start failures | `startReason` from stderr/exit code; `startMessage` wording; `AgentStartError` |
| `packages/shared/src/capabilities.ts` | shared protocol/registry | — |
| `packages/shared/src/connectors.ts` | shared protocol/registry | — |
| `packages/shared/src/edits.ts` | shared protocol/registry | — |
| `packages/shared/src/error-class.test.ts` | shared protocol/registry | — |
| `packages/shared/src/error-class.ts` | shared protocol/registry | — |
| `packages/shared/src/home/home.test.ts` | shared protocol/registry | — |
| `packages/shared/src/home/index.d.mts` | shared protocol/registry | — |
| `packages/shared/src/home/index.mjs` | home | `resolveHome`, `layout`, `writeAtomic`, `loadKey`/`encrypt`/`decrypt` (AES-256-GCM), `wipeHome`, `migrateHome` |
| `packages/shared/src/home/mcp.d.mts` | shared protocol/registry | — |
| `packages/shared/src/home/mcp.mjs` | mcp.json | read/write of the `{mcpServers}` file with `openlive` block and `${secret:}` refs (used, not read in full) |
| `packages/shared/src/index.ts` | shared protocol/registry | — |
| `packages/shared/src/live-events.ts` | wire | `/live` client/server message unions, language codes, Flow event union |
| `packages/shared/src/live-models.ts` | shared protocol/registry | — |
| `packages/shared/src/memory.ts` | memory limits | 240 chars/note, 300 notes, 2000-char prompt budget, `MemoryWire` |
| `packages/shared/src/node/agent-node.test.ts` | shared protocol/registry | — |
| `packages/shared/src/node/agent-node.ts` | node helpers | `widenedPath`, `commandOnPath`, `evalCredProbe` (file/json/fileMatch/keychain/anyOf), `terminalCommand` |
| `packages/shared/src/reminders.ts` | shared protocol/registry | — |
| `packages/shared/src/skills.ts` | skills wire | name rule, `SkillSource`, `SkillWire` |
| `packages/shared/src/sse-events.ts` | wire | SSE event union (text, reasoning, tool, acp_tool, term, todos, usage, say, error) |
| `packages/shared/src/telemetry-docs.test.ts` | shared protocol/registry | — |
| `packages/shared/src/telemetry-ids.test.ts` | shared protocol/registry | — |
| `packages/shared/src/telemetry-schema.test.ts` | shared protocol/registry | — |
| `packages/shared/src/telemetry-schema.ts` | shared protocol/registry | — |
| `packages/shared/src/telemetry.ts` | shared protocol/registry | — |
| `packages/shared/src/tool-call.test.ts` | shared protocol/registry | — |
| `packages/shared/src/tool-call.ts` | wire | `ToolKind`, `ToolStatus`, `ToolContent`, `ToolCallState`/delta merge |
| `packages/shared/src/tool-summary.test.ts` | shared protocol/registry | — |
| `packages/shared/src/tool-summary.ts` | shared protocol/registry | — |
| `packages/shared/src/types.ts` | types | `Provider`, `ChatSummary`, `HistoryChat`, `ChatMessage`, Dictate limits |
| `packages/shared/tsconfig.json` | shared protocol/registry | — |

## web API routes (32 files)

| path | feature | role |
|---|---|---|
| `apps/web/src/app/api/agents/action/route.ts` | Agents panel | streamed install/uninstall/update/login/logout, EACCES help, terminal fallback |
| `apps/web/src/app/api/agents/agents.test.ts` | web API routes | — |
| `apps/web/src/app/api/agents/agents.ts` | Agents panel | `actionCommand`, `installDisplay`, `installHint` |
| `apps/web/src/app/api/agents/route.ts` | Agents panel | installed (which/where), version, credState, commands, hidden |
| `apps/web/src/app/api/capabilities/[[...path]]/route.ts` | web API routes | — |
| `apps/web/src/app/api/chats/[id]/route.ts` | web API routes | — |
| `apps/web/src/app/api/computer/[[...path]]/route.ts` | web API routes | — |
| `apps/web/src/app/api/connectors/[[...path]]/route.ts` | web API routes | — |
| `apps/web/src/app/api/dictate/[...path]/route.ts` | web API routes | — |
| `apps/web/src/app/api/dictate/history/route.ts` | web API routes | — |
| `apps/web/src/app/api/edits/[[...path]]/route.ts` | web API routes | — |
| `apps/web/src/app/api/flow/agent-models/route.ts` | web API routes | — |
| `apps/web/src/app/api/flow/config/route.ts` | web API routes | — |
| `apps/web/src/app/api/flow/sessions/[id]/asset/route.ts` | web API routes | — |
| `apps/web/src/app/api/flow/sessions/[id]/route.ts` | web API routes | — |
| `apps/web/src/app/api/flow/sessions/route.ts` | web API routes | — |
| `apps/web/src/app/api/history/agentSessions.test.ts` | web API routes | — |
| `apps/web/src/app/api/history/agentSessions.ts` | discovery | Claude JSONL / Codex rollout / Cursor meta / OpenCode & Hermes sqlite parsers, `mergeListed`, delete external |
| `apps/web/src/app/api/history/route.ts` | history API | merge OpenLive chats with agents' own sessions, retention, clear all |
| `apps/web/src/app/api/history/session/route.ts` | history API | delete an agent's own session |
| `apps/web/src/app/api/home/route.ts` | web API routes | — |
| `apps/web/src/app/api/memory/[[...path]]/route.ts` | web API routes | — |
| `apps/web/src/app/api/models/route.ts` | web API routes | — |
| `apps/web/src/app/api/providers/[id]/route.ts` | web API routes | — |
| `apps/web/src/app/api/providers/route.ts` | web API routes | — |
| `apps/web/src/app/api/reminders/[[...path]]/route.ts` | web API routes | — |
| `apps/web/src/app/api/settings/route.test.ts` | web API routes | — |
| `apps/web/src/app/api/settings/route.ts` | settings API | plain settings GET/PUT, settings secret for off-machine Ollama (grep'd) |
| `apps/web/src/app/api/skills/[[...path]]/route.ts` | web API routes | — |
| `apps/web/src/app/api/ui-state/route.ts` | web API routes | — |
| `apps/web/src/app/api/voice/[...path]/route.ts` | proxy | Same-origin proxy to the agent's `/voice/*`, injects the shared secret, streams bodies. |
| `apps/web/src/app/api/workspace/route.ts` | web API routes | — |

## tools/MCP/skills/memory (30 files)

| path | feature | role |
|---|---|---|
| `services/agent/src/capabilities/approval.test.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/approval.ts` | approval | `askEach` (call), `consentApprove` (Flow one-time consent), `allowAll` |
| `services/agent/src/capabilities/assistant.ts` | built-ins | `delegate`, `update_todos`, `remember`, `look` |
| `services/agent/src/capabilities/checkpoints.test.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/checkpoints.ts` | built-ins | `list_edits`, `undo_edit`, checkpoint journal |
| `services/agent/src/capabilities/device-tools.test.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/device-tools.ts` | built-ins | ol-input tools (screenshot, click, type, windows, shell, open_url…) |
| `services/agent/src/capabilities/device.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/dispatch.test.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/dispatch.ts` | dispatch | `ToolSet` (loose lookup + aliases), `normalizeArgs`, `validateArgs`, `dispatch`/`dispatchAll`, on-demand unwrap, `offerOf` |
| `services/agent/src/capabilities/edit-routes.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/files.test.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/files.ts` | built-ins | `list_dir`, `read_file`, `write_file`, `edit_file` (workspace-fenced, checkpointed) |
| `services/agent/src/capabilities/find.test.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/find.ts` | built-ins | `find_files` backends (mdfind / Windows Search / fd+locate / walk) |
| `services/agent/src/capabilities/groups.test.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/groups.ts` | tool groups | `GROUPS` table, `disabledToolGroups` setting, `groupTools` for Settings |
| `services/agent/src/capabilities/input-lock.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/mcp.test.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/mcp.ts` | loopback MCP | `mcpServer` (low-level Server, tools/list + tools/call), `serveMcp` (random port+path, Host check, `toolsChanged`) |
| `services/agent/src/capabilities/on-demand.test.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/on-demand.ts` | connector loading | `find_tools`/`read_tool`/`use_tool`, `AUTO_THRESHOLD` 40 tools / 8k tokens |
| `services/agent/src/capabilities/profiles.ts` | profiles | `CHAT`/`FLOW` ordering, prompt builder, approval policy |
| `services/agent/src/capabilities/registry.test.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/registry.ts` | registry | `ToolRegistry.tools(profile, session)`, builtins provider, `builtinCatalog`, machine tools selection |
| `services/agent/src/capabilities/routes.ts` | /capabilities | list groups, toggle group, on-demand mode, write-only Exa key |
| `services/agent/src/capabilities/text.ts` | built-ins | `insert_text`, `read_selection`, `clipboard_read/write`, `get_context`, `set_dictation` |
| `services/agent/src/capabilities/types.ts` | tool model | `Tool`, `Session`, `ToolCtx`, `ToolResult`, `Approve`, `Emit` |
| `services/agent/src/capabilities/web.test.ts` | tools/MCP/skills/memory | — |
| `services/agent/src/capabilities/web.ts` | worker tools | `web_search` (Exa), `fetch_url` (SSRF guard, DNS pinning), `params` zod→JSON Schema |

## Flow (orb/owner renderer) (27 files)

| path | feature | role |
|---|---|---|
| `apps/web/src/lib/flow/bridge.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/failure.test.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/failure.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/format.test.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/format.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/onboarding.test.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/onboarding.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/ownerFact.test.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/ownerFact.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/quiet.test.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/quiet.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/sessionTimeline.test.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/sessionTimeline.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/sessions.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/setup.test.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/setup.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/talk.test.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/talk.ts` | talk | one open session, hold latching, Close after silence |
| `apps/web/src/lib/flow/types.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/useCapabilities.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/useFlowConfig.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/useFlowOwner.ts` | Flow voice | Second `VoiceEngine` for Flow with `TurnTuning` from flow-store and `backchannels: false`. |
| `apps/web/src/lib/flow/useVoiceSetup.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/voice.test.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/voice.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/wait.test.ts` | Flow (orb/owner renderer) | — |
| `apps/web/src/lib/flow/wait.ts` | Flow (orb/owner renderer) | — |

## Flow store (26 files)

| path | feature | role |
|---|---|---|
| `packages/flow-store/package.json` | Flow store | — |
| `packages/flow-store/src/config.test.ts` | Flow store | — |
| `packages/flow-store/src/config.ts` | Flow turn defaults | threshold 0.65, holdMs 6000, redemptionMs 800 (overridable). |
| `packages/flow-store/src/config.v1.fixture.ts` | Flow store | — |
| `packages/flow-store/src/config.v6.fixture.ts` | Flow store | — |
| `packages/flow-store/src/config.v7.fixture.ts` | Flow store | — |
| `packages/flow-store/src/config.v8.fixture.ts` | Flow store | — |
| `packages/flow-store/src/dictations.test.ts` | Flow store | — |
| `packages/flow-store/src/dictations.ts` | dictate history | `dictations.jsonl` append, fold, cap 1000, retention rewrite |
| `packages/flow-store/src/history.scale.test.ts` | Flow store | — |
| `packages/flow-store/src/history.test.ts` | Flow store | — |
| `packages/flow-store/src/history.ts` | flow history | list/search/load/delete/prune/rename sessions |
| `packages/flow-store/src/idle.test.ts` | Flow store | — |
| `packages/flow-store/src/idle.ts` | Flow store | — |
| `packages/flow-store/src/index.ts` | Flow store | — |
| `packages/flow-store/src/jsonl.test.ts` | Flow store | — |
| `packages/flow-store/src/jsonl.ts` | Flow store | — |
| `packages/flow-store/src/lease.test.ts` | Flow store | — |
| `packages/flow-store/src/lease.ts` | Flow store | — |
| `packages/flow-store/src/paths.test.ts` | Flow store | — |
| `packages/flow-store/src/paths.ts` | flow store | `flow/` dir, sessions, assets, lease paths |
| `packages/flow-store/src/session.test.ts` | Flow store | — |
| `packages/flow-store/src/session.ts` | Flow store | — |
| `packages/flow-store/src/shared.ts` | flow/dictate config | `HISTORY_KEEPS`/`KEEP_MS`, PTT/toggle key rules, `defaultBrain`/`flowBrain`/`dictateBrain` |
| `packages/flow-store/src/types.ts` | flow store | session file format v1 (header, entries, states) |
| `packages/flow-store/tsconfig.json` | Flow store | — |

## telemetry (25 files)

| path | feature | role |
|---|---|---|
| `apps/desktop/telemetry/aggregator.cjs` | telemetry | — |
| `apps/desktop/telemetry/aggregator.test.ts` | telemetry | — |
| `apps/desktop/telemetry/config.cjs` | telemetry | stamped config validation, `isActive` kill switches |
| `apps/desktop/telemetry/config.test.ts` | telemetry | — |
| `apps/desktop/telemetry/feedback.cjs` | telemetry | — |
| `apps/desktop/telemetry/feedback.test.ts` | telemetry | — |
| `apps/desktop/telemetry/index.cjs` | telemetry | — |
| `apps/desktop/telemetry/index.test.ts` | telemetry | — |
| `apps/desktop/telemetry/limits.cjs` | telemetry | — |
| `apps/desktop/telemetry/limits.test.ts` | telemetry | — |
| `apps/desktop/telemetry/queue.cjs` | telemetry | — |
| `apps/desktop/telemetry/queue.test.ts` | telemetry | — |
| `apps/desktop/telemetry/rig.ts` | telemetry | — |
| `apps/desktop/telemetry/schema.json` | telemetry | — |
| `apps/desktop/telemetry/schema.test.ts` | telemetry | — |
| `apps/desktop/telemetry/sender.cjs` | telemetry | — |
| `apps/desktop/telemetry/sender.test.ts` | telemetry | — |
| `apps/desktop/telemetry/state.cjs` | telemetry | — |
| `apps/desktop/telemetry/state.test.ts` | telemetry | — |
| `apps/desktop/telemetry/transport.cjs` | telemetry | — |
| `apps/desktop/telemetry/transport.test.ts` | telemetry | — |
| `apps/desktop/telemetry/username.cjs` | telemetry | — |
| `apps/desktop/telemetry/username.test.ts` | telemetry | — |
| `apps/desktop/telemetry/validate.cjs` | telemetry | — |
| `apps/desktop/telemetry/validate.test.ts` | telemetry | — |

## assets (23 files)

| path | feature | role |
|---|---|---|
| `assets/clone-voice.png` | assets | — |
| `assets/dictate-home.png` | assets | — |
| `assets/dictate.png` | assets | — |
| `assets/flow-access.png` | assets | — |
| `assets/flow-home.png` | assets | — |
| `assets/flow-orb-acting.png` | assets | — |
| `assets/flow-orb-failure.png` | assets | — |
| `assets/flow-orb-hover.png` | assets | — |
| `assets/flow-orb-listening.png` | assets | — |
| `assets/flow-orb-permission.png` | assets | — |
| `assets/flow-orb-speaking.png` | assets | — |
| `assets/flow-orb-states.png` | assets | — |
| `assets/flow-settings.png` | assets | — |
| `assets/hero.png` | assets | — |
| `assets/home.png` | assets | — |
| `assets/lobby.png` | assets | — |
| `assets/logo-dark.gif` | assets | — |
| `assets/logo-light.gif` | assets | — |
| `assets/logo.svg` | assets | — |
| `assets/openlive-social-preview.png` | assets | — |
| `assets/settings.png` | assets | — |
| `assets/tour.png` | assets | — |
| `assets/welcome.png` | assets | — |

## voice regress (22 files)

| path | feature | role |
|---|---|---|
| `tools/voice-regress/bakeoff.json` | voice regress | — |
| `tools/voice-regress/baseline/kitten.json` | voice regress | — |
| `tools/voice-regress/baseline/kokoro-js.json` | voice regress | — |
| `tools/voice-regress/baseline/kokoro-native.json` | voice regress | — |
| `tools/voice-regress/baseline/matcha.json` | voice regress | — |
| `tools/voice-regress/baseline/piper-lessac.json` | voice regress | — |
| `tools/voice-regress/baseline/supertonic-agent.json` | voice regress | — |
| `tools/voice-regress/baseline/supertonic.json` | voice regress | — |
| `tools/voice-regress/corpus.json` | voice regress | — |
| `tools/voice-regress/package.json` | voice regress | — |
| `tools/voice-regress/src/analyze.test.ts` | voice regress | — |
| `tools/voice-regress/src/analyze.ts` | metrics | Join analysis (pitch, pause, loudness, lead/tail, broken samples). |
| `tools/voice-regress/src/bakeoff.ts` | bake-off | P0 benchmark per provider, renders, WER/UTMOS/CED scoring, table output. |
| `tools/voice-regress/src/capture.test.ts` | voice regress | — |
| `tools/voice-regress/src/capture.ts` | playback analysis | Reads `ttsCapture` manifests, reports clicks/gaps/DC steps, writes reconstruction.wav. |
| `tools/voice-regress/src/chatterbox.ts` | bake-off candidate | Chatterbox-Turbo ONNX pipeline on onnxruntime-node. |
| `tools/voice-regress/src/engines.ts` | regression engines | Per-engine adapters (native worker, kokoro-js, Supertonic), pinned SHA-256 sums, tiers/slack/limits. |
| `tools/voice-regress/src/run.ts` | regression | Streams corpus through the chunker and engines, compares joins against one-go renders, gates and baselines. |
| `tools/voice-regress/src/score.test.ts` | voice regress | — |
| `tools/voice-regress/src/score.ts` | voice regress | — |
| `tools/voice-regress/src/summary.ts` | metrics | `METRICS` thresholds, delta simulation, summarize. |
| `tools/voice-regress/tsconfig.json` | voice regress | — |

## provider harness (21 files)

| path | feature | role |
|---|---|---|
| `packages/harness/package.json` | provider harness | — |
| `packages/harness/src/anthropic.test.ts` | provider harness | — |
| `packages/harness/src/anthropic.ts` | adapter | `/messages` with cache_control placement (grep'd) |
| `packages/harness/src/catalog.ts` | catalog | models.dev cache (24 h) |
| `packages/harness/src/effort.test.ts` | provider harness | — |
| `packages/harness/src/effort.ts` | effort | thinking budgets, OpenAI effort map, `anthropicThinkingForm`, `isReasoningModel` |
| `packages/harness/src/index.ts` | harness | `streamProvider` dispatch, tools-refused retry |
| `packages/harness/src/models.ts` | model listing | live `/models` + models.dev enrichment |
| `packages/harness/src/openai-chat.test.ts` | provider harness | — |
| `packages/harness/src/openai-chat.ts` | provider harness | — |
| `packages/harness/src/openai-responses.test.ts` | provider harness | — |
| `packages/harness/src/openai-responses.ts` | provider harness | — |
| `packages/harness/src/paths.ts` | provider harness | — |
| `packages/harness/src/registry.test.ts` | provider harness | — |
| `packages/harness/src/registry.ts` | providers | `BUILTIN_PROVIDERS` (15), snapshots, Ollama URL, `resolveApiMode` |
| `packages/harness/src/retry.ts` | adapter | pre-stream retry/backoff (grep'd) |
| `packages/harness/src/sse.ts` | provider harness | — |
| `packages/harness/src/stream-provider.test.ts` | provider harness | — |
| `packages/harness/src/transient.test.ts` | provider harness | — |
| `packages/harness/src/types.ts` | harness | `Message`, `ChatRequest`, `ProviderInfo`, `ModelInfo`, `ProviderEvent`, `Protocol` |
| `packages/harness/tsconfig.json` | provider harness | — |

## store (19 files)

| path | feature | role |
|---|---|---|
| `packages/db/package.json` | store | — |
| `packages/db/src/connectors.test.ts` | store | — |
| `packages/db/src/connectors.ts` | connectors store | rows over mcp.json + secrets, OAuth per issuer, consent, tool cache |
| `packages/db/src/crypto.ts` | secrets | `encryptSecret`/`decryptSecret` over the lazily loaded key |
| `packages/db/src/env.ts` | dev | `.env` loader |
| `packages/db/src/index.ts` | exports | package surface |
| `packages/db/src/migrate-conversations.ts` | migration | legacy conversations.json → SQLite |
| `packages/db/src/paths.ts` | store | `PATHS` from `layout(resolveHome())`, runs `migrateHome` at import, `skillsDir` |
| `packages/db/src/queries.test.ts` | store | — |
| `packages/db/src/queries.ts` | queries | providers (encrypted keys), chats/messages, voice profiles, settings (secret routing), memory raw access |
| `packages/db/src/reminders.ts` | reminders store | `state/reminders.json` |
| `packages/db/src/reset.ts` | dev | clear local data script |
| `packages/db/src/skills.ts` | skills state | `state/skills.json` disabled set |
| `packages/db/src/sqlite.ts` | SQLite | schema (chats, messages, meta), PRAGMAs, `scrubDeleted`, busy retry |
| `packages/db/src/store.test.ts` | store | — |
| `packages/db/src/store.ts` | JSON store | `readJson`/`writeJson`, `withFileLock` (proper-lockfile + in-process chain), `updateJson` |
| `packages/db/src/ui-state.test.ts` | store | — |
| `packages/db/src/ui-state.ts` | store | — |
| `packages/db/tsconfig.json` | store | — |

## native speech engines (19 files)

| path | feature | role |
|---|---|---|
| `services/agent/src/voice/accel.test.ts` | native speech engines | — |
| `services/agent/src/voice/accel.ts` | native speech engines | — |
| `services/agent/src/voice/addressee.ts` | native speech engines | — |
| `services/agent/src/voice/bench.ts` | native speech engines | — |
| `services/agent/src/voice/device.test.ts` | native speech engines | — |
| `services/agent/src/voice/device.ts` | native speech engines | — |
| `services/agent/src/voice/engine.ts` | native speech engines | — |
| `services/agent/src/voice/native-models.test.ts` | native speech engines | — |
| `services/agent/src/voice/native-models.ts` | native speech engines | — |
| `services/agent/src/voice/native-worker.ts` | native speech engines | — |
| `services/agent/src/voice/native.test.ts` | native speech engines | — |
| `services/agent/src/voice/native.ts` | native speech engines | — |
| `services/agent/src/voice/pcm.test.ts` | native speech engines | — |
| `services/agent/src/voice/pcm.ts` | native speech engines | — |
| `services/agent/src/voice/routes.test.ts` | native speech engines | — |
| `services/agent/src/voice/routes.ts` | native speech engines | — |
| `services/agent/src/voice/voiceprint.test.ts` | native speech engines | — |
| `services/agent/src/voice/voiceprint.ts` | native speech engines | — |
| `services/agent/src/voice/web-catalog.test.ts` | native speech engines | — |

## web app (18 files)

| path | feature | role |
|---|---|---|
| `apps/web/next.config.ts` | web app | — |
| `apps/web/package.json` | web app | — |
| `apps/web/postcss.config.mjs` | web app | — |
| `apps/web/public/agents/claude.svg` | web app | — |
| `apps/web/public/agents/codex.svg` | web app | — |
| `apps/web/public/agents/copilot.svg` | web app | — |
| `apps/web/public/agents/cursor.svg` | web app | — |
| `apps/web/public/agents/gemini.svg` | web app | — |
| `apps/web/public/agents/hermes.svg` | web app | — |
| `apps/web/public/agents/kiro.svg` | web app | — |
| `apps/web/public/agents/opencode.svg` | web app | — |
| `apps/web/public/agents/pi.svg` | web app | — |
| `apps/web/scripts/copy-voice-assets.mjs` | VAD assets | Vendors `silero_vad_v6.onnx`, `silero_vad_v5.onnx`, vad worklet and ORT wasm into `public/vad/`. |
| `apps/web/scripts/dev.mjs` | web app | — |
| `apps/web/src/design.lint.test.ts` | web app | — |
| `apps/web/src/proxy.test.ts` | web app | — |
| `apps/web/src/proxy.ts` | web app | — |
| `apps/web/tsconfig.json` | web app | — |

## live/flow websockets (18 files)

| path | feature | role |
|---|---|---|
| `services/agent/src/live/flow-resume.test.ts` | live/flow websockets | — |
| `services/agent/src/live/flow-ws.test.ts` | live/flow websockets | — |
| `services/agent/src/live/flow-ws.ts` | Flow ACP brain | `serveMcp` + `AgentSupervisor(AcpAgent)` with `buildFlowAcpPreamble`, `AcpBrain` |
| `services/agent/src/live/narrator.test.ts` | live/flow websockets | — |
| `services/agent/src/live/narrator.ts` | spoken progress | `wrapEmitWithNarration` (`say` lines) and `createCommentaryGate` |
| `services/agent/src/live/replay.selfcheck.ts` | live/flow websockets | — |
| `services/agent/src/live/session-bind.test.ts` | live/flow websockets | — |
| `services/agent/src/live/session-cut.test.ts` | live/flow websockets | — |
| `services/agent/src/live/session-language.test.ts` | live/flow websockets | — |
| `services/agent/src/live/session-mcp.test.ts` | live/flow websockets | — |
| `services/agent/src/live/session-telemetry.test.ts` | live/flow websockets | — |
| `services/agent/src/live/session.ts` | LiveSession | `/live` chat session: bind, turn, permission/elicitation relay (120 s), barge-in cut, replay ingest, MCP server, persistence |
| `services/agent/src/live/turn-runner.test.ts` | live/flow websockets | — |
| `services/agent/src/live/turn-runner.ts` | API brain | provider turn loop (6 steps + tool-free last), `describeFrames`, history cap |
| `services/agent/src/live/worker.test.ts` | live/flow websockets | — |
| `services/agent/src/live/worker.ts` | delegate worker | web subagent (`web_search`/`fetch_url`, 5 steps), narration lines |
| `services/agent/src/live/ws.test.ts` | live/flow websockets | — |
| `services/agent/src/live/ws.ts` | /live gate | secret/token check, loopback origin rule, chat vs flow session dispatch |

## Flow UI (14 files)

| path | feature | role |
|---|---|---|
| `apps/web/src/components/flow/AddonCard.tsx` | Flow UI | — |
| `apps/web/src/components/flow/FlowCanvas.tsx` | Flow UI | — |
| `apps/web/src/components/flow/FlowEvent.tsx` | Flow UI | — |
| `apps/web/src/components/flow/FlowHome.tsx` | Flow UI | — |
| `apps/web/src/components/flow/FlowOnboarding.tsx` | Flow UI | — |
| `apps/web/src/components/flow/FlowOrb.tsx` | Flow UI | — |
| `apps/web/src/components/flow/FlowSessionModal.tsx` | Flow UI | — |
| `apps/web/src/components/flow/FlowSettings.tsx` | Flow UI | — |
| `apps/web/src/components/flow/FlowShell.tsx` | Flow UI | — |
| `apps/web/src/components/flow/GrantPills.tsx` | Flow UI | — |
| `apps/web/src/components/flow/InputAccessFix.tsx` | Flow UI | — |
| `apps/web/src/components/flow/ModeSwitch.tsx` | Flow UI | — |
| `apps/web/src/components/flow/PowerPill.tsx` | Flow UI | — |
| `apps/web/src/components/flow/VoiceModelsCard.tsx` | Flow UI | — |

## shared speech (14 files)

| path | feature | role |
|---|---|---|
| `packages/shared/src/speech/addressee-head.ts` | shared speech | — |
| `packages/shared/src/speech/addressee.test.ts` | shared speech | — |
| `packages/shared/src/speech/addressee.ts` | shared speech | — |
| `packages/shared/src/speech/lexicon.test.ts` | shared speech | — |
| `packages/shared/src/speech/lexicon.ts` | shared speech | — |
| `packages/shared/src/speech/normalize.test.ts` | shared speech | — |
| `packages/shared/src/speech/normalize.ts` | shared speech | — |
| `packages/shared/src/speech/supertonic.ts` | shared speech | — |
| `packages/shared/src/speech/timing.test.ts` | shared speech | — |
| `packages/shared/src/speech/timing.ts` | shared speech | — |
| `packages/shared/src/speech/trim.test.ts` | shared speech | — |
| `packages/shared/src/speech/trim.ts` | shared speech | — |
| `packages/shared/src/speech/voiceprint.test.ts` | shared speech | — |
| `packages/shared/src/speech/voiceprint.ts` | shared speech | — |

## ACP driving (14 files)

| path | feature | role |
|---|---|---|
| `services/agent/src/agents/acp-agent.test.ts` | ACP driving | — |
| `services/agent/src/agents/acp-agent.ts` | ACP driver | spawn adapter, `initialize`/`session/resume`/`session/load`/`session/new`, `_meta.claudeCode.options`, `session/prompt`, update mapping, permission relay, terminals, elicitations, `session/cancel`, `session/list`, dispose |
| `services/agent/src/agents/fake-acp-agent.fixture.mjs` | ACP driving | — |
| `services/agent/src/agents/index.ts` | binding | `boundAgent`, `agentCwd` (realpath), `createBoundAgent` (supervisor + AcpAgent + MCP wire), `flowAgentCwd` |
| `services/agent/src/agents/mcp-config.test.ts` | ACP driving | — |
| `services/agent/src/agents/mcp-config.ts` | .mcp.json passthrough | `readProjectMcpServers` (cap 20, http/sse gated), `hostedBy` title match |
| `services/agent/src/agents/models-route.ts` | probes | `GET /agents/models` (session/new probe, 5 min cache), `GET /agents/sessions` (initialize-only `session/list`, 60 s cache, PATH-gated) |
| `services/agent/src/agents/pi-bridge.ts` | Pi | temp 0700 dir with launcher + `pi.registerMcpServer` extension carrying OpenLive's servers |
| `services/agent/src/agents/proc.ts` | process trees | `track` + exit reaping, `killTree` (PG SIGTERM→SIGKILL, taskkill /T) |
| `services/agent/src/agents/supervisor.test.ts` | ACP driving | — |
| `services/agent/src/agents/supervisor.ts` | reliability | per-turn watchdogs (start/first-output/stall), restart-once with text history seed, spoken failure |
| `services/agent/src/agents/terminal-manager.test.ts` | ACP driving | — |
| `services/agent/src/agents/terminal-manager.ts` | ACP terminals | client-hosted `terminal/*`: spawn, tail-capped output, 80 ms live flush, kill/release |
| `services/agent/src/agents/types.ts` | types | `Agent`, `TurnInput`, `AskPermission`, `PERMISSION_CANCELLED`, `AgentMeta`, `ReplayMessage` |

## root (13 files)

| path | feature | role |
|---|---|---|
| `.gitignore` | root | — |
| `CHANGELOG.md` | root | — |
| `CONTRIBUTING.md` | regress / bake-off | How to run `voice:regress`, `voice:bakeoff`, tiers, caches. |
| `LICENSE` | root | — |
| `NOTICE` | root | — |
| `README.md` | overview | Product framing: cascaded on-device pipeline, engine list, ten languages, PTT vs hands-free, data folder layout, download sizes. |
| `RELEASING.md` | root | — |
| `THIRD_PARTY_NOTICES` | licenses | Adapted source code only (Orca, Cua Driver, Orb wave orb); no model licenses here. |
| `package.json` | scripts | `dev`, `desktop:dev` (AGENT_PORT=47833 WEB_PORT=47834), pre-sweeps |
| `pnpm-lock.yaml` | root | — |
| `pnpm-workspace.yaml` | root | — |
| `tsconfig.base.json` | root | — |
| `vitest.config.ts` | root | — |

## Flow tool loop (11 files)

| path | feature | role |
|---|---|---|
| `services/agent/src/flow/brain.test.ts` | Flow tool loop | — |
| `services/agent/src/flow/brain.ts` | Flow brains | `LocalBrain` provider mapper, `AcpBrain` |
| `services/agent/src/flow/loop.test.ts` | Flow tool loop | — |
| `services/agent/src/flow/loop.ts` | Flow tool loop | — |
| `services/agent/src/flow/partial-json.test.ts` | Flow tool loop | — |
| `services/agent/src/flow/partial-json.ts` | Flow tool loop | — |
| `services/agent/src/flow/prompt.test.ts` | Flow tool loop | — |
| `services/agent/src/flow/prompt.ts` | Flow prompt | `buildFlowPrompt`, `buildFlowAcpPreamble`, namespaced tool names |
| `services/agent/src/flow/retention.test.ts` | Flow tool loop | — |
| `services/agent/src/flow/retention.ts` | Flow context | `trimImages` keeps the 3 newest screenshots |
| `services/agent/src/flow/types.ts` | Flow tool loop | — |

## pages (9 files)

| path | feature | role |
|---|---|---|
| `apps/web/src/app/flow-owner/page.tsx` | pages | — |
| `apps/web/src/app/flow/page.tsx` | pages | — |
| `apps/web/src/app/global-error.tsx` | pages | — |
| `apps/web/src/app/globals.css` | pages | — |
| `apps/web/src/app/icon.svg` | pages | — |
| `apps/web/src/app/layers.test.ts` | pages | — |
| `apps/web/src/app/layout.tsx` | pages | — |
| `apps/web/src/app/page.tsx` | pages | — |
| `apps/web/src/app/providers.tsx` | pages | — |

## addressee eval (8 files)

| path | feature | role |
|---|---|---|
| `tools/addressee/package.json` | addressee eval | — |
| `tools/addressee/src/data.ts` | addressee eval | — |
| `tools/addressee/src/head.test.ts` | addressee eval | — |
| `tools/addressee/src/head.ts` | addressee eval | — |
| `tools/addressee/src/run.ts` | addressee eval | — |
| `tools/addressee/src/simulate.ts` | addressee eval | — |
| `tools/addressee/src/train.ts` | addressee eval | — |
| `tools/addressee/tsconfig.json` | addressee eval | — |

## CI (7 files)

| path | feature | role |
|---|---|---|
| `.github/CODEOWNERS` | CI | — |
| `.github/ISSUE_TEMPLATE/bug_report.md` | CI | — |
| `.github/ISSUE_TEMPLATE/feature_request.md` | CI | — |
| `.github/PULL_REQUEST_TEMPLATE.md` | CI | — |
| `.github/workflows/ci.yml` | CI | — |
| `.github/workflows/release.yml` | CI | — |
| `.github/workflows/voice.yml` | CI | — |

## docs (7 files)

| path | feature | role |
|---|---|---|
| `docs/ARCHITECTURE.md` | voice loop | Authoritative narrative of one turn, chunker rules, barge-in, model licenses, Supertonic-on-agent, native engine benchmarking, voiceprint and side-talk evals with measured numbers. |
| `docs/CHAT.md` | chat | who answers, History drawer and retention |
| `docs/DESIGN.md` | docs | — |
| `docs/DICTATE.md` | dictate | cleanup rules, AI polish flow, developer architecture (hook → engine → rewrite → insert) |
| `docs/FLOW.md` | docs | — |
| `docs/PRIVACY.md` | docs | — |
| `docs/TELEMETRY.md` | docs | — |

## computer use client (7 files)

| path | feature | role |
|---|---|---|
| `services/agent/src/computer/fake-helper.mjs` | computer use client | — |
| `services/agent/src/computer/helper.test.ts` | computer use client | — |
| `services/agent/src/computer/helper.ts` | computer use client | — |
| `services/agent/src/computer/routes.test.ts` | computer use client | — |
| `services/agent/src/computer/routes.ts` | computer use client | — |
| `services/agent/src/computer/tools.test.ts` | computer use client | — |
| `services/agent/src/computer/tools.ts` | built-ins | computer-use helper tools (get_app_state, click, perform_action…) |

## voiceprint eval (7 files)

| path | feature | role |
|---|---|---|
| `tools/voiceprint/package.json` | voiceprint eval | — |
| `tools/voiceprint/src/audio.test.ts` | voiceprint eval | — |
| `tools/voiceprint/src/audio.ts` | voiceprint eval | — |
| `tools/voiceprint/src/metrics.test.ts` | voiceprint eval | — |
| `tools/voiceprint/src/metrics.ts` | voiceprint eval | — |
| `tools/voiceprint/src/run.ts` | eval | Speaker-model eval on LibriSpeech + agent voices under noise/room conditions; picked CAM++. |
| `tools/voiceprint/tsconfig.json` | voiceprint eval | — |

## converse eval (6 files)

| path | feature | role |
|---|---|---|
| `tools/converse/package.json` | converse eval | — |
| `tools/converse/src/measure.test.ts` | converse eval | — |
| `tools/converse/src/measure.ts` | converse eval | — |
| `tools/converse/src/run.eval.ts` | eval | Scripted conversations through the real `VoiceEngine` + Silero + Smart-Turn + Nemotron stream + `/live`, measuring latency and listening-cue overlap. |
| `tools/converse/tsconfig.json` | converse eval | — |
| `tools/converse/vitest.config.ts` | converse eval | — |

## scripts (1 files)

| path | feature | role |
|---|---|---|
| `scripts/free-ports.mjs` | dev | kill stale listeners on 3000/8787/47833/47834/9333, sweep dev supervisors |

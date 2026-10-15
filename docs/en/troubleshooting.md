# Troubleshooting

| Symptom | Fix |
|---|---|
| Key press does nothing | ClyphX Pro selected as Control Surface? Input = `LL Deck`? Restarted Live after installing? |
| Stream Deck keys play notes in the synth | Turn *Track* off for input `LL Deck`. |
| Status bar: `track "LOOPER" not found` | Name the track exactly `LOOPER` (case-sensitive). |
| `"Synth 1" not offered as input` | The source must output audio (instrument loaded) and can't be LOOPER itself. Check names. |
| Mic not recorded | `Mic` monitor *In*, right input, level visible on the track? |
| I hear the source twice | See *Avoid hearing things twice* in setup.md. |
| Preset doesn't change | Pigments as AU/VST2 instead of VST3; playlist created; synth track armed; `LL Synth` input *Track* on; ClyphX Output = `LL Synth`. |
| Work without the User Action | In `X-Controls` replace `$LL_SYN1$` with `$LLB_SYN1$` etc. – uses built-in ClyphX actions only. |

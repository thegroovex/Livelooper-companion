# livelooper companion

*designed by groovex* · [Deutsch](README.de.md)

Pick **which track livelooper records** at the press of a key during a performance – up to **12 sources** (synths, rhythm, mic …) – and switch **synth presets** (e.g. Pigments). Runs in Ableton Live 12 with **ClyphX Pro**, easiest to play from an **Elgato Stream Deck** (15 keys).

| Page 1 · Sources | Page 2 · Perform |
|---|---|
| ![Page 1](streamdeck/layout-page1.png) | ![Page 2](streamdeck/layout-page2.png) |

## What happens on a key press?
`SOURCE 2` →
1. The LOOPER track gets **Synth 2 (Post FX)** as input and monitor **In**.
2. Synth 2 is **armed** (your keyboard plays it), Synth 1 and 3 are disarmed.
3. Live's status bar shows `livelooper: recording source -> Synth 2`.

`PRESET 1–8` send a Program Change to the active synth. `LOOP REC/PLAY/UNDO/CLEAR` drive livelooper directly.

## Install in 3 steps
1. **Requirements:** Ableton Live 12, ClyphX Pro (selected once as Control Surface in *Settings → Link, Tempo & MIDI*), optionally a Stream Deck with the *Midi* plugin by Trevliga Spel.
2. **Download** → **double-click** `install.command`. It copies the User Action, adds macros and X-Controls to ClyphX Pro (with backup, safe to run again) and puts the Stream Deck icons on your Desktop. If macOS says “unidentified developer”: right-click → Open.
3. **Let it build the template:** launch a clip named `[SETUP] LLSETUP 8` in Live – the action creates synths, Rhythm, Mic and LOOPER, loads Pigments and livelooper, then *Save as Template*. Details: [docs/en/setup.md](docs/en/setup.md)

Stream Deck: [docs/en/stream-deck.md](docs/en/stream-deck.md) · Presets: [docs/en/presets.md](docs/en/presets.md) · Problems: [docs/en/troubleshooting.md](docs/en/troubleshooting.md)

Uninstall: double-click `uninstall.command`.

## Dynamic: 3 to 12 sources
Every track **left of LOOPER** is automatically source 1, 2, 3 … (max 12) in track order. Add, move or rename a track – no config needed. Tracks whose name starts with `_` and group tracks are skipped.

| Template | Result |
|---|---|
| `LLSETUP` | Synth 1–3, Rhythm, Mic, LOOPER (5 sources) |
| `LLSETUP 8` | Synth 1–6, Rhythm, Mic, LOOPER |
| `LLSETUP 12` | Synth 1–10, Rhythm, Mic, LOOPER |
| `LLSETUP 8 NOPLUG` | same, without loading plug-ins |

## License
AGPL-3.0 – see [LICENSE](LICENSE). ClyphX Pro, Pigments and Stream Deck are products of their respective makers and not part of this repo.

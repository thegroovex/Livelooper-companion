# Setup (Live Set)

About 10 minutes, once. Then save it as your template (*File → Save Live Set as Template*).

## 1. Two virtual MIDI ports (IAC)
1. Open **Audio MIDI Setup** (Applications → Utilities) → *Window → Show MIDI Studio*.
2. Double-click **IAC Driver** → tick **Device is online**.
3. Under *Ports* add two ports with **+**: **`LL Deck`** and **`LL Synth`**.

| Port | Purpose |
|---|---|
| `LL Deck` | Stream Deck → Live (source select, presets, looper transport) |
| `LL Synth` | ClyphX Pro → synth tracks (Program Change) |

## 2. Live Settings → Link, Tempo & MIDI
- **Control Surface:** `ClyphX Pro` · **Input:** `IAC Driver (LL Deck)` · **Output:** `IAC Driver (LL Synth)`
- **MIDI Ports:**

| Port | Track | Remote |
|---|---|---|
| Input `LL Deck` | **off** | **on** |
| Input `LL Synth` | **on** | off |
| Outputs `LL Deck`, `LL Synth` | off | off |

*Track off* on `LL Deck` matters – otherwise the keys play notes into your synths.

## 3. Tracks (exact names)
| # | Name | Settings |
|---|---|---|
| 1–3 | `Synth 1`, `Synth 2`, `Synth 3` | MIDI track, instrument (e.g. Pigments), input *All Ins / All Channels*, monitor *Auto*, output *Master* |
| 4 | `Rhythm` | Drum Rack, clips or audio – just runs, output *Master* |
| 5 | `Mic` | Audio track, input *Ext. In 1* (your mic), monitor *In*, output *Master* |
| 6 | `LOOPER` | Audio track with **livelooper**, output *Master*. Input/monitor are set by the script. |

## 4. Avoid hearing things twice
The source plays through its own track to Master **and** into LOOPER. If livelooper passes its input through, you hear it twice. Two ways:
- **A (recommended):** turn input pass-through off in livelooper – you hear the source on its track and the loops on LOOPER.
- **B:** set the output of tracks 1–5 to *Sends Only* – you then only hear the selected source (through livelooper); the others are silent.

## 5. Test
Press **SYNTH 1** (or X-Control note 36, channel 16). Live's status bar shows `livelooper: recording source -> Synth 1`, Synth 1 is armed, LOOPER shows *Synth 1 · Post FX* as input.

### Without a Stream Deck
Any pad controller works: send notes 36–53 on **channel 16** and select it as ClyphX Pro *Input*. Or use X-Clips on an empty track, e.g. a clip named `[S1] $LL_SYN1$`.

### Other track names
Edit `SOURCES` and `LOOPER_TRACK` at the top of `clyphx/user_actions/livelooper_companion.py`, run `install.command` again, restart Live.

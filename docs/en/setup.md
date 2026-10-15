# Setup

About 10 minutes, once. You end up with a Live template that makes every new set ready to play.

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

## 3. Build the template automatically
1. Open a **new, empty Live Set** (*File → New Live Set*).
2. Double-click an empty clip slot on one of the MIDI tracks → new clip → **⌘ R** → name it **`[SETUP] LLSETUP 8`** (the number = sources, 3 to 12).
3. Launch the clip. Within seconds you get:

| Tracks | Settings |
|---|---|
| `Synth 1` … `Synth N-2` | MIDI track with **Pigments** (AU preferred) |
| `Rhythm` | MIDI track – Drum Rack or clips of your choice |
| `Mic` | Audio track, input *Ext. In 1*, monitor *In* |
| `LOOPER` | Audio track with **livelooper** |

   Live's empty default tracks are removed; tracks with clips or devices are left alone. If a `LOOPER` already exists, the action changes nothing.
4. Delete the track holding the setup clip, then **File → Save Live Set as Template**.

If the action can't find a plug-in it says so in the status bar – just load it by hand. `LLSETUP 8 NOPLUG` creates the tracks only.

## 4. More or fewer sources (dynamic)
Every track **left of LOOPER** is a source – in track order, max 12. Insert a synth track left of LOOPER = new source. Name starting with `_` (e.g. `_Click`) or a group track = skipped. Fixed list instead: set `SOURCES = ['Synth 1', 'Bass', 'Mic']` at the top of `clyphx/user_actions/livelooper_companion.py` and reinstall.

## 5. Avoid hearing things twice
The source plays through its own track to Master **and** into LOOPER. If livelooper passes its input through, you hear it twice:
- **A (recommended):** turn input pass-through off in livelooper.
- **B:** set the source tracks' output to *Sends Only* – you then only hear the selected source (through livelooper).

## 6. Test
Press **SOURCE 1**. Live's status bar shows `livelooper: recording source -> Synth 1 (1/8)`, Synth 1 is armed, LOOPER shows *Synth 1 · Post FX* as input.

### Without a Stream Deck
Any pad controller works: send notes on **channel 16** (map in [stream-deck.md](stream-deck.md)) and select it as ClyphX Pro *Input*. Or X-Clips, e.g. `[S1] $LL_SRC1$`.

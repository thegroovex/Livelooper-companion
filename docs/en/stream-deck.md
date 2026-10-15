# Stream Deck (standard, 15 keys)

## 1. Plugin
Stream Deck app → **Marketplace** → search **“Midi” by Trevliga Spel** (not “Midi Button”) and install. It is sold on the Elgato Marketplace; check the current price there.

## 2. Profile
New profile **livelooper**. Every key: action **Midi → Note On/Off** (type *Push*), **port `LL Deck`**, **channel 16**, velocity 127. Transport keys: **Midi → Control Change**, port `LL Deck`, channel 16, value 127.
Icons: drag the PNGs from the *livelooper Stream Deck Icons* folder on your Desktop onto the keys.

| Row | Key 1 | Key 2 | Key 3 | Key 4 | Key 5 |
|---|---|---|---|---|---|
| 1 Source | SYNTH 1 · note **36** | SYNTH 2 · **37** | SYNTH 3 · **38** | RHYTHM · **39** | MIC · **40** |
| 2 Presets | PRESET 1 · note **44** | PRESET 2 · **45** | PRESET 3 · **46** | PRESET 4 · **47** | INPUT OFF · note **43** |
| 3 Looper | REC · **CC 20** | PLAY · **CC 21** | UNDO · **CC 22** | CLEAR · **CC 23** | SOURCE NEXT · note **42** |

The plugin may show note names – the number is what counts.

## 3. Map the looper keys (once)
1. Turn on Live's **MIDI Map Mode** (⌘ M).
2. Click livelooper's **Rec** parameter (if needed, use *Configure* in the device header to expose it first).
3. Press the Stream Deck **REC** key. Same for PLAY, UNDO, CLEAR.
4. ⌘ M off. The mapping is saved in the Live Set.

## More keys
Extra X-Controls already exist: note 41 = previous source, 48–51 = preset 5–8, 52/53 = rack chain back/forward. Put them in a Stream Deck folder, for example.

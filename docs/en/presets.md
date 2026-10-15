# Switching synth presets live (e.g. Pigments)

Preset keys always act on the **currently armed synth** – the one you picked with SOURCE.

## Way A: Pigments playlist + Program Change (recommended)
1. In Pigments' preset browser create a **playlist** and add the sounds for the song in order.
2. Load Pigments as **AU** (or VST2) – **not VST3**: Live does not pass Program Changes to VST3 instruments.
3. PRESET 1 = first preset of the playlist, PRESET 2 = second, and so on.
4. With several playlists, Bank Select (MSB) picks the list. Easiest: put the live playlist first.

Tip: switch between phrases – held notes may cut off on a change.

## Way B: Instrument Rack (gapless)
1. Put the Pigments track into an **Instrument Rack**, one chain per sound with its own Pigments instance.
2. In the chain editor give every chain its own chain-select value.
3. Notes 60/61 (X-Controls) step the chain back/forward, or write macros like `"Synth 1"/DEV(1) CSEL "Pad"`.

Pro: instant switch, sounds ring out. Con: more CPU and RAM since all instances stay loaded.

## Other synths
Way A works with any instrument that understands Program Change; way B with anything.

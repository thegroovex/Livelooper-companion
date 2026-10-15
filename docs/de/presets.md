# Synth-Presets live wechseln (z. B. Pigments)

Die Preset-Tasten wirken immer auf den **gerade scharf geschalteten Synth** – also den, den du mit SOURCE gewählt hast.

## Weg A: Pigments-Playlist + Program Change (empfohlen)
1. In Pigments im Preset-Browser eine **Playlist** anlegen und die Sounds für den Song in der gewünschten Reihenfolge hinzufügen.
2. Pigments als **AU** (oder VST2) laden – **nicht VST3**: Live gibt Program Changes nicht an VST3-Instrumente weiter.
3. PRESET 1 = erstes Preset der Playlist, PRESET 2 = zweites usw.
4. Hat Pigments mehrere Playlists, bestimmt Bank Select (MSB), welche gilt. Am einfachsten: die Live-Playlist an erste Stelle legen.

Tipp: zwischen zwei Phrasen umschalten – gehaltene Noten können beim Wechsel abreißen.

## Weg B: Instrument Rack (lückenlos)
1. Pigments-Spur in ein **Instrument Rack** packen, pro Sound eine Kette mit eigener Pigments-Instanz.
2. Im Chain-Editor jede Kette auf einen eigenen Chain-Select-Wert legen.
3. Note 60/61 (X-Controls) schalten die Kette zurück/vor, oder eigene Makros wie `"Synth 1"/DEV(1) CSEL "Pad"`.

Vorteil: sofortiger Wechsel, Sounds klingen aus. Nachteil: mehr CPU und RAM, weil alle Instanzen geladen sind.

## Andere Synths
Weg A funktioniert mit jedem Instrument, das Program Change versteht; Weg B mit allem.

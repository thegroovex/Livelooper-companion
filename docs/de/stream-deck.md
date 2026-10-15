# Stream Deck (Standard, 15 Tasten)

## 1. Plugin
Stream-Deck-App → **Marketplace** → nach **„Midi“ von Trevliga Spel** suchen (nicht „Midi Button“) und installieren. Hinweis: Das Plugin wird im Elgato Marketplace angeboten; prüfe dort den aktuellen Preis.

## 2. Profil anlegen
Neues Profil **livelooper**. Jede Taste: Aktion **Midi → Note On/Off** (Typ *Push*), **Port `LL Deck`**, **Kanal 16**, Velocity 127. Transport-Tasten: **Midi → Control Change**, Port `LL Deck`, Kanal 16, Wert 127.
Icons: Die PNGs aus dem Ordner *livelooper Stream Deck Icons* auf deinem Schreibtisch auf die Tasten ziehen.

| Reihe | Taste 1 | Taste 2 | Taste 3 | Taste 4 | Taste 5 |
|---|---|---|---|---|---|
| 1 Quelle | SYNTH 1 · Note **36** | SYNTH 2 · **37** | SYNTH 3 · **38** | RHYTHM · **39** | MIC · **40** |
| 2 Presets | PRESET 1 · Note **44** | PRESET 2 · **45** | PRESET 3 · **46** | PRESET 4 · **47** | INPUT OFF · Note **43** |
| 3 Looper | REC · **CC 20** | PLAY · **CC 21** | UNDO · **CC 22** | CLEAR · **CC 23** | SOURCE NEXT · Note **42** |

Das Plugin zeigt Noten evtl. als Namen an – maßgeblich ist die Nummer.

## 3. Looper-Tasten zuweisen (einmalig)
1. In Live **MIDI-Map-Modus** an (⌘ M).
2. Im livelooper-Gerät den Parameter **Rec** anklicken (ggf. vorher im Geräte-Header *Konfigurieren* und den Parameter hinzufügen).
3. Stream-Deck-Taste **REC** drücken. Genauso PLAY, UNDO, CLEAR.
4. ⌘ M wieder aus. Die Zuweisung wird im Live-Set gespeichert.

## Mehr Tasten
Weitere X-Controls sind schon definiert: Note 41 = vorherige Quelle, 48–51 = Preset 5–8, 52/53 = Rack-Kette zurück/vor. Lege sie z. B. in einen Stream-Deck-Ordner.

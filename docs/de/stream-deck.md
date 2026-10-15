# Stream Deck (Standard, 15 Tasten, 2 Seiten)

## 1. Plugin
Stream-Deck-App → **Marketplace** → **„Midi“ von Trevliga Spel** (nicht „Midi Button“) installieren. Den aktuellen Preis siehst du im Marketplace.

## 2. Profil anlegen
Neues Profil **livelooper** mit zwei Seiten. Notentasten: Aktion **Midi → Note On/Off**, Typ *Push*, **Port `LL Deck`**, **Kanal 16**, Velocity 127. Looper-Tasten: **Midi → Control Change**, Port `LL Deck`, Kanal 16, Wert 127. Seitenwechsel: eingebaute Aktion **Stream Deck → Nächste/Vorherige Seite**.
Icons: PNGs aus *livelooper Stream Deck Icons* (Schreibtisch) auf die Tasten ziehen. Tipp: Den Titel der Quelltasten auf den Spurnamen ändern (z. B. „Bass“).

**Seite 1 · Quellen** ![Seite 1](../../streamdeck/layout-page1.png)

| Reihe | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | SOURCE 1 · **36** | SOURCE 2 · **37** | SOURCE 3 · **38** | SOURCE 4 · **39** | SOURCE 5 · **40** |
| 2 | SOURCE 6 · **41** | SOURCE 7 · **42** | SOURCE 8 · **43** | SOURCE 9 · **44** | SOURCE 10 · **45** |
| 3 | SOURCE 11 · **46** | SOURCE 12 · **47** | PREV · **48** | NEXT · **49** | Seite 2 |

**Seite 2 · Perform** ![Seite 2](../../streamdeck/layout-page2.png)

| Reihe | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | PRESET 1 · **52** | PRESET 2 · **53** | PRESET 3 · **54** | PRESET 4 · **55** | PRESET 5 · **56** |
| 2 | PRESET 6 · **57** | PRESET 7 · **58** | PRESET 8 · **59** | REC · **CC 20** | PLAY · **CC 21** |
| 3 | UNDO · **CC 22** | CLEAR · **CC 23** | INPUT OFF · **50** | NEXT · **49** | Seite 1 |

Weniger als 12 Quellen? Überzählige Tasten leer lassen – sie melden nur „unknown source“. Extra: Note 60/61 = Rack-Kette zurück/vor.

## 3. Looper-Tasten zuweisen (einmalig, in der Vorlage)
1. **MIDI-Map-Modus** an (⌘ M).
2. Im livelooper-Gerät **Rec** anklicken (ggf. vorher über *Konfigurieren* im Geräte-Header sichtbar machen).
3. Stream-Deck-Taste **REC** drücken. Genauso PLAY, UNDO, CLEAR.
4. ⌘ M aus und Vorlage erneut speichern.

# livelooper companion

*designed by groovex* · [English](README.md)

Wähle während der Performance per Knopfdruck, **welche Spur in livelooper aufgenommen wird** – Synth 1–3, Rhythmus oder Mikro – und schalte **Synth-Presets** (z. B. Pigments) um. Läuft in Ableton Live 12 mit **ClyphX Pro** und wird am einfachsten mit einem **Elgato Stream Deck** (15 Tasten) bedient.

![Stream-Deck-Layout](streamdeck/layout.png)

## Was passiert beim Tastendruck?
`SYNTH 2` →
1. Die LOOPER-Spur bekommt als Eingang **Synth 2 (Post FX)** und Monitor **In**.
2. Synth 2 wird **scharf geschaltet** (dein Keyboard spielt ihn), Synth 1 und 3 werden entschärft.
3. Live zeigt unten in der Statuszeile: `livelooper: recording source -> Synth 2`.

`PRESET 1–4` schicken einen Program Change an den gerade aktiven Synth. `LOOP REC/PLAY/UNDO/CLEAR` steuern livelooper direkt.

## Installation in 3 Schritten
1. **Voraussetzungen:** Ableton Live 12, ClyphX Pro (einmal in *Einstellungen → Link, Tempo & MIDI* als Control Surface gewählt), optional Stream Deck + Plugin *Midi* von Trevliga Spel.
2. **Download** → `install.command` **doppelklicken**. Das Skript kopiert die User Action, trägt Makros und X-Controls in ClyphX Pro ein (mit Backup, mehrfach ausführbar) und legt die Stream-Deck-Icons auf den Schreibtisch. Meldet macOS „nicht verifizierter Entwickler“: Rechtsklick → Öffnen.
3. **Live-Set anlegen** wie in [docs/de/setup.md](docs/de/setup.md) – 6 Spuren, 2 IAC-Ports, fertig.

Stream Deck einrichten: [docs/de/stream-deck.md](docs/de/stream-deck.md) · Presets: [docs/de/presets.md](docs/de/presets.md) · Probleme: [docs/de/troubleshooting.md](docs/de/troubleshooting.md)

Deinstallieren: `uninstall.command` doppelklicken.

## Spurlayout
| # | Name (exakt) | Typ | Eingang | Ausgang |
|---|---|---|---|---|
| 1–3 | `Synth 1`, `Synth 2`, `Synth 3` | MIDI + Instrument | All Ins | Master |
| 4 | `Rhythm` | MIDI/Audio | – | Master |
| 5 | `Mic` | Audio | Ext. In 1 | Master |
| 6 | `LOOPER` | Audio + livelooper | wird vom Skript gesetzt | Master |

Andere Namen? Oben in `clyphx/user_actions/livelooper_companion.py` die Liste `SOURCES` und `LOOPER_TRACK` anpassen und erneut installieren.

## Lizenz
AGPL-3.0 – siehe [LICENSE](LICENSE). ClyphX Pro, Pigments und Stream Deck sind Produkte ihrer jeweiligen Hersteller und nicht Teil dieses Repos.

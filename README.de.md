# livelooper companion

*designed by groovex* · [English](README.md)

Wähle während der Performance per Knopfdruck, **welche Spur in livelooper aufgenommen wird** – bis zu **12 Quellen** (Synths, Rhythmus, Mikro …) – und schalte **Synth-Presets** (z. B. Pigments) um. Läuft in Ableton Live 12 mit **ClyphX Pro** und wird am einfachsten mit einem **Elgato Stream Deck** (15 Tasten) bedient.

| Seite 1 · Quellen | Seite 2 · Perform |
|---|---|
| ![Seite 1](streamdeck/layout-page1.png) | ![Seite 2](streamdeck/layout-page2.png) |

## Was passiert beim Tastendruck?
`SOURCE 2` →
1. Die LOOPER-Spur bekommt als Eingang **Synth 2 (Post FX)** und Monitor **In**.
2. Synth 2 wird **scharf geschaltet** (dein Keyboard spielt ihn), Synth 1 und 3 werden entschärft.
3. Live zeigt unten in der Statuszeile: `livelooper: recording source -> Synth 2`.

`PRESET 1–8` schicken einen Program Change an den gerade aktiven Synth. `LOOP REC/PLAY/UNDO/CLEAR` steuern livelooper direkt.

## Installation in 3 Schritten
1. **Voraussetzungen:** Ableton Live 12, ClyphX Pro (einmal in *Einstellungen → Link, Tempo & MIDI* als Control Surface gewählt), optional Stream Deck + Plugin *Midi* von Trevliga Spel.
2. **Download** → `install.command` **doppelklicken**. Das Skript kopiert die User Action, trägt Makros und X-Controls in ClyphX Pro ein (mit Backup, mehrfach ausführbar) und legt die Stream-Deck-Icons auf den Schreibtisch. Meldet macOS „nicht verifizierter Entwickler“: Rechtsklick → Öffnen.
3. **Vorlage bauen lassen:** in Live einen Clip `[SETUP] LLSETUP 8` starten – die Action legt Synths, Rhythm, Mic und LOOPER an, lädt Pigments und livelooper, dann *Als Vorlage speichern*. Details: [docs/de/setup.md](docs/de/setup.md)

Stream Deck einrichten: [docs/de/stream-deck.md](docs/de/stream-deck.md) · Presets: [docs/de/presets.md](docs/de/presets.md) · Probleme: [docs/de/troubleshooting.md](docs/de/troubleshooting.md)

Deinstallieren: `uninstall.command` doppelklicken.

## Dynamisch: 3 bis 12 Quellen
Alle Spuren **links vom LOOPER** sind automatisch Quellen 1, 2, 3 … (max. 12) in ihrer Reihenfolge. Spur hinzufügen, verschieben oder umbenennen genügt – keine Konfiguration. Spuren, deren Name mit `_` beginnt, und Gruppenspuren werden übersprungen.

| Vorlage | Ergebnis |
|---|---|
| `LLSETUP` | Synth 1–3, Rhythm, Mic, LOOPER (5 Quellen) |
| `LLSETUP 8` | Synth 1–6, Rhythm, Mic, LOOPER |
| `LLSETUP 12` | Synth 1–10, Rhythm, Mic, LOOPER |
| `LLSETUP 8 NOPLUG` | wie oben, ohne Plug-ins zu laden |

## Lizenz
AGPL-3.0 – siehe [LICENSE](LICENSE). ClyphX Pro, Pigments und Stream Deck sind Produkte ihrer jeweiligen Hersteller und nicht Teil dieses Repos.

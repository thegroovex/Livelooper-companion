# Einrichtung

Einmalig ca. 10 Minuten. Am Ende hast du eine Live-Vorlage, mit der jedes neue Set sofort spielbereit ist.

## 1. Zwei virtuelle MIDI-Ports (IAC)
1. **Audio-MIDI-Setup** öffnen (Programme → Dienstprogramme) → *Fenster → MIDI-Studio einblenden*.
2. **IAC-Treiber** doppelklicken → Haken bei **Gerät ist online**.
3. Unter *Ports* mit **+** zwei Ports anlegen: **`LL Deck`** und **`LL Synth`**.

| Port | Wofür |
|---|---|
| `LL Deck` | Stream Deck → Live (Quellwahl, Presets, Looper-Transport) |
| `LL Synth` | ClyphX Pro → Synth-Spuren (Program Change) |

## 2. Live-Einstellungen → Link, Tempo & MIDI
- **Control Surface:** `ClyphX Pro` · **Input:** `IAC-Treiber (LL Deck)` · **Output:** `IAC-Treiber (LL Synth)`
- **MIDI-Ports:**

| Port | Track | Remote |
|---|---|---|
| Eingang `LL Deck` | **aus** | **an** |
| Eingang `LL Synth` | **an** | aus |
| Ausgänge `LL Deck`, `LL Synth` | aus | aus |

*Track aus* bei `LL Deck` ist wichtig – sonst spielen die Tasten Noten in deine Synths.

## 3. Vorlage automatisch bauen
1. **Neues, leeres Live-Set** öffnen (*Datei → Neues Live-Set*).
2. In einer der MIDI-Spuren in einen leeren Clip-Slot doppelklicken → neuer Clip → **⌘ R** → Name: **`[SETUP] LLSETUP 8`** (die Zahl = Anzahl Quellen, 3 bis 12).
3. Clip starten. In Sekunden entstehen:

| Spuren | Einstellung |
|---|---|
| `Synth 1` … `Synth N-2` | MIDI-Spur mit **Pigments** (AU bevorzugt) |
| `Rhythm` | MIDI-Spur – Drum Rack oder Clips nach Wahl |
| `Mic` | Audiospur, Eingang *Ext. In 1*, Monitor *In* |
| `LOOPER` | Audiospur mit **livelooper** |

   Live's leere Standardspuren werden dabei entfernt; Spuren mit Clips oder Geräten bleiben unangetastet. Ist schon ein `LOOPER` da, ändert die Action nichts.
4. Spur mit dem Setup-Clip löschen, dann **Datei → Live-Set als Vorlage speichern**.

Findet die Action ein Plug-in nicht, steht das in der Statuszeile – dann einfach von Hand laden. `LLSETUP 8 NOPLUG` legt nur die Spuren an.

## 4. Mehr oder weniger Quellen (dynamisch)
Alle Spuren **links vom LOOPER** sind Quellen – in ihrer Reihenfolge, maximal 12. Neue Synth-Spur links vom LOOPER einfügen = neue Quelle. Name mit `_` am Anfang (z. B. `_Click`) oder Gruppenspur = wird übersprungen. Feste Liste statt Automatik: oben in `clyphx/user_actions/livelooper_companion.py` `SOURCES = ['Synth 1', 'Bass', 'Mic']` setzen und neu installieren.

## 5. Nichts doppelt hören
Die Quelle läuft über ihre eigene Spur in den Master **und** in den LOOPER. Wenn livelooper sein Eingangssignal durchschleift, hörst du sie doppelt:
- **A (empfohlen):** In livelooper das Durchschleifen des Eingangs ausschalten.
- **B:** Ausgang der Quellspuren auf *Sends Only* – dann hörst du nur die gewählte Quelle (über livelooper).

## 6. Test
Taste **SOURCE 1** drücken. Unten in Live steht `livelooper: recording source -> Synth 1 (1/8)`, Synth 1 ist scharf, der LOOPER zeigt *Synth 1 · Post FX* als Eingang.

### Ohne Stream Deck
Jeder Pad-Controller geht: Noten auf **Kanal 16** senden (Belegung in [stream-deck.md](stream-deck.md)) und ihn als *Input* von ClyphX Pro wählen. Oder X-Clips, z. B. `[S1] $LL_SRC1$`.

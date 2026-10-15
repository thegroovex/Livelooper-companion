# Einrichtung (Live-Set)

Dauer: ca. 10 Minuten, nur einmal nötig. Danach als Vorlage speichern (*Datei → Live-Set als Vorlage speichern*).

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

## 3. Spuren anlegen (Namen exakt so)
| # | Name | Einstellung |
|---|---|---|
| 1–3 | `Synth 1`, `Synth 2`, `Synth 3` | MIDI-Spur, Instrument (z. B. Pigments), Eingang *All Ins / All Channels*, Monitor *Auto*, Ausgang *Master* |
| 4 | `Rhythm` | Drum Rack, Clips oder Audio – läuft einfach, Ausgang *Master* |
| 5 | `Mic` | Audiospur, Eingang *Ext. In 1* (dein Mikro), Monitor *In*, Ausgang *Master* |
| 6 | `LOOPER` | Audiospur mit **livelooper**, Ausgang *Master*. Eingang/Monitor setzt das Skript. |

## 4. Nichts doppelt hören
Die Quelle läuft über ihre eigene Spur in den Master **und** in den LOOPER. Wenn livelooper sein Eingangssignal durchschleift, hörst du sie doppelt. Zwei Wege:
- **A (empfohlen):** In livelooper das Durchschleifen des Eingangs ausschalten – du hörst die Quelle über ihre Spur, die Loops über den LOOPER.
- **B:** Ausgang der Spuren 1–5 auf *Sends Only* – dann hörst du nur die gerade gewählte Quelle (über livelooper), die anderen sind stumm.

## 5. Test
Taste **SYNTH 1** drücken (oder X-Control Note 36, Kanal 16). Unten in Live steht `livelooper: recording source -> Synth 1`, Synth 1 ist scharf, der LOOPER zeigt *Synth 1 · Post FX* als Eingang.

### Ohne Stream Deck
Jeder Pad-Controller geht: Noten 36–53 auf **Kanal 16** senden und den Controller als *Input* von ClyphX Pro wählen. Oder X-Clips in einer leeren Spur, z. B. ein Clip namens `[S1] $LL_SYN1$`.

### Andere Spurnamen
Oben in `clyphx/user_actions/livelooper_companion.py` `SOURCES` und `LOOPER_TRACK` ändern, `install.command` erneut starten, Live neu starten.

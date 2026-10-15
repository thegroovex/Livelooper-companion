# Probleme lösen

| Symptom | Lösung |
|---|---|
| Tastendruck macht nichts | ClyphX Pro als Control Surface gewählt? Input = `LL Deck`? Nach der Installation Live neu gestartet? |
| Stream-Deck-Tasten spielen Noten im Synth | Bei Eingang `LL Deck` *Track* ausschalten. |
| Statuszeile: `track "LOOPER" not found` | Spur exakt `LOOPER` nennen (Groß-/Kleinschreibung). |
| `"Synth 1" not offered as input` | Quelle muss Audio ausgeben (Instrument geladen) und darf nicht der LOOPER selbst sein. Namen prüfen. |
| Mikro wird nicht aufgenommen | `Mic` Monitor *In*, richtiger Eingang, Pegel an der Spur sichtbar? |
| Ich höre die Quelle doppelt | Siehe *Nichts doppelt hören* in setup.md. |
| Preset wechselt nicht | Pigments als AU/VST2 statt VST3; Playlist angelegt; Synth-Spur scharf; `LL Synth` Eingang *Track* an; ClyphX Output = `LL Synth`. |
| Ohne User Action arbeiten | In `X-Controls` `$LL_SYN1$` durch `$LLB_SYN1$` usw. ersetzen – nutzt nur eingebaute ClyphX-Actions. |

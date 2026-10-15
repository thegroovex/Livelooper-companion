#!/bin/bash
# livelooper companion – installer (macOS). Double-click me. / Doppelklick.
# designed by groovex · AGPL-3.0
set -euo pipefail
cd "$(dirname "$0")"

UL="${ABLETON_USER_LIBRARY:-$HOME/Music/Ableton/User Library}"
CX="${CLYPHX_SETTINGS:-$HOME/nativeKONTROL/ClyphX_Pro}"
BEGIN="# >>> livelooper companion >>>"
END="# <<< livelooper companion <<<"

say() { printf '\033[1m%s\033[0m\n' "$*"; }
fail() { printf '\033[31m%s\033[0m\n' "$*"; read -r -p "Enter …" _ || true; exit 1; }

say "livelooper companion – Installation"

[ -d "$UL" ] || fail "Ableton User Library not found / nicht gefunden: $UL
Set ABLETON_USER_LIBRARY or open Live once. / Live einmal starten."

[ -d "$CX" ] || fail "ClyphX Pro settings folder missing / ClyphX-Pro-Ordner fehlt: $CX
Select ClyphX Pro once as Control Surface in Live (Settings > Link, Tempo & MIDI), then run again.
ClyphX Pro einmal in Live als Control Surface wählen und erneut starten."

# 1) User Action
UA="$UL/Remote Scripts/_user_actions"
mkdir -p "$UA"
cp clyphx/user_actions/livelooper_companion.py "$UA/"
say "✓ User Action -> $UA"

# 2) merge our block into a ClyphX settings file (idempotent, with backup)
merge() {
  local src="$1" dst="$2"
  touch "$dst"
  cp "$dst" "$dst.bak-livelooper"
  awk -v b="$BEGIN" -v e="$END" '
    $0==b {skip=1; next}
    $0==e {skip=0; next}
    !skip {print}' "$dst.bak-livelooper" > "$dst.tmp"
  { cat "$dst.tmp"; echo "$BEGIN"; grep -v '^[[:space:]]*$' "$src" | sed 's/\r$//'; echo "$END"; } > "$dst"
  rm -f "$dst.tmp"
  say "✓ $(basename "$dst") (Backup: $(basename "$dst").bak-livelooper)"
}
merge clyphx/Macros.txt     "$CX/Macros.txt"
merge clyphx/X-Controls.txt "$CX/X-Controls.txt"

# 3) Stream Deck icons next to the user's Desktop for drag & drop
if [ "${SKIP_ICONS:-0}" != "1" ]; then
  ICONS="$HOME/Desktop/livelooper Stream Deck Icons"
  mkdir -p "$ICONS"
  cp streamdeck/icons/*.png "$ICONS/" 2>/dev/null || true
  say "✓ Stream Deck icons -> $ICONS"
fi

say ""
say "Fertig / Done. Restart Live (or run the ClyphX action RELOAD)."
say "Next / Weiter: docs/de/setup.md · docs/en/setup.md"
[ "${CI:-}" = "true" ] || read -r -p "Enter …" _ || true

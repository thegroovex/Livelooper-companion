#!/bin/bash
# livelooper companion – uninstall (macOS) / deinstallieren
set -euo pipefail
UL="${ABLETON_USER_LIBRARY:-$HOME/Music/Ableton/User Library}"
CX="${CLYPHX_SETTINGS:-$HOME/nativeKONTROL/ClyphX_Pro}"
BEGIN="# >>> livelooper companion >>>"; END="# <<< livelooper companion <<<"
rm -f "$UL/Remote Scripts/_user_actions/livelooper_companion.py"
for f in "$CX/Macros.txt" "$CX/X-Controls.txt"; do
  [ -f "$f" ] || continue
  awk -v b="$BEGIN" -v e="$END" '$0==b{s=1;next} $0==e{s=0;next} !s{print}' "$f" > "$f.tmp" && mv "$f.tmp" "$f"
done
echo "Removed / entfernt. Restart Live."
[ "${CI:-}" = "true" ] || read -r -p "Enter …" _ || true

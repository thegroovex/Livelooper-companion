#!/bin/bash
# Installer test in a throwaway HOME: install twice (idempotent), then uninstall.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
T="$(mktemp -d)"; export HOME="$T" CI=true SKIP_ICONS=1
mkdir -p "$T/Music/Ableton/User Library" "$T/nativeKONTROL/ClyphX_Pro"
echo '$MINE$ = METRO' > "$T/nativeKONTROL/ClyphX_Pro/Macros.txt"
bash "$ROOT/install.command" >/dev/null
bash "$ROOT/install.command" >/dev/null
M="$T/nativeKONTROL/ClyphX_Pro/Macros.txt"
[ "$(grep -c '>>> livelooper companion >>>' "$M")" = 1 ] || { echo "block duplicated"; exit 1; }
grep -q '^\$MINE\$ = METRO' "$M" || { echo "user macro lost"; exit 1; }
grep -q 'LLSRC 1' "$M"
[ -f "$T/Music/Ableton/User Library/Remote Scripts/_user_actions/livelooper_companion.py" ]
grep -q 'LL_SRC1 = NOTE, 16, 36' "$T/nativeKONTROL/ClyphX_Pro/X-Controls.txt"
bash "$ROOT/uninstall.command" >/dev/null
! grep -q 'livelooper' "$M"
grep -q '^\$MINE\$ = METRO' "$M"
echo "install test ok"

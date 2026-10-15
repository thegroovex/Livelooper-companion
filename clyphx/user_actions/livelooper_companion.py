# -*- coding: utf-8 -*-
"""
livelooper companion – ClyphX Pro User Actions
designed by groovex · AGPL-3.0

Routes exactly one source track (synth, rhythm, mic …) into the livelooper
track, arms it if it is a MIDI track and leaves the others disarmed.

Install: copy this file to
    ~/Music/Ableton/User Library/Remote Scripts/_user_actions/
(or ClyphX_Pro/clyphx_pro/user_actions inside the User Library) and restart Live.

Actions (global):
    LLSRC 1            -> source no. 1 from SOURCES
    LLSRC "Synth 2"    -> source by track name
    LLSRC >  / LLSRC < -> next / previous source
    LLSRC OFF          -> looper input = No Input (nothing gets recorded)
    LLSRC ?            -> show the active source in Live's status bar

---------------------------------------------------------------------------
DE: Routet genau eine Quellspur (Synth, Rhythmus, Mikro …) in die livelooper-
Spur, armt sie (bei MIDI-Spuren) und disarmt die anderen.
Kopieren nach: ~/Music/Ableton/User Library/Remote Scripts/_user_actions/
"""

from ClyphX_Pro.clyphx_pro.UserActionsBase import UserActionsBase

# ------------------------------------------------------------------ config --
# Track names exactly as in your Live Set (case-sensitive).
# Spurnamen exakt wie im Live-Set (Groß-/Kleinschreibung beachten).
LOOPER_TRACK = 'LOOPER'
SOURCES = ['Synth 1', 'Synth 2', 'Synth 3', 'Rhythm', 'Mic']

# Tap point on the source track: 'Post FX', 'Pre FX' or 'Post Mixer'.
TAP_POINT = 'Post FX'

# Arm the selected MIDI source and disarm the other sources.
EXCLUSIVE_ARM = True

# Audio sources (e.g. the mic) are kept on monitor "In" so their signal
# always reaches the looper, even when not armed.
FORCE_AUDIO_MONITOR_IN = True

MONITOR_IN = 0  # Live API: 0 = In, 1 = Auto, 2 = Off
# ---------------------------------------------------------------------------


class LivelooperCompanionActions(UserActionsBase):

    def create_actions(self):
        self._current = None
        self.add_global_action('llsrc', self.select_source)

    # ---------------------------------------------------------------- utils
    def _msg(self, text):
        self.canonical_parent.show_message('livelooper: ' + text)

    def _track(self, name):
        for t in self.song().tracks:
            if t.name == name:
                return t
        return None

    @staticmethod
    def _pick(options, wanted):
        """Return the routing option whose display_name matches `wanted`.
        Live shows tracks as 'Synth 1' or '2-Synth 1' depending on version,
        so exact match wins, then a '-<name>' suffix match."""
        for o in options:
            if o.display_name == wanted:
                return o
        for o in options:
            if o.display_name.endswith('-' + wanted):
                return o
        return None

    def _resolve(self, arg):
        arg = arg.strip()
        if not arg:
            return None
        if arg in ('>', '<'):
            idx = SOURCES.index(self._current) if self._current in SOURCES else -1
            step = 1 if arg == '>' else -1
            return SOURCES[(idx + step) % len(SOURCES)]
        if arg.isdigit():
            n = int(arg) - 1
            return SOURCES[n] if 0 <= n < len(SOURCES) else None
        name = arg.strip('"')
        return name if self._track(name) is not None else None

    # --------------------------------------------------------------- action
    def select_source(self, action_def, args):
        looper = self._track(LOOPER_TRACK)
        if looper is None:
            self._msg('track "%s" not found' % LOOPER_TRACK)
            return

        arg = (args or '').strip()
        if arg == '?':
            self._msg('source = %s' % (self._current or 'none'))
            return

        if arg.upper() == 'OFF':
            off = self._pick(looper.available_input_routing_types, 'No Input')
            if off is not None:
                looper.input_routing_type = off
            self._current = None
            self._msg('input off')
            return

        name = self._resolve(arg)
        if name is None:
            self._msg('unknown source "%s"' % arg)
            return
        src = self._track(name)
        if src is None:
            self._msg('track "%s" not found' % name)
            return

        # 1) looper input <- source track
        rtype = self._pick(looper.available_input_routing_types, name)
        if rtype is None:
            self._msg('"%s" not offered as input of %s' % (name, LOOPER_TRACK))
            return
        looper.input_routing_type = rtype

        # 2) tap point (Post FX / Pre FX / Post Mixer)
        chan = self._pick(looper.available_input_routing_channels, TAP_POINT)
        if chan is not None:
            looper.input_routing_channel = chan

        # 3) looper must monitor its input so livelooper hears it
        looper.current_monitoring_state = MONITOR_IN

        # 4) arm the chosen synth, disarm the others
        for sname in SOURCES:
            t = self._track(sname)
            if t is None:
                continue
            if FORCE_AUDIO_MONITOR_IN and not t.has_midi_input:
                t.current_monitoring_state = MONITOR_IN
            if EXCLUSIVE_ARM and t.can_be_armed and t.has_midi_input:
                t.arm = (t == src)

        self._current = name
        self._msg('recording source -> %s' % name)

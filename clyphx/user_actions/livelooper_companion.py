# -*- coding: utf-8 -*-
"""
livelooper companion - ClyphX Pro User Actions
designed by groovex - AGPL-3.0

LLSRC   - route exactly one source track into the livelooper track
LLSETUP - build the whole template set (sources + Mic + LOOPER) in one go

Install: install.command copies this file to
    ~/Music/Ableton/User Library/Remote Scripts/_user_actions/

LLSRC 1 .. LLSRC 12   source by number (tracks left of LOOPER, in order)
LLSRC "Synth 2"       source by track name
LLSRC > / LLSRC <     next / previous source
LLSRC OFF             looper input = No Input
LLSRC ?               show the active source in Live's status bar

LLSETUP               3 synths + Rhythm + Mic + LOOPER (= 5 sources)
LLSETUP 10            8 synths + Rhythm + Mic + LOOPER (8 to 12 sources)
LLSETUP 10 NOPLUG     same, without loading Pigments / livelooper

---------------------------------------------------------------------------
DE: LLSRC routet genau eine Quellspur in die livelooper-Spur, LLSETUP baut
die komplette Vorlage (Quellen + Mic + LOOPER). Quellen sind automatisch
alle Spuren links vom LOOPER (max. 12) - Spuren hinzufuegen genuegt.
"""

import re

from ClyphX_Pro.clyphx_pro.UserActionsBase import UserActionsBase

try:
    import Live  # only available inside Ableton Live
except ImportError:  # tests
    Live = None

# ------------------------------------------------------------------ config --
LOOPER_TRACK = 'LOOPER'

# None = automatic: every track LEFT of LOOPER is a source (max MAX_SOURCES).
#        Tracks whose name starts with '_' and group tracks are skipped.
# Or a fixed list, e.g. ['Synth 1', 'Synth 2', 'Bass', 'Mic'].
# None = automatisch: alle Spuren links vom LOOPER (Name mit '_' = ignoriert).
SOURCES = None
MAX_SOURCES = 12

TAP_POINT = 'Post FX'          # 'Post FX', 'Pre FX' or 'Post Mixer'
EXCLUSIVE_ARM = True           # arm only the chosen MIDI source
FORCE_AUDIO_MONITOR_IN = True  # audio sources (mic) stay on monitor In

# LLSETUP
SYNTH_PLUGIN = 'Pigments'      # loaded on every synth track ('' = none)
LOOPER_PLUGIN = 'livelooper'   # loaded on the LOOPER track
PREFER_FORMAT = 'Audio Units'  # AU passes Program Change in Live (VST3 not)
MIC_INPUT = ('Ext. In', '1')   # input type and channel for the Mic track
DEFAULT_SOURCES = 5

MONITOR_IN = 0  # Live API: 0 = In, 1 = Auto, 2 = Off
# ---------------------------------------------------------------------------


def _pick(options, wanted):
    """Routing option matching `wanted`: exact display_name first, then the
    '<n>-<name>' form some Live versions use for tracks."""
    for o in options:
        if o.display_name == wanted:
            return o
    for o in options:
        if o.display_name.endswith('-' + wanted):
            return o
    return None


class LivelooperCompanionActions(UserActionsBase):

    def create_actions(self):
        self._current = None
        self.add_global_action('llsrc', self.select_source)
        self.add_global_action('llsetup', self.setup_set)

    # ---------------------------------------------------------------- utils
    def _msg(self, text):
        self.canonical_parent.show_message('livelooper: ' + text)

    def _track(self, name):
        for t in self.song().tracks:
            if t.name == name:
                return t
        return None

    def sources(self):
        """Names of the source tracks, in order."""
        if SOURCES:
            return [n for n in SOURCES if self._track(n) is not None][:MAX_SOURCES]
        names = []
        for t in self.song().tracks:
            if t.name == LOOPER_TRACK:
                break
            if t.name.startswith('_') or getattr(t, 'is_foldable', False):
                continue
            names.append(t.name)
        return names[:MAX_SOURCES]

    def _resolve(self, arg, srcs):
        if not arg or not srcs:
            return None
        if arg in ('>', '<'):
            idx = srcs.index(self._current) if self._current in srcs else -1
            return srcs[(idx + (1 if arg == '>' else -1)) % len(srcs)]
        if arg.isdigit():
            n = int(arg) - 1
            return srcs[n] if 0 <= n < len(srcs) else None
        name = arg.strip('"')
        return name if name in srcs else None

    # ---------------------------------------------------------------- LLSRC
    def select_source(self, action_def, args):
        looper = self._track(LOOPER_TRACK)
        if looper is None:
            self._msg('track "%s" not found' % LOOPER_TRACK)
            return
        arg = (args or '').strip()
        srcs = self.sources()

        if arg == '?':
            self._msg('source = %s (%d sources)' % (self._current or 'none', len(srcs)))
            return
        if arg.upper() == 'OFF':
            off = _pick(looper.available_input_routing_types, 'No Input')
            if off is not None:
                looper.input_routing_type = off
            self._current = None
            self._msg('input off')
            return

        name = self._resolve(arg, srcs)
        if name is None:
            self._msg('unknown source "%s" (%d sources)' % (arg, len(srcs)))
            return
        src = self._track(name)

        rtype = _pick(looper.available_input_routing_types, name)
        if rtype is None:
            self._msg('"%s" not offered as input of %s' % (name, LOOPER_TRACK))
            return
        looper.input_routing_type = rtype
        chan = _pick(looper.available_input_routing_channels, TAP_POINT)
        if chan is not None:
            looper.input_routing_channel = chan
        looper.current_monitoring_state = MONITOR_IN

        for sname in srcs:
            t = self._track(sname)
            if FORCE_AUDIO_MONITOR_IN and not t.has_midi_input:
                t.current_monitoring_state = MONITOR_IN
            if EXCLUSIVE_ARM and t.can_be_armed and t.has_midi_input:
                t.arm = (t == src)

        self._current = name
        self._msg('recording source -> %s (%d/%d)' % (name, srcs.index(name) + 1, len(srcs)))

    # -------------------------------------------------------------- LLSETUP
    def _new_track(self, midi, name):
        song = self.song()
        idx = len(song.tracks)
        if midi:
            song.create_midi_track(idx)
        else:
            song.create_audio_track(idx)
        t = song.tracks[idx]
        t.name = name
        return t

    _DEFAULT_NAME = re.compile(r'^(\d+-)?(MIDI|Audio)$')

    def _remove_empty_default_tracks(self):
        """Delete Live's untouched default tracks ('1-MIDI', '3-Audio' ...):
        only when they have no devices and no clips."""
        song, removed = self.song(), 0
        for i in range(len(song.tracks) - 1, -1, -1):
            t = song.tracks[i]
            if not self._DEFAULT_NAME.match(t.name) or len(t.devices):
                continue
            if any(cs.has_clip for cs in t.clip_slots):
                continue
            song.delete_track(i)
            removed += 1
        return removed

    def _find_plugin(self, wanted):
        """Search Live's plug-in browser; prefer PREFER_FORMAT."""
        if Live is None or not wanted:
            return None
        browser = Live.Application.get_application().browser
        hits = []

        def walk(item, path, depth):
            if depth > 6:
                return
            for child in item.children:
                p = path + '/' + child.name
                if child.is_loadable and child.name.lower().startswith(wanted.lower()):
                    hits.append((p, child))
                elif child.is_folder or not child.is_loadable:
                    walk(child, p, depth + 1)

        walk(browser.plugins, '', 0)
        if not hits:
            return None
        hits.sort(key=lambda h: (PREFER_FORMAT.lower() not in h[0].lower(), len(h[0])))
        return hits[0][1]

    def _load(self, track, item):
        if item is None:
            return False
        self.song().view.selected_track = track
        Live.Application.get_application().browser.load_item(item)
        return True

    def setup_set(self, action_def, args):
        parts = (args or '').split()
        n = DEFAULT_SOURCES
        if parts and parts[0].isdigit():
            n = int(parts[0])
        n = max(3, min(MAX_SOURCES, n))
        plugins = 'NOPLUG' not in [p.upper() for p in parts]

        if self._track(LOOPER_TRACK) is not None:
            self._msg('set already has a %s track - nothing changed' % LOOPER_TRACK)
            return

        synths = n - 2
        synth_tracks = [self._new_track(True, 'Synth %d' % (i + 1)) for i in range(synths)]
        self._new_track(True, 'Rhythm')
        mic = self._new_track(False, 'Mic')
        itype = _pick(mic.available_input_routing_types, MIC_INPUT[0])
        if itype is not None:
            mic.input_routing_type = itype
            ich = _pick(mic.available_input_routing_channels, MIC_INPUT[1])
            if ich is not None:
                mic.input_routing_channel = ich
        mic.current_monitoring_state = MONITOR_IN
        looper = self._new_track(False, LOOPER_TRACK)
        removed = self._remove_empty_default_tracks()

        missing = []
        if plugins:
            synth = self._find_plugin(SYNTH_PLUGIN)
            for t in synth_tracks:
                if not self._load(t, synth):
                    missing.append(SYNTH_PLUGIN)
                    break
            if not self._load(looper, self._find_plugin(LOOPER_PLUGIN)):
                missing.append(LOOPER_PLUGIN)

        msg = 'set ready: %d sources + %s' % (n, LOOPER_TRACK)
        if removed:
            msg += ', %d empty default tracks removed' % removed
        if missing:
            msg += ' (load manually: %s)' % ', '.join(missing)
        self._msg(msg + ' - now File > Save Live Set as Template')

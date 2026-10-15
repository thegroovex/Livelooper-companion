"""Tests for the LLSRC user action with a fake Live API (no Live needed)."""
import importlib, sys, types, unittest
from pathlib import Path

# fake ClyphX_Pro.clyphx_pro.UserActionsBase
base = types.ModuleType("ClyphX_Pro.clyphx_pro.UserActionsBase")
class UserActionsBase:
    def __init__(self, song):
        self._song, self.actions, self.messages = song, {}, []
        self.canonical_parent = types.SimpleNamespace(show_message=self.messages.append)
        self.create_actions()
    def song(self): return self._song
    def add_global_action(self, name, fn): self.actions[name] = fn
base.UserActionsBase = UserActionsBase
for n in ("ClyphX_Pro", "ClyphX_Pro.clyphx_pro"):
    sys.modules[n] = types.ModuleType(n)
sys.modules["ClyphX_Pro.clyphx_pro.UserActionsBase"] = base
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "clyphx" / "user_actions"))
mod = importlib.import_module("livelooper_companion")

class Opt:
    def __init__(self, n): self.display_name = n

class Slot:
    def __init__(self, has): self.has_clip = has

class Song:
    def __init__(self): self.tracks = []; self.view = types.SimpleNamespace(selected_track=None)
    def _refresh(self):
        names = [t.name for t in self.tracks]
        for t in self.tracks:
            t.available_input_routing_types = [Opt("No Input"), Opt("Ext. In")] + [
                Opt(f"{i+1}-{n}") for i, n in enumerate(names) if n != t.name]
    def create_midi_track(self, i): self.tracks.insert(i, Track("MIDI", True)); self._refresh()
    def create_audio_track(self, i): self.tracks.insert(i, Track("Audio", False)); self._refresh()
    def delete_track(self, i): del self.tracks[i]; self._refresh()

class Track:
    def __init__(self, name, midi):
        self.name, self.has_midi_input, self.can_be_armed = name, midi, True
        self.arm, self.current_monitoring_state, self.is_foldable = False, 1, False
        self.devices, self.clip_slots = [], [Slot(False)]
        self.available_input_routing_types = []
        self.available_input_routing_channels = [Opt("Pre FX"), Opt("Post FX"), Opt("Post Mixer"), Opt("1"), Opt("1/2")]
        self.input_routing_type = self.input_routing_channel = None

def make(names=("Synth 1", "Synth 2", "Synth 3", "Rhythm", "Mic")):
    song = Song()
    for n in list(names) + ["LOOPER"]:
        song.tracks.append(Track(n, n not in ("Mic", "LOOPER")))
    song._refresh()
    ua = mod.LivelooperCompanionActions(song)
    return ua, song.tracks[:-1], song.tracks[-1]

class T(unittest.TestCase):
    def run_action(self, ua, arg, name="llsrc"): ua.actions[name]({}, arg)

    def test_select_by_number(self):
        ua, tr, lp = make(); self.run_action(ua, "2")
        self.assertEqual(lp.input_routing_type.display_name, "2-Synth 2")
        self.assertEqual(lp.input_routing_channel.display_name, "Post FX")
        self.assertEqual(lp.current_monitoring_state, 0)
        self.assertEqual([t.arm for t in tr[:3]], [False, True, False])

    def test_mic_stays_monitor_in(self):
        ua, tr, lp = make(); self.run_action(ua, '"Mic"')
        self.assertEqual(lp.input_routing_type.display_name, "5-Mic")
        self.assertEqual(tr[4].current_monitoring_state, 0)
        self.assertFalse(any(t.arm for t in tr[:4]))

    def test_next_prev_wrap(self):
        ua, tr, lp = make()
        self.run_action(ua, "5"); self.run_action(ua, ">")
        self.assertEqual(lp.input_routing_type.display_name, "1-Synth 1")
        self.run_action(ua, "<")
        self.assertEqual(lp.input_routing_type.display_name, "5-Mic")

    def test_off(self):
        ua, tr, lp = make(); self.run_action(ua, "1"); self.run_action(ua, "OFF")
        self.assertEqual(lp.input_routing_type.display_name, "No Input")

    def test_unknown_source_is_harmless(self):
        ua, tr, lp = make(); self.run_action(ua, "9")
        self.assertIsNone(lp.input_routing_type)
        self.assertIn("unknown", ua.messages[-1])

    def test_twelve_sources_auto(self):
        ua, tr, lp = make([f"Synth {i}" for i in range(1, 11)] + ["Rhythm", "Mic", "Extra"])
        self.assertEqual(len(ua.sources()), 12)
        self.run_action(ua, "12")
        self.assertEqual(lp.input_routing_type.display_name, "12-Mic")

    def test_underscore_and_groups_skipped(self):
        ua, tr, lp = make(["_Click", "Synth 1", "Mic"])
        self.assertEqual(ua.sources(), ["Synth 1", "Mic"])

    def test_setup_builds_template(self):
        song = Song()
        for n, m in (("1-MIDI", True), ("2-MIDI", True), ("3-Audio", False), ("4-Audio", False)):
            song.tracks.append(Track(n, m))
        ua = mod.LivelooperCompanionActions(song)
        self.run_action(ua, "10 NOPLUG", "llsetup")
        names = [t.name for t in song.tracks]
        self.assertEqual(names, [f"Synth {i}" for i in range(1, 9)] + ["Rhythm", "Mic", "LOOPER"])
        mic = song.tracks[9]
        self.assertEqual(mic.input_routing_type.display_name, "Ext. In")
        self.assertEqual(mic.current_monitoring_state, 0)
        self.assertEqual(len(ua.sources()), 10)

    def test_setup_keeps_used_tracks_and_is_idempotent(self):
        song = Song(); t = Track("1-MIDI", True); t.clip_slots = [Slot(True)]; song.tracks.append(t)
        ua = mod.LivelooperCompanionActions(song)
        self.run_action(ua, "", "llsetup"); n = len(song.tracks)
        self.assertEqual(song.tracks[0].name, "1-MIDI")
        self.run_action(ua, "", "llsetup")
        self.assertEqual(len(song.tracks), n)

if __name__ == "__main__":
    unittest.main()

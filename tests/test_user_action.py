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

class Track:
    def __init__(self, name, midi, names=()):
        self.name, self.has_midi_input, self.can_be_armed = name, midi, True
        self.arm, self.current_monitoring_state = False, 1
        self.available_input_routing_types = [Opt("No Input")] + [Opt(f"{i+1}-{n}") for i, n in enumerate(names)]
        self.available_input_routing_channels = [Opt("Pre FX"), Opt("Post FX"), Opt("Post Mixer")]
        self.input_routing_type = self.input_routing_channel = None

def make():
    names = mod.SOURCES
    tracks = [Track(n, n != "Mic" and n != "Rhythm") for n in names]
    looper = Track("LOOPER", False, names)
    song = types.SimpleNamespace(tracks=tracks + [looper])
    ua = mod.LivelooperCompanionActions(song)
    return ua, tracks, looper

class T(unittest.TestCase):
    def run_action(self, ua, arg): ua.actions["llsrc"]({}, arg)

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
        self.assertFalse(any(t.arm for t in tr[:3]))

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

    def test_exact_name_match(self):
        ua, tr, lp = make()
        lp.available_input_routing_types.append(Opt("Synth 3"))
        self.run_action(ua, "3")
        self.assertEqual(lp.input_routing_type.display_name, "Synth 3")

if __name__ == "__main__":
    unittest.main()

import unittest

from PyQt5 import QtWidgets

from omni_checklist.checklist_data import AIRCRAFT, CHECKLISTS
from omni_checklist.emergency_data import EMERGENCY_CHECKLISTS, DEMONSTRATOR_EMERGENCY_CHECKLISTS
from omni_checklist.screens import ChecklistScreen


class ProcedureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])

    def test_trainer_follows_afm_normal_sequence(self):
        sections = CHECKLISTS["trainer"]
        self.assertEqual(list(sections), [
            "Preflight / GCS", "Before Start", "Start & Takeoff",
            "Mission / Cruise", "Before Landing", "After Landing",
        ])
        start = [item.text for item in sections["Start & Takeoff"]]
        for earlier, later in [
            ("CHT: AT LEAST 100 C BEFORE RUN-UP", "FULL THROTTLE: 3-5 S; 7,100 +/- 200 RPM"),
            ("BRAKE 1 HOLD: 3,000-4,000 RPM", "BRAKE 2 HOLD: 5,000-6,000 RPM"),
            ("PARACHUTE SAFETY PIN: REMOVED", "TOWER: TAKEOFF CLEARANCE RECEIVED"),
            ("TOWER: TAKEOFF CLEARANCE RECEIVED", "TAKEOFF: 3, 2, 1; SELECT AUTO"),
        ]:
            self.assertLess(start.index(earlier), start.index(later))
        landing = [item.text for item in sections["Before Landing"]]
        self.assertIn("HANDOVER: ALIGNED; AT OR ABOVE 100 FT AGL", landing)
        shutdown = [item.text for item in sections["After Landing"]]
        self.assertLess(shutdown.index("RPM ZERO / PROP STOPPED: CONFIRMED"), shutdown.index("AIRCRAFT: DISARMED"))

    def test_emergency_thresholds_and_conditions(self):
        battery = [item.text for item in EMERGENCY_CHECKLISTS["Low / Critical Battery (3S)"]]
        engine = [item.text for item in EMERGENCY_CHECKLISTS["Engine Failure (Flight)"]]
        self.assertTrue(any("10.5 V" in text for text in battery))
        self.assertTrue(any("9.9 V" in text for text in battery))
        self.assertTrue(any("GPS VALID" in text and "RTL" in text for text in battery))
        self.assertTrue(any("40-42 KT" in text for text in engine))
        self.assertTrue(any("MAX 3 COMMANDS; 2 ATTEMPTS EACH" in text for text in engine))
        self.assertTrue(any("ABOVE 150 FT AGL" in text for text in engine))

    def test_emergency_access_is_immediate_and_normal_state_survives(self):
        screen = ChecklistScreen(AIRCRAFT["trainer"])
        screen.rows[0].set_checked(True)
        screen._toggle_mode()
        self.assertEqual(screen.mode, "emergency")
        self.assertTrue(screen._can_open_section("Engine Failure (Flight)"))
        screen._load_section("Engine Failure (Flight)")
        self.assertEqual(screen.current_section, "Engine Failure (Flight)")
        screen._toggle_mode()
        self.assertEqual(screen.mode, "normal")
        self.assertTrue(screen.rows[0].is_checked())

    def test_emergency_navigation_scrolls_without_overlapping_buttons(self):
        screen = ChecklistScreen(AIRCRAFT["trainer"])
        screen.resize(1366, 768)
        screen.show()
        screen._toggle_mode()
        self.app.processEvents()
        screen.nav_layout.activate()
        buttons = list(screen.nav_buttons.values())
        self.assertGreater(screen.nav_scroll.verticalScrollBar().maximum(), 0)
        self.assertTrue(all(
            later.y() >= earlier.y() + earlier.height()
            for earlier, later in zip(buttons, buttons[1:])
        ), [(button.text(), button.y(), button.height()) for button in buttons])

    def test_demonstrator_uses_electric_6s_procedures(self):
        screen = ChecklistScreen(AIRCRAFT["demonstrator"])
        self.assertEqual(screen.section_order[0], "Preflight / GCS")
        self.assertTrue(hasattr(screen, "mode_btn"))
        normal = [item.text for section in CHECKLISTS["demonstrator"].values() for item in section]
        emergency = [item.text for section in DEMONSTRATOR_EMERGENCY_CHECKLISTS.values() for item in section]
        combined = " ".join(normal + emergency).upper()
        for forbidden in ("PARACHUTE", "FUEL", "CHT", "3S", "ENGINE", "BRAKE"):
            self.assertNotIn(forbidden, combined)
        self.assertIn("MOTOR", combined)
        self.assertIn("6S", combined)
        self.assertIn("6S BATTERY BELOW 22.0 V: PREPARE TO LAND", normal)
        self.assertIn("AT 21.0 V: LOW VOLTAGE; END MISSION", emergency)
        self.assertIn("AT 18.0 V: CRITICAL; LAND AT SAFE AREA", emergency)

    def test_demonstrator_emergency_is_accessible_without_normal_completion(self):
        screen = ChecklistScreen(AIRCRAFT["demonstrator"])
        screen.rows[0].set_checked(True)
        screen._toggle_mode()
        self.assertTrue(screen._can_open_section("Motor Power Loss (Flight)"))
        screen._load_section("Motor Power Loss (Flight)")
        self.assertEqual(screen.current_section, "Motor Power Loss (Flight)")
        screen._toggle_mode()
        self.assertTrue(screen.rows[0].is_checked())

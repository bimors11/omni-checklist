import unittest

from PyQt5 import QtCore, QtTest, QtWidgets

from omni_checklist.checklist_data import AIRCRAFT, CHECKLISTS
from omni_checklist.main_window import MainWindow
from omni_checklist.screens import ChecklistScreen
from omni_checklist.widgets import INSTRUCTION_KINDS, instruction_kind


class ChecklistTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])

    def test_aircraft_session_is_preserved(self):
        window = MainWindow()
        window._open_aircraft("trainer")
        session = window.current_checklist
        session.rows[0].set_checked(True)

        window._show_select()
        window._open_aircraft("trainer")

        self.assertIs(window.current_checklist, session)
        self.assertTrue(window.current_checklist.rows[0].is_checked())

    def test_section_change_resets_scroll_to_top(self):
        screen = ChecklistScreen(AIRCRAFT["trainer"])
        screen.resize(1040, 680)
        screen.show()
        self.app.processEvents()
        screen.enforce_checklist = False
        screen.scroll.verticalScrollBar().setValue(
            screen.scroll.verticalScrollBar().maximum()
        )

        screen._load_section("Start & Takeoff")
        self.app.processEvents()

        self.assertEqual(screen.scroll.verticalScrollBar().value(), 0)

    def test_demonstrator_has_no_rangefinder_or_brake_items(self):
        items = [
            item.text
            for section in CHECKLISTS["demonstrator"].values()
            for item in section
        ]
        self.assertFalse(any("RANGEFINDER" in item for item in items))
        self.assertFalse(any("BRAKE" in item for item in items))

    def test_trainer_brake_sequence(self):
        takeoff = [item.text for item in CHECKLISTS["trainer"]["Start & Takeoff"]]
        after_landing = [item.text for item in CHECKLISTS["trainer"]["After Landing"]]

        self.assertLess(
            takeoff.index("BRAKE 1 HOLD: 3,000-4,000 RPM"),
            takeoff.index("BRAKE 2 HOLD: 5,000-6,000 RPM"),
        )
        self.assertIn("BRAKE: POSITION 1", takeoff)
        self.assertLess(
            after_landing.index("FLIGHT MODE: FBWA"),
            after_landing.index("BRAKE: POSITION 2"),
        )

    def test_trainer_engine_warmup_precedes_full_throttle(self):
        items = CHECKLISTS["trainer"]["Start & Takeoff"]
        texts = [item.text for item in items]
        expected_order = (
            "ENGINE: START",
            "IDLE RPM: 2,100 +/- 200 RPM",
            "WARM-UP: THROTTLE BELOW 20% IF TEMP BELOW 100 C",
            "ENGINE TEMP: ABOVE 100 C",
            "THROTTLE: INCREASE GRADUALLY",
            "FULL THROTTLE RPM: APPROX. 7000 RPM",
        )
        indices = [texts.index(text) for text in expected_order]
        self.assertEqual(indices, sorted(indices))
        warmup = items[texts.index(expected_order[2])]
        self.assertTrue(warmup.optional)

    def test_checked_section_survives_next_and_previous_navigation(self):
        screen = ChecklistScreen(AIRCRAFT["demonstrator"])
        expected_count = len(CHECKLISTS["demonstrator"]["Before Start"])
        screen._complete_current_section()

        screen._next_section()
        screen._previous_section()

        self.assertEqual(len(screen.rows), expected_count)
        self.assertEqual(len(screen.checked_state["Before Start"]), expected_count)
        self.assertTrue(all(row.is_checked() for row in screen.rows))

    def test_takeoff_countdown_precedes_auto_selection(self):
        for aircraft in ("trainer", "demonstrator"):
            items = [item.text for item in CHECKLISTS[aircraft]["Start & Takeoff"]]
            runway_index = items.index("RUNWAY: CLEAR")
            countdown_index = items.index("TAKEOFF: COMMENCE, 3-2-1")
            auto_index = items.index("FLIGHT MODE: AUTO")
            self.assertLess(runway_index, countdown_index)
            self.assertLess(countdown_index, auto_index)

    def test_checklist_instructions_are_unique_and_concise(self):
        for sections in CHECKLISTS.values():
            for items in sections.values():
                texts = [item.text for item in items]
                self.assertEqual(len(texts), len(set(texts)))
                self.assertTrue(all(text and len(text) <= 60 for text in texts))
                self.assertFalse(any(" - SELECT" in text for text in texts))

    def test_control_authority_follows_control_surfaces(self):
        for aircraft in ("trainer", "demonstrator"):
            items = [item.text for item in CHECKLISTS[aircraft]["Before Start"]]
            surfaces_index = items.index("CONTROL SURFACES: FULL / FREE / CORRECT")
            authority_index = items.index("CONTROL AUTHORITY: CHECKED")
            self.assertEqual(authority_index, surfaces_index + 1)

    def test_tower_calls_follow_operational_sequence(self):
        for aircraft in ("trainer", "demonstrator"):
            takeoff = [item.text for item in CHECKLISTS[aircraft]["Start & Takeoff"]]
            mission = [item.text for item in CHECKLISTS[aircraft]["Mission / Cruise"]]
            landing = [item.text for item in CHECKLISTS[aircraft]["Before Landing"]]

            self.assertLess(
                takeoff.index("TOWER: REQUEST START CLEARANCE"),
                takeoff.index("PROP AREA: CLEAR - CALL 'CLEAR PROP'"),
            )
            self.assertEqual(
                takeoff.index("TOWER: REQUEST TAXI CLEARANCE"),
                takeoff.index("THROTTLE RESPONSE: SMOOTH") + 1,
            )
            self.assertEqual(
                takeoff.index("TOWER: REQUEST TAKEOFF CLEARANCE"),
                takeoff.index("RUNWAY: CLEAR") - 1,
            )
            self.assertEqual(
                mission.index("TOWER: REPORT AREA / ALTITUDE"),
                mission.index("ALTITUDE / AIRSPEED: NORMAL") + 1,
            )
            self.assertLess(
                landing.index("TOWER: REQUEST LANDING CLEARANCE"),
                landing.index("RUNWAY / APPROACH: CLEAR"),
            )

    def test_external_pilot_handover_is_optional(self):
        for aircraft in ("trainer", "demonstrator"):
            items = CHECKLISTS[aircraft]["Before Landing"]
            texts = [item.text for item in items]
            landing_index = texts.index("LANDING: CONTINUE")
            handover_index = texts.index("EXTERNAL PILOT: HANDOVER IF REQUIRED")
            self.assertEqual(handover_index, landing_index + 1)
            self.assertTrue(items[handover_index].optional)

            screen = ChecklistScreen(AIRCRAFT[aircraft])
            screen.enforce_checklist = False
            screen._load_section("Before Landing")
            for row in screen.rows:
                if not row.item.optional:
                    row.set_checked(True)
            self.assertTrue(screen._section_complete("Before Landing"))

    def test_home_and_rally_point_follow_landing_sequence(self):
        for aircraft in ("trainer", "demonstrator"):
            items = [item.text for item in CHECKLISTS[aircraft]["Before Start"]]
            self.assertIn("MISSION: ROUTE / ALTITUDE CHECKED", items)
            landing_index = items.index("LANDING SEQUENCE: CHECKED")
            rally_index = items.index(
                "HOME / RALLY POINT: POSITION / ALTITUDE CHECKED"
            )
            self.assertEqual(rally_index, landing_index + 1)
            self.assertFalse(any("HOME / RTL" in item for item in items))

    def test_instruction_color_categories(self):
        expected = {
            "MAIN BATTERY: MIN 12.3 V": "check",
            "AIRSPEED: REASONABLE": "test",
            "AIRSPEED DATA: VALID": "check",
            "AHRS: ATTITUDE / HEADING CORRECT": "test",
            "RANGEFINDER: REASONABLE": "test",
            "THROTTLE RESPONSE: SMOOTH": "test",
            "FLIGHT MODE: AUTO": "set",
            "TAKEOFF: COMMENCE, 3-2-1": "action",
            "TOWER: REQUEST TAKEOFF CLEARANCE": "comm",
        }
        categorized = {}
        for sections in CHECKLISTS.values():
            for items in sections.values():
                for item in items:
                    kind = instruction_kind(item)
                    self.assertIn(kind, INSTRUCTION_KINDS)
                    categorized[item.text] = kind
        for text, kind in expected.items():
            self.assertEqual(categorized[text], kind)

    def test_color_legend_is_in_side_panel(self):
        screen = ChecklistScreen(AIRCRAFT["trainer"])
        legend = screen.findChild(QtWidgets.QFrame, "legendPanel")
        self.assertIsNotNone(legend)
        labels = [label.text() for label in legend.findChildren(QtWidgets.QLabel)]
        for text in ("Color Legend", "CHECK", "TEST", "SET", "ACTION", "COMM"):
            self.assertIn(text, labels)

    def test_instruction_kind_colors_the_whole_row(self):
        screen = ChecklistScreen(AIRCRAFT["trainer"])
        for row in screen.rows:
            self.assertEqual(row.property("kind"), instruction_kind(row.item))
            self.assertIsNone(row.findChild(QtWidgets.QLabel, "categoryBadge"))

    def test_enter_checks_the_next_unchecked_item(self):
        screen = ChecklistScreen(AIRCRAFT["trainer"])
        screen.show()
        screen.activateWindow()
        screen.setFocus()
        self.app.processEvents()

        QtTest.QTest.keyClick(screen, QtCore.Qt.Key_Return)
        self.app.processEvents()
        self.assertTrue(screen.rows[0].is_checked())
        self.assertFalse(screen.rows[1].is_checked())

        QtTest.QTest.keyClick(screen, QtCore.Qt.Key_Enter)
        self.app.processEvents()
        self.assertTrue(screen.rows[1].is_checked())


if __name__ == "__main__":
    unittest.main()

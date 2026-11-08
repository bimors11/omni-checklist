import unittest

from PyQt5 import QtCore, QtWidgets

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
        screen.scroll.verticalScrollBar().setValue(screen.scroll.verticalScrollBar().maximum())
        screen._load_section("Start & Takeoff")
        self.app.processEvents()
        self.assertEqual(screen.scroll.verticalScrollBar().value(), 0)

    def test_demonstrator_has_rangefinder_but_no_brake_items(self):
        items = [item.text for section in CHECKLISTS["demonstrator"].values() for item in section]
        self.assertTrue(any("RANGEFINDER" in text for text in items))
        self.assertFalse(any("BRAKE" in text for text in items))

    def test_checked_section_survives_navigation(self):
        screen = ChecklistScreen(AIRCRAFT["demonstrator"])
        screen._complete_current_section()
        screen._next_section()
        screen._previous_section()
        self.assertTrue(all(row.is_checked() for row in screen.rows))

    def test_instructions_are_unique_and_concise(self):
        for sections in CHECKLISTS.values():
            for items in sections.values():
                texts = [item.text for item in items]
                self.assertEqual(len(texts), len(set(texts)))
                self.assertTrue(all(text and len(text) <= 60 for text in texts))

    def test_legend_and_row_categories(self):
        screen = ChecklistScreen(AIRCRAFT["trainer"])
        legend = screen.findChild(QtWidgets.QFrame, "legendPanel")
        self.assertIsNotNone(legend)
        labels = [label.text() for label in legend.findChildren(QtWidgets.QLabel)]
        for text in ("Color Legend", "CHECK", "TEST", "SET", "ACTION", "COMM"):
            self.assertIn(text, labels)
        for row in screen.rows:
            self.assertIn(instruction_kind(row.item), INSTRUCTION_KINDS)
            self.assertEqual(row.property("kind"), instruction_kind(row.item))

    def test_enter_checks_next_item(self):
        screen = ChecklistScreen(AIRCRAFT["trainer"])
        screen._check_next_item()
        self.assertTrue(screen.rows[0].is_checked())
        self.assertFalse(screen.rows[1].is_checked())

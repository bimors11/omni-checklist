from PyQt5 import QtWidgets

from omni_checklist.background import BackgroundWidget
from omni_checklist.checklist_data import AIRCRAFT
from omni_checklist.screens import ChecklistScreen, SelectScreen
from omni_checklist.styles import style_for


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OMNI Checklist")
        self.resize(1320, 820)
        self.setMinimumSize(1040, 680)
        self.theme = "dark"

        self.surface = BackgroundWidget()
        self.setCentralWidget(self.surface)
        self.stack = QtWidgets.QStackedLayout(self.surface)
        self.stack.setContentsMargins(0, 0, 0, 0)

        self.select_screen = SelectScreen()
        self.select_screen.aircraft_selected.connect(self._open_aircraft)
        self.select_screen.theme_toggled.connect(self._toggle_theme)
        self.stack.addWidget(self.select_screen)
        self.current_checklist = None
        self.checklist_sessions = {}
        self._apply_theme()

    def _open_aircraft(self, key: str) -> None:
        self.current_checklist = self.checklist_sessions.get(key)
        if self.current_checklist is None:
            self.current_checklist = ChecklistScreen(AIRCRAFT[key], self.theme)
            self.current_checklist.back_requested.connect(self._show_select)
            self.current_checklist.theme_toggled.connect(self._toggle_theme)
            self.checklist_sessions[key] = self.current_checklist
            self.stack.addWidget(self.current_checklist)
        else:
            self.current_checklist.set_theme(self.theme)
        self.stack.setCurrentWidget(self.current_checklist)

    def _show_select(self) -> None:
        self.stack.setCurrentWidget(self.select_screen)

    def _toggle_theme(self) -> None:
        self.theme = "light" if self.theme == "dark" else "dark"
        self._apply_theme()

    def _apply_theme(self) -> None:
        app = QtWidgets.QApplication.instance()
        if app:
            app.setStyleSheet(style_for(self.theme))
        self.surface.set_theme(self.theme)
        self.select_screen.set_theme(self.theme)
        for checklist in self.checklist_sessions.values():
            checklist.set_theme(self.theme)

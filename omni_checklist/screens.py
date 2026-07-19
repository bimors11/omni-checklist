from typing import Dict, List

from PyQt5 import QtCore, QtGui, QtWidgets

from omni_checklist.checklist_data import BETA_LOGO, AIRCRAFT, SECTION_ORDER, Aircraft, checklist_for
from omni_checklist.widgets import AircraftCard, ChecklistRow


def beta_logo_pixmap(size: int, theme: str) -> QtGui.QPixmap:
    pix = QtGui.QPixmap(BETA_LOGO)
    if pix.isNull():
        return pix

    scaled = pix.scaled(size, size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
    if theme == "dark":
        return scaled

    tinted = QtGui.QPixmap(scaled.size())
    tinted.fill(QtCore.Qt.transparent)

    painter = QtGui.QPainter(tinted)
    painter.setCompositionMode(QtGui.QPainter.CompositionMode_Source)
    painter.drawPixmap(0, 0, scaled)
    painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
    painter.fillRect(tinted.rect(), QtGui.QColor("#172123"))
    painter.end()
    return tinted


def beta_logo_label(size: int = 58, theme: str = "dark") -> QtWidgets.QLabel:
    label = QtWidgets.QLabel()
    label.setObjectName("betaLogo")
    label.setFixedSize(size, size)
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setProperty("logoSize", size)

    pix = beta_logo_pixmap(size, theme)
    if not pix.isNull():
        label.setPixmap(pix)
    return label


def set_beta_logo_theme(label: QtWidgets.QLabel, theme: str) -> None:
    size = label.property("logoSize") or label.width()
    pix = beta_logo_pixmap(int(size), theme)
    if not pix.isNull():
        label.setPixmap(pix)


class SelectScreen(QtWidgets.QWidget):
    aircraft_selected = QtCore.pyqtSignal(str)
    theme_toggled = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.theme = "dark"
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(34, 28, 34, 28)
        layout.setSpacing(22)

        heading_row = QtWidgets.QHBoxLayout()
        heading_row.setSpacing(14)
        heading = QtWidgets.QVBoxLayout()
        heading.setSpacing(6)
        title = QtWidgets.QLabel("OMNI UAV Checklist")
        title.setObjectName("appTitle")
        subtitle = QtWidgets.QLabel("Select the aircraft before entering the operational checklist.")
        subtitle.setObjectName("mutedText")
        heading.addWidget(title)
        heading.addWidget(subtitle)
        heading_row.addLayout(heading, 1)
        self.theme_btn = QtWidgets.QPushButton()
        self.theme_btn.setProperty("role", "theme")
        self.theme_btn.clicked.connect(self.theme_toggled.emit)
        heading_row.addWidget(self.theme_btn, 0, QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        self.logo = beta_logo_label(68, self.theme)
        heading_row.addWidget(self.logo, 0, QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        layout.addLayout(heading_row)

        cards = QtWidgets.QHBoxLayout()
        cards.setSpacing(18)
        for aircraft in AIRCRAFT.values():
            card = AircraftCard(aircraft)
            card.selected.connect(self.aircraft_selected.emit)
            cards.addWidget(card)
        layout.addLayout(cards, 1)

        foot = QtWidgets.QLabel("OMNI-Trainer and OMNI-Demonstrator normal operations checklist.")
        foot.setObjectName("hintText")
        foot.setWordWrap(True)
        layout.addWidget(foot)
        self.set_theme(self.theme)

    def set_theme(self, theme: str) -> None:
        self.theme = theme
        self.theme_btn.setText("Light Theme" if theme == "dark" else "Dark Theme")
        set_beta_logo_theme(self.logo, theme)


class ChecklistScreen(QtWidgets.QWidget):
    back_requested = QtCore.pyqtSignal()
    theme_toggled = QtCore.pyqtSignal()

    def __init__(self, aircraft: Aircraft, theme: str = "dark"):
        super().__init__()
        self.aircraft = aircraft
        self.theme = theme
        self.data = checklist_for(aircraft.key)
        self.rows: List[ChecklistRow] = []
        self.nav_buttons: Dict[str, QtWidgets.QPushButton] = {}
        self.checked_state = {
            section: [False] * len(items)
            for section, items in self.data.items()
        }
        self.enforce_checklist = False
        self.current_section = SECTION_ORDER[0]
        self._build_ui()
        self._load_section(self.current_section)

    def _build_ui(self):
        root = QtWidgets.QVBoxLayout(self)
        root.setContentsMargins(18, 16, 18, 14)
        root.setSpacing(12)

        top = self._build_toolbar()
        root.addWidget(top)

        splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitter.setChildrenCollapsible(False)
        splitter.setHandleWidth(9)
        root.addWidget(splitter, 1)

        splitter.addWidget(self._build_side_panel())
        splitter.addWidget(self._build_checklist_panel())
        splitter.setSizes([420, 900])

    def _build_toolbar(self) -> QtWidgets.QFrame:
        top = QtWidgets.QFrame()
        top.setObjectName("toolbar")
        top_layout = QtWidgets.QHBoxLayout(top)
        top_layout.setContentsMargins(14, 10, 14, 10)
        top_layout.setSpacing(12)

        back = QtWidgets.QPushButton("Change UAV")
        back.setProperty("role", "secondary")
        back.clicked.connect(self.back_requested.emit)
        top_layout.addWidget(back)

        title_box = QtWidgets.QVBoxLayout()
        title_box.setSpacing(0)
        title = QtWidgets.QLabel(self.aircraft.name)
        title.setObjectName("screenTitle")
        subtitle = QtWidgets.QLabel(f"{self.aircraft.subtitle} | Normal operations")
        subtitle.setObjectName("mutedText")
        title_box.addWidget(title)
        title_box.addWidget(subtitle)
        top_layout.addLayout(title_box, 1)

        self.progress = QtWidgets.QProgressBar()
        self.progress.setFixedWidth(290)
        self.progress.setRange(0, 100)
        top_layout.addWidget(self.progress)

        reset = QtWidgets.QPushButton("Reset Section")
        reset.setProperty("role", "danger")
        reset.clicked.connect(self._reset_current_section)
        top_layout.addWidget(reset)

        self.theme_btn = QtWidgets.QPushButton()
        self.theme_btn.setProperty("role", "theme")
        self.theme_btn.clicked.connect(self.theme_toggled.emit)
        top_layout.addWidget(self.theme_btn)

        self.logo = beta_logo_label(54, self.theme)
        top_layout.addWidget(self.logo, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.set_theme(self.theme)
        return top

    def set_theme(self, theme: str) -> None:
        self.theme = theme
        if hasattr(self, "theme_btn"):
            self.theme_btn.setText("Light Theme" if theme == "dark" else "Dark Theme")
        if hasattr(self, "logo"):
            set_beta_logo_theme(self.logo, theme)

    def _build_side_panel(self) -> QtWidgets.QFrame:
        left = QtWidgets.QFrame()
        left.setObjectName("sidePanel")
        left_layout = QtWidgets.QVBoxLayout(left)
        left_layout.setContentsMargins(12, 12, 12, 12)
        left_layout.setSpacing(8)

        aircraft_image = QtWidgets.QLabel()
        aircraft_image.setAlignment(QtCore.Qt.AlignCenter)
        pix = QtGui.QPixmap(self.aircraft.image)
        if not pix.isNull():
            aircraft_image.setPixmap(pix.scaled(280, 155, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        left_layout.addWidget(aircraft_image)

        for section in SECTION_ORDER:
            button = QtWidgets.QPushButton(section)
            button.setProperty("role", "nav")
            button.setCheckable(True)
            button.clicked.connect(lambda checked, name=section: self._load_section(name))
            self.nav_buttons[section] = button
            left_layout.addWidget(button)

        left_layout.addStretch(1)
        hint = QtWidgets.QLabel("Normal operations checklist.")
        hint.setObjectName("hintText")
        hint.setWordWrap(True)
        left_layout.addWidget(hint)
        return left

    def _build_checklist_panel(self) -> QtWidgets.QWidget:
        right = QtWidgets.QWidget()
        right_layout = QtWidgets.QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(10)

        header = QtWidgets.QFrame()
        header.setObjectName("sectionHeader")
        header_layout = QtWidgets.QVBoxLayout(header)
        header_layout.setContentsMargins(14, 12, 14, 12)
        self.section_title = QtWidgets.QLabel()
        self.section_title.setObjectName("sectionTitle")
        self.section_context = QtWidgets.QLabel()
        self.section_context.setObjectName("rowDetail")
        self.section_context.setWordWrap(True)
        header_layout.addWidget(self.section_title)
        header_layout.addWidget(self.section_context)
        right_layout.addWidget(header)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.list_widget = QtWidgets.QWidget()
        self.list_layout = QtWidgets.QVBoxLayout(self.list_widget)
        self.list_layout.setContentsMargins(0, 0, 0, 0)
        self.list_layout.setSpacing(8)
        self.scroll.setWidget(self.list_widget)
        right_layout.addWidget(self.scroll, 1)

        footer = self._build_footer()
        right_layout.addWidget(footer)
        return right

    def _build_footer(self) -> QtWidgets.QFrame:
        footer = QtWidgets.QFrame()
        footer.setObjectName("toolbar")
        footer_layout = QtWidgets.QHBoxLayout(footer)
        footer_layout.setContentsMargins(12, 10, 12, 10)
        footer_layout.setSpacing(10)
        self.prev_btn = QtWidgets.QPushButton("Previous")
        self.next_btn = QtWidgets.QPushButton("Next")
        self.prev_btn.clicked.connect(self._previous_section)
        self.next_btn.clicked.connect(self._next_section)
        self.enforce_btn = QtWidgets.QPushButton()
        self.enforce_btn.setProperty("role", "enforce")
        self.enforce_btn.setCheckable(True)
        self.enforce_btn.clicked.connect(self._toggle_enforce_checklist)
        self.complete_btn = QtWidgets.QPushButton("Mark Section Complete")
        self.complete_btn.setProperty("role", "primary")
        self.complete_btn.clicked.connect(self._complete_current_section)
        self.enforce_hint = QtWidgets.QLabel()
        self.enforce_hint.setObjectName("hintText")
        footer_layout.addWidget(self.prev_btn)
        footer_layout.addWidget(self.next_btn)
        footer_layout.addWidget(self.enforce_btn)
        footer_layout.addWidget(self.enforce_hint)
        footer_layout.addStretch(1)
        footer_layout.addWidget(self.complete_btn)
        self._sync_enforce_button()
        return footer

    def _section_context(self, section: str) -> str:
        if section == "Before Start":
            return "Aircraft, link, mission, and area checks before start."
        if section == "Start & Takeoff":
            return "Start, taxi, wind, runway, and takeoff checks."
        if section == "Mission / Cruise":
            return "Flight path, status, link, and return decision checks."
        if section == "Before Landing":
            return "Landing sequence, approach, wind, and go-around checks."
        return "Shutdown and disconnect checks."

    def _load_section(self, section: str):
        if not self._can_open_section(section):
            self._sync_prev_next()
            return

        self._save_current_state()
        self.current_section = section
        for name, button in self.nav_buttons.items():
            button.setChecked(name == section)

        while self.list_layout.count():
            item = self.list_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        self.rows = []

        self.section_title.setText(section)
        self.section_context.setText(self._section_context(section))

        for index, checklist_item in enumerate(self.data[section]):
            row = ChecklistRow(checklist_item)
            row.changed.connect(self._update_progress)
            row.set_checked(self.checked_state[section][index])
            self.rows.append(row)
            self.list_layout.addWidget(row)
        self.list_layout.addStretch(1)
        self._update_progress()
        self._sync_prev_next()

    def _save_current_state(self):
        if not self.rows or self.current_section not in self.checked_state:
            return
        self.checked_state[self.current_section] = [row.is_checked() for row in self.rows]

    def _update_progress(self):
        self._save_current_state()
        total = len(self.rows)
        done = sum(row.is_checked() for row in self.rows)
        percent = int((done / total) * 100) if total else 0
        self.progress.setValue(percent)
        self.progress.setFormat(f"{done}/{total} complete")
        self._sync_prev_next()

    def _sync_prev_next(self):
        idx = SECTION_ORDER.index(self.current_section)
        self.prev_btn.setEnabled(idx > 0)
        self.next_btn.setEnabled(idx < len(SECTION_ORDER) - 1 and self._can_continue_from_current())
        self._sync_nav_buttons()
        self._sync_enforce_button()

    def _sync_nav_buttons(self):
        for section, button in self.nav_buttons.items():
            button.setEnabled(self._can_open_section(section))

    def _sync_enforce_button(self):
        if not hasattr(self, "enforce_btn"):
            return
        self.enforce_btn.setChecked(self.enforce_checklist)
        self.enforce_btn.setText("Enforce Checklist: ON" if self.enforce_checklist else "Enforce Checklist: OFF")
        if not hasattr(self, "enforce_hint"):
            return
        if self.enforce_checklist and not self._section_complete(self.current_section):
            self.enforce_hint.setText("Complete this section to continue.")
        else:
            self.enforce_hint.setText("")

    def _toggle_enforce_checklist(self):
        self.enforce_checklist = self.enforce_btn.isChecked()
        if self.enforce_checklist and not self._can_open_section(self.current_section):
            self._load_section(self._first_incomplete_section())
            return
        self._sync_prev_next()

    def _section_complete(self, section: str) -> bool:
        checked = self.checked_state.get(section, [])
        return bool(checked) and all(checked)

    def _first_incomplete_section(self) -> str:
        for section in SECTION_ORDER:
            if not self._section_complete(section):
                return section
        return SECTION_ORDER[-1]

    def _can_open_section(self, section: str) -> bool:
        if not self.enforce_checklist:
            return True
        return SECTION_ORDER.index(section) <= SECTION_ORDER.index(self._first_incomplete_section())

    def _can_continue_from_current(self) -> bool:
        return not self.enforce_checklist or self._section_complete(self.current_section)

    def _previous_section(self):
        idx = SECTION_ORDER.index(self.current_section)
        if idx > 0:
            self._load_section(SECTION_ORDER[idx - 1])

    def _next_section(self):
        idx = SECTION_ORDER.index(self.current_section)
        if idx < len(SECTION_ORDER) - 1 and self._can_continue_from_current():
            self._load_section(SECTION_ORDER[idx + 1])

    def _complete_current_section(self):
        for row in self.rows:
            row.set_checked(True)
        self._save_current_state()
        self._update_progress()

    def _reset_current_section(self):
        for row in self.rows:
            row.set_checked(False)
        self._save_current_state()
        self._update_progress()

from PyQt5 import QtCore, QtGui, QtWidgets

from omni_checklist.checklist_data import Aircraft, ChecklistItem


class AircraftCard(QtWidgets.QFrame):
    selected = QtCore.pyqtSignal(str)

    def __init__(self, aircraft: Aircraft):
        super().__init__()
        self.aircraft = aircraft
        self.setObjectName("aircraftCard")
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.setMinimumHeight(440)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(12)

        image = QtWidgets.QLabel()
        image.setObjectName("aircraftImage")
        image.setAlignment(QtCore.Qt.AlignCenter)
        pix = QtGui.QPixmap(aircraft.image)
        if not pix.isNull():
            image.setPixmap(pix.scaled(760, 360, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        image.setMinimumHeight(330)
        layout.addWidget(image, 1)

        name = QtWidgets.QLabel(aircraft.name)
        name.setObjectName("aircraftName")
        layout.addWidget(name)

        subtitle = QtWidgets.QLabel(aircraft.subtitle)
        subtitle.setObjectName("mutedText")
        subtitle.setWordWrap(True)
        layout.addWidget(subtitle)

        button = QtWidgets.QPushButton("Open Checklist")
        button.setProperty("role", "primary")
        button.clicked.connect(lambda: self.selected.emit(aircraft.key))
        layout.addWidget(button)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.selected.emit(self.aircraft.key)
        super().mouseReleaseEvent(event)


class ChecklistRow(QtWidgets.QFrame):
    changed = QtCore.pyqtSignal()

    def __init__(self, item: ChecklistItem):
        super().__init__()
        self.item = item
        self.setObjectName("checkRow")
        self.setProperty("critical", "true" if item.critical else "false")
        self.setCursor(QtCore.Qt.PointingHandCursor)

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(14, 13, 14, 13)
        layout.setSpacing(14)

        self.checkbox = QtWidgets.QCheckBox()
        self.checkbox.setFixedWidth(36)
        self.checkbox.stateChanged.connect(self._on_changed)
        layout.addWidget(self.checkbox, 0, QtCore.Qt.AlignTop)

        text_layout = QtWidgets.QVBoxLayout()
        text_layout.setSpacing(4)
        title = QtWidgets.QLabel(item.text)
        title.setObjectName("rowTitle")
        title.setWordWrap(True)
        title.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        text_layout.addWidget(title)

        if item.detail:
            detail = QtWidgets.QLabel(item.detail)
            detail.setObjectName("rowDetail")
            detail.setWordWrap(True)
            detail.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
            text_layout.addWidget(detail)
        layout.addLayout(text_layout, 1)

        if item.critical:
            badge = QtWidgets.QLabel("CRITICAL")
            badge.setObjectName("criticalBadge")
            badge.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
            layout.addWidget(badge, 0, QtCore.Qt.AlignTop)

    def _on_changed(self):
        self.setProperty("done", "true" if self.checkbox.isChecked() else "false")
        self.style().unpolish(self)
        self.style().polish(self)
        self.changed.emit()

    def is_checked(self) -> bool:
        return self.checkbox.isChecked()

    def set_checked(self, checked: bool) -> None:
        self.checkbox.setChecked(checked)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.checkbox.toggle()
            event.accept()
            return
        super().mouseReleaseEvent(event)

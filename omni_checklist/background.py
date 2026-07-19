from PyQt5 import QtCore, QtGui, QtWidgets


class BackgroundWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.theme = "dark"

    def set_theme(self, theme: str) -> None:
        self.theme = theme
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        rect = self.rect()
        if self.theme == "light":
            painter.fillRect(rect, QtGui.QColor("#eef4f4"))
            base = QtGui.QRadialGradient(
                QtCore.QPointF(rect.width() * 0.18, rect.height() * 0.95),
                max(rect.width(), rect.height()) * 0.95,
            )
            base.setColorAt(0.0, QtGui.QColor(116, 216, 218, 92))
            base.setColorAt(0.34, QtGui.QColor(207, 239, 238, 124))
            base.setColorAt(0.70, QtGui.QColor(238, 244, 244, 210))
            base.setColorAt(1.0, QtGui.QColor(238, 244, 244, 255))
            painter.fillRect(rect, base)
            painter.end()
            return

        painter.fillRect(rect, QtGui.QColor("#000000"))

        base = QtGui.QRadialGradient(
            QtCore.QPointF(rect.width() * 0.18, rect.height() * 0.95),
            max(rect.width(), rect.height()) * 0.95,
        )
        base.setColorAt(0.0, QtGui.QColor(0, 174, 190, 92))
        base.setColorAt(0.28, QtGui.QColor(0, 82, 96, 64))
        base.setColorAt(0.62, QtGui.QColor(0, 17, 27, 80))
        base.setColorAt(1.0, QtGui.QColor(0, 0, 0, 255))
        painter.fillRect(rect, base)
        painter.end()

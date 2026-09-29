DARK_STYLE = """
QWidget {
    color: #f2f2ef;
    background: transparent;
    font-family: "Liberation Sans", "Inter", "Segoe UI", Arial, sans-serif;
    font-size: 16px;
}
QMainWindow { background: #000000; }
QLabel#appTitle {
    font-size: 40px;
    font-weight: 900;
    letter-spacing: 0px;
}
QLabel#screenTitle {
    font-size: 24px;
    font-weight: 900;
}
QLabel#sectionTitle {
    font-size: 28px;
    font-weight: 900;
}
QLabel#aircraftName {
    font-size: 26px;
    font-weight: 900;
}
QLabel#mutedText, QLabel#rowDetail, QLabel#hintText {
    color: #aebbbb;
}
QLabel#hintText {
    font-size: 14px;
}
QLabel#betaLogo {
    background: transparent;
    border: none;
}
QFrame#aircraftCard,
QFrame#sidePanel,
QFrame#sectionHeader,
QFrame#toolbar {
    background: rgba(6, 10, 11, 188);
    border: 1px solid rgba(93, 129, 130, 118);
    border-radius: 8px;
}
QFrame#aircraftCard:hover {
    background: rgba(8, 19, 21, 220);
    border-color: rgba(205, 255, 252, 190);
}
QFrame#checkRow {
    background: rgba(7, 11, 12, 172);
    border: 1px solid rgba(77, 105, 104, 96);
    border-radius: 7px;
}
QFrame#checkRow:hover {
    background: rgba(11, 20, 21, 210);
    border-color: rgba(151, 206, 204, 145);
}
QFrame#checkRow[critical="true"] {
    border-left: 3px solid #00e5ff;
}
QFrame#checkRow[done="true"] {
    background: rgba(9, 24, 22, 190);
    border-color: rgba(58, 205, 176, 150);
}
QFrame#checkRow[kind="check"] {
    background: rgba(23, 107, 135, 82);
    border-color: rgba(42, 151, 184, 155);
}
QFrame#checkRow[kind="test"] {
    background: rgba(165, 90, 18, 82);
    border-color: rgba(211, 125, 40, 165);
}
QFrame#checkRow[kind="set"] {
    background: rgba(113, 76, 162, 82);
    border-color: rgba(153, 111, 207, 165);
}
QFrame#checkRow[kind="action"] {
    background: rgba(166, 61, 61, 82);
    border-color: rgba(218, 83, 83, 165);
}
QFrame#checkRow[kind="comm"] {
    background: rgba(36, 117, 79, 82);
    border-color: rgba(58, 166, 112, 165);
}
QFrame#legendPanel {
    background: rgba(8, 14, 15, 150);
    border: 1px solid rgba(77, 105, 104, 96);
    border-radius: 7px;
}
QLabel#legendTitle {
    font-size: 17px;
    font-weight: 900;
}
QLabel#legendText {
    color: #aebbbb;
    font-size: 13px;
}
QLabel#rowTitle {
    color: #ffffff;
    font-weight: 800;
    font-size: 20px;
}
QLabel#criticalBadge {
    color: #061010;
    background: #61f7ff;
    border-radius: 4px;
    padding: 5px 8px;
    font-size: 12px;
    font-weight: 900;
}
QLabel#optionalBadge {
    color: #d8e2e2;
    background: #354142;
    border-radius: 4px;
    padding: 5px 8px;
    font-size: 12px;
    font-weight: 900;
}
QLabel#categoryBadge {
    color: #ffffff;
    border-radius: 4px;
    padding: 5px 8px;
    font-size: 12px;
    font-weight: 900;
}
QLabel#categoryBadge[kind="check"] { background: #176b87; }
QLabel#categoryBadge[kind="test"] { background: #a55a12; }
QLabel#categoryBadge[kind="set"] { background: #714ca2; }
QLabel#categoryBadge[kind="action"] { background: #a63d3d; }
QLabel#categoryBadge[kind="comm"] { background: #24754f; }
QPushButton {
    color: #f2f2ef;
    background: rgba(10, 14, 15, 205);
    border: 1px solid rgba(98, 122, 122, 112);
    border-radius: 6px;
    padding: 10px 14px;
    font-weight: 800;
    min-height: 36px;
}
QPushButton:hover {
    color: #ffffff;
    background: #1a1f1f;
    border-color: #d7dbdb;
}
QPushButton:pressed {
    color: #070909;
    background: #ffffff;
    border-color: #ffffff;
}
QPushButton:disabled {
    color: #657171;
    background: #101515;
    border-color: #252d2d;
}
QPushButton[role="primary"] {
    color: #061010;
    background: #f2f2ef;
    border-color: #ffffff;
}
QPushButton[role="secondary"] {
    background: rgba(13, 16, 16, 220);
}
QPushButton[role="danger"] {
    color: #ffffff;
    background: #7d2421;
    border-color: #c24038;
}
QPushButton[role="theme"] {
    min-width: 112px;
}
QPushButton[role="enforce"] {
    min-width: 190px;
}
QPushButton[role="enforce"]:checked {
    color: #061010;
    background: #58f7e8;
    border-color: #cffffb;
}
QPushButton[role="nav"] {
    text-align: left;
    padding: 6px 12px;
    min-height: 28px;
}
QPushButton[role="nav"]:checked {
    color: #061010;
    background: #f2f2ef;
    border-color: #ffffff;
}
QCheckBox::indicator {
    width: 28px;
    height: 28px;
    border-radius: 5px;
    border: 1px solid rgba(170, 205, 205, 160);
    background: rgba(0, 0, 0, 155);
}
QCheckBox::indicator:hover {
    border-color: #ffffff;
}
QCheckBox::indicator:checked {
    background: #58f7e8;
    border-color: #cffffb;
}
QProgressBar {
    height: 34px;
    text-align: center;
    color: #f2f2ef;
    background: rgba(6, 9, 10, 220);
    border: 1px solid rgba(98, 122, 122, 112);
    border-radius: 6px;
    font-weight: 800;
    font-size: 15px;
}
QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00d5ff, stop:1 #4ff7c8);
    border-radius: 5px;
}
QScrollArea {
    background: transparent;
    border: none;
}
QScrollBar:vertical {
    background: rgba(4, 7, 8, 160);
    width: 12px;
    margin: 0px;
}
QScrollBar::handle:vertical {
    background: rgba(134, 162, 162, 150);
    border-radius: 5px;
    min-height: 30px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
QSplitter::handle {
    background: rgba(33, 43, 43, 120);
    margin: 0px 4px;
    border-radius: 3px;
}
"""


LIGHT_STYLE = """
QWidget {
    color: #172123;
    background: transparent;
    font-family: "Liberation Sans", "Inter", "Segoe UI", Arial, sans-serif;
    font-size: 16px;
}
QMainWindow { background: #eef4f4; }
QLabel#appTitle {
    font-size: 40px;
    font-weight: 900;
    letter-spacing: 0px;
}
QLabel#screenTitle {
    font-size: 24px;
    font-weight: 900;
}
QLabel#sectionTitle {
    font-size: 28px;
    font-weight: 900;
}
QLabel#aircraftName {
    font-size: 26px;
    font-weight: 900;
}
QLabel#mutedText, QLabel#rowDetail, QLabel#hintText {
    color: #526468;
}
QLabel#hintText {
    font-size: 14px;
}
QLabel#betaLogo {
    background: transparent;
    border: none;
}
QFrame#aircraftCard,
QFrame#sidePanel,
QFrame#sectionHeader,
QFrame#toolbar {
    background: rgba(255, 255, 255, 224);
    border: 1px solid rgba(123, 148, 151, 150);
    border-radius: 8px;
}
QFrame#aircraftCard:hover {
    background: rgba(247, 252, 252, 245);
    border-color: rgba(0, 120, 138, 190);
}
QFrame#checkRow {
    background: rgba(255, 255, 255, 232);
    border: 1px solid rgba(126, 151, 153, 126);
    border-radius: 7px;
}
QFrame#checkRow:hover {
    background: rgba(241, 249, 249, 245);
    border-color: rgba(0, 132, 150, 170);
}
QFrame#checkRow[critical="true"] {
    border-left: 3px solid #008ea3;
}
QFrame#checkRow[done="true"] {
    background: rgba(220, 248, 242, 240);
    border-color: rgba(0, 143, 118, 170);
}
QFrame#checkRow[kind="check"] {
    background: rgba(18, 103, 131, 42);
    border-color: rgba(18, 103, 131, 135);
}
QFrame#checkRow[kind="test"] {
    background: rgba(153, 80, 13, 42);
    border-color: rgba(153, 80, 13, 140);
}
QFrame#checkRow[kind="set"] {
    background: rgba(104, 68, 150, 42);
    border-color: rgba(104, 68, 150, 140);
}
QFrame#checkRow[kind="action"] {
    background: rgba(153, 53, 53, 42);
    border-color: rgba(153, 53, 53, 140);
}
QFrame#checkRow[kind="comm"] {
    background: rgba(28, 112, 73, 42);
    border-color: rgba(28, 112, 73, 140);
}
QFrame#legendPanel {
    background: rgba(247, 251, 251, 220);
    border: 1px solid rgba(126, 151, 153, 126);
    border-radius: 7px;
}
QLabel#legendTitle {
    font-size: 17px;
    font-weight: 900;
}
QLabel#legendText {
    color: #526468;
    font-size: 13px;
}
QLabel#rowTitle {
    color: #10191b;
    font-weight: 800;
    font-size: 20px;
}
QLabel#criticalBadge {
    color: #ffffff;
    background: #008ea3;
    border-radius: 4px;
    padding: 5px 8px;
    font-size: 12px;
    font-weight: 900;
}
QLabel#optionalBadge {
    color: #ffffff;
    background: #647679;
    border-radius: 4px;
    padding: 5px 8px;
    font-size: 12px;
    font-weight: 900;
}
QLabel#categoryBadge {
    color: #ffffff;
    border-radius: 4px;
    padding: 5px 8px;
    font-size: 12px;
    font-weight: 900;
}
QLabel#categoryBadge[kind="check"] { background: #126783; }
QLabel#categoryBadge[kind="test"] { background: #99500d; }
QLabel#categoryBadge[kind="set"] { background: #684496; }
QLabel#categoryBadge[kind="action"] { background: #993535; }
QLabel#categoryBadge[kind="comm"] { background: #1c7049; }
QPushButton {
    color: #172123;
    background: rgba(255, 255, 255, 232);
    border: 1px solid rgba(110, 134, 137, 150);
    border-radius: 6px;
    padding: 10px 14px;
    font-weight: 800;
    min-height: 36px;
}
QPushButton:hover {
    color: #081113;
    background: #eef7f7;
    border-color: #008ea3;
}
QPushButton:pressed {
    color: #ffffff;
    background: #172123;
    border-color: #172123;
}
QPushButton:disabled {
    color: #91a0a3;
    background: #e3ebeb;
    border-color: #c8d4d5;
}
QPushButton[role="primary"] {
    color: #ffffff;
    background: #172123;
    border-color: #172123;
}
QPushButton[role="secondary"] {
    background: rgba(248, 252, 252, 235);
}
QPushButton[role="danger"] {
    color: #ffffff;
    background: #9c312c;
    border-color: #be4a43;
}
QPushButton[role="theme"] {
    min-width: 112px;
}
QPushButton[role="enforce"] {
    min-width: 190px;
}
QPushButton[role="enforce"]:checked {
    color: #ffffff;
    background: #008ea3;
    border-color: #007a8d;
}
QPushButton[role="nav"] {
    text-align: left;
    padding: 6px 12px;
    min-height: 28px;
}
QPushButton[role="nav"]:checked {
    color: #ffffff;
    background: #172123;
    border-color: #172123;
}
QCheckBox::indicator {
    width: 28px;
    height: 28px;
    border-radius: 5px;
    border: 1px solid rgba(88, 113, 116, 170);
    background: rgba(255, 255, 255, 230);
}
QCheckBox::indicator:hover {
    border-color: #008ea3;
}
QCheckBox::indicator:checked {
    background: #00a993;
    border-color: #007a6d;
}
QProgressBar {
    height: 34px;
    text-align: center;
    color: #172123;
    background: rgba(255, 255, 255, 232);
    border: 1px solid rgba(110, 134, 137, 150);
    border-radius: 6px;
    font-weight: 800;
    font-size: 15px;
}
QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #10b5c8, stop:1 #19c79f);
    border-radius: 5px;
}
QScrollArea {
    background: transparent;
    border: none;
}
QScrollBar:vertical {
    background: rgba(219, 229, 230, 180);
    width: 12px;
    margin: 0px;
}
QScrollBar::handle:vertical {
    background: rgba(107, 132, 135, 170);
    border-radius: 5px;
    min-height: 30px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
QSplitter::handle {
    background: rgba(151, 169, 171, 120);
    margin: 0px 4px;
    border-radius: 3px;
}
"""


STYLE = DARK_STYLE


def style_for(theme: str) -> str:
    return LIGHT_STYLE if theme == "light" else DARK_STYLE

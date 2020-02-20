import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.setWindowTitle('Fight Fighter Game Lobby')
        cx_form = qtw.QWidget()
        self.setCentralWidget(cx_form)
        cx_form.setLayout(qtw.QFormLayout())
        heading = qtw.QLabel('Fight Fighter!')
        cx_form.layout().addRow(heading)

        inputs = {
            'Server': qtw.QLineEdit(),
            'Name': qtw.QLineEdit(),
            'Password': qtw.QLineEdit(echoMode=qtw.QLineEdit.Password),
            'Team': qtw.QComboBox(),
            'Ready': qtw.QCheckBox('Check when ready')
        }
        teams = ('Crimson Shark', 'Shadow Hawks', 'Night Terrors', 'Blue Crew')
        inputs['Team'].addItems(teams)
        for label, widget in inputs.items():
            cx_form.layout().addRow(label, widget)
        self.submit = qtw.QPushButton('Connect')
        self.submit.clicked.connect(
            lambda: qtw.QMessageBox.information(
                None, 'Connecting', 'Prepare for Battle!'
            )
        )
        self.reset = qtw.QPushButton('Cancel')
        self.reset.clicked.connect(self.close)
        cx_form.layout().addRow(self.submit, self.reset)

        # Setting a font
        heading_font = qtg.QFont('Impact', 32 , qtg.QFont.Bold)
        heading_font.setStretch(qtg.QFont.ExtraExpanded)
        heading.setFont(heading_font)

        label_font = qtg.QFont()
        label_font.setFamily('Impact')
        label_font.setPointSize(14)
        label_font.setWeight(qtg.QFont.DemiBold)
        label_font.setStyle(qtg.QFont.StyleItalic)

        for inp in inputs.values():
            cx_form.layout().labelForField(inp).setFont(label_font)

        # Dealing with miss fonts
        button_font = qtg.QFont('Totally Nonexistant Font Family XYZ', 15.233)
        print(f'Font is {button_font.family()}')
        actual_font = qtg.QFontInfo(button_font).family()
        print(f'Actual font used is {actual_font}')

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())

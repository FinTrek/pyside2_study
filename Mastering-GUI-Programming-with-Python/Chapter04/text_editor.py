import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()

        ######################
        # The central widget #
        ######################
        self.text_edit = qtw.QTextEdit()
        self.setCentralWidget(self.text_edit)

        #################
        # The Statusbar #
        #################
        self.statusBar().showMessage('Welcome to text_editor.py')
        char_count = qtw.QLabel('chars: 0')
        self.text_edit.textChanged.connect(
            lambda: char_count.setText(
                'chars: ' + str(len(self.text_edit.toPlainText()))
            )
        )
        self.statusBar().addPermanentWidget(char_count)


        ###############
        # The menubar #
        ###############
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('File')
        edit_menu = menu_bar.addMenu('Edit')
        help_menu = menu_bar.addMenu('Help')

        open_action = file_menu.addAction('Open')
        save_action = file_menu.addAction('Save')
        quit_action = file_menu.addAction('Quit', self.destroy)

        edit_menu.addAction('Undo', self.text_edit.undo)
        redo_action = qtw.QAction('Redo', self)
        redo_action.triggered.connect(self.text_edit.redo)
        edit_menu.addAction(redo_action)

        ############################
        # The Toolbar and QActions #
        ############################
        tool_bar = self.addToolBar('File')

        tool_bar.setMovable(False)
        tool_bar.setFloatable(False)
        tool_bar.setAllowedAreas(qtc.Qt.TopToolBarArea | qtc.Qt.BottomToolBarArea)

        open_icon = self.style().standardIcon(qtw.QStyle.SP_DirOpenIcon)
        save_icon = self.style().standardIcon(qtw.QStyle.SP_DriveHDIcon)

        open_action.setIcon(open_icon)
        tool_bar.addAction(open_action)
        tool_bar.addAction(save_icon, 'Save', lambda: self.statusBar().showMessage('File Saved!'))
        help_action = qtw.QAction(
            self.style().standardIcon(qtw.QStyle.SP_DialogHelpButton), 'Help', self
        )
        help_action.triggered.connect(lambda: self.statusBar().showMessage('Sorry, no help yet!'))
        tool_bar.addAction(help_action)

        tool_bar2 = qtw.QToolBar('Edit')
        tool_bar2.addAction('Copy', self.text_edit.copy)
        tool_bar2.addAction('Cut', self.text_edit.cut)
        tool_bar2.addAction('Paste', self.text_edit.paste)
        self.addToolBar(qtc.Qt.RightToolBarArea, tool_bar2)

        ################
        # Dock Widgets #
        ################
        dock = qtw.QDockWidget('Replace')
        self.addDockWidget(qtc.Qt.LeftDockWidgetArea, dock)
        dock.setFeatures(
            qtw.QDockWidget.DockWidgetMovable |
            qtw.QDockWidget.DockWidgetFloatable
        )
        replace_widget = qtw.QWidget()
        replace_widget.setLayout(qtw.QVBoxLayout())
        dock.setWidget(replace_widget)

        self.search_text_inp = qtw.QLineEdit(placeholderText='search')
        self.replace_text_inp = qtw.QLineEdit(placeholderText='replace')
        search_and_replace_btn = qtw.QPushButton('Search and Replace')
        search_and_replace_btn.clicked.connect(self.search_and_replace)

        replace_widget.layout().addWidget(self.search_text_inp)
        replace_widget.layout().addWidget(self.replace_text_inp)
        replace_widget.layout().addWidget(search_and_replace_btn)
        replace_widget.layout().addStretch()

        ############################
        # Messageboxes and Dialogs #
        ############################
        help_menu.addAction('About', self.showAboutDialog)

        response = qtw.QMessageBox.question(
            self,
            'My Text Editor',
            'This is beta software, do you want to continue?',
            qtw.QMessageBox.Yes | qtw.QMessageBox.Abort
        )
        if response == qtw.QMessageBox.Abort:
            self.close()
            sys.exit()

        # custom message box

        splash_screen = qtw.QMessageBox()
        splash_screen.setWindowTitle('My Text Editor')
        splash_screen.setText('BETA SOFTWARE WARNING!')
        splash_screen.setInformativeText(
            'This is very, very beta, '
            'are you really sure you want to use it?'
        )
        splash_screen.setDetailedText(
            'This editor was written for pedagogical '
            'purposes, and probably is not fit for real work.'
        )
        splash_screen.setWindowModality(qtc.Qt.WindowModal)
        splash_screen.addButton(qtw.QMessageBox.Yes)
        splash_screen.addButton(qtw.QMessageBox.Abort)
        response = splash_screen.exec()
        if response == qtw.QMessageBox.Abort:
            self.close()
            sys.exit()


        self.show()

    def search_and_replace(self):
        s_text = self.search_text_inp.text()
        r_text = self.replace_text_inp.text()

        if s_text:
            self.text_edit.setText(
                self.text_edit.toPlainText().replace(s_text, r_text)
            )

    def showAboutDialog(self):
        qtw.QMessageBox.about(self, 'About text_editor.py', 'This is a text editor written in Pyside2.')


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())

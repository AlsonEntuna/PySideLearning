import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import *
from PySide6.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.btnPress.clicked(self._onPress())
        self.connect(self.ui.btnPress, SIGNAL("clicked()"), self._onPress)

    def _onPress(self) -> None:
        print("pressed")
        self.ui.txtbOuput.setText("Pressed")


def main():
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

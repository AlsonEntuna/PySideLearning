from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui.ui_mainwindow import Ui_rootWindow
from PySide6.QtCore import *
from PySide6.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_rootWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("My QT Window")


        # self.ui.btnPress.clicked(self._onPress())
        # self.connect(self.ui.btnPress, SIGNAL("clicked()"), self._onPress)
        self.ui.btnPress.clicked.connect(self._onPress)

    def _onPress(self) -> None:
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(["Alson", "Entuna"])
        QMessageBox.about(self, "Information", "Added Information...")

import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QApplication
from ui.ui_mainwindow import Ui_rootWindow


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
        photo, ext = QFileDialog.getOpenFileName(self, "Open")
        if photo:
            print(photo)
            print(ext)

        self.ui.listWidget.addItems(["Alson", "Entuna"])
        QMessageBox.about(self, "Information", "Added Information...")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.setWindowTitle("Testing UI - Visualization")
    mainWindow.show()

    sys.exit(app.exec())

import sys
sys.path.insert(0, "ui")
print(sys.path)

from PySide6.QtWidgets import QApplication
from ui.mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

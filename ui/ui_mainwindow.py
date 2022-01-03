# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)

class Ui_rootWindow(object):
    def setupUi(self, rootWindow):
        if not rootWindow.objectName():
            rootWindow.setObjectName(u"rootWindow")
        rootWindow.resize(1000, 768)
        rootWindow.setMinimumSize(QSize(800, 768))
        rootWindow.setMaximumSize(QSize(1600, 900))
        rootWindow.setDocumentMode(False)
        rootWindow.setTabShape(QTabWidget.Rounded)
        rootWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionClose = QAction(rootWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.centralwidget = QWidget(rootWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnPress = QPushButton(self.centralwidget)
        self.btnPress.setObjectName(u"btnPress")

        self.gridLayout.addWidget(self.btnPress, 5, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_3)


        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_2)


        self.gridLayout.addLayout(self.formLayout_2, 1, 0, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_4)


        self.gridLayout.addLayout(self.formLayout_4, 3, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lne_name = QLineEdit(self.centralwidget)
        self.lne_name.setObjectName(u"lne_name")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lne_name)


        self.gridLayout.addLayout(self.formLayout_3, 0, 0, 1, 1)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 4, 0, 1, 1)

        rootWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(rootWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        rootWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(rootWindow)
        self.statusbar.setObjectName(u"statusbar")
        rootWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionClose)

        self.retranslateUi(rootWindow)

        QMetaObject.connectSlotsByName(rootWindow)
    # setupUi

    def retranslateUi(self, rootWindow):
        rootWindow.setWindowTitle(QCoreApplication.translate("rootWindow", u"MainWindow", None))
        self.actionClose.setText(QCoreApplication.translate("rootWindow", u"Close", None))
        self.btnPress.setText(QCoreApplication.translate("rootWindow", u"Add Information", None))
        self.label_3.setText(QCoreApplication.translate("rootWindow", u"Address:", None))
        self.label_2.setText(QCoreApplication.translate("rootWindow", u"Age:", None))
        self.label_4.setText(QCoreApplication.translate("rootWindow", u"Gender:", None))
        self.label.setText(QCoreApplication.translate("rootWindow", u"Name:", None))
        self.menuFile.setTitle(QCoreApplication.translate("rootWindow", u"File", None))
    # retranslateUi


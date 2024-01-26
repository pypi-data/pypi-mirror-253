# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stats.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_InfoWindow(object):
    def setupUi(self, InfoWindow):
        if not InfoWindow.objectName():
            InfoWindow.setObjectName(u"InfoWindow")
        InfoWindow.resize(322, 308)
        self.centralwidget = QWidget(InfoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)

        self.verticalLayout_2.addWidget(self.label)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        InfoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(InfoWindow)
        self.statusbar.setObjectName(u"statusbar")
        InfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InfoWindow)

        QMetaObject.connectSlotsByName(InfoWindow)
    # setupUi

    def retranslateUi(self, InfoWindow):
        InfoWindow.setWindowTitle(QCoreApplication.translate("InfoWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("InfoWindow", u"You are compareing the webpage on:", None))
        self.label_6.setText(QCoreApplication.translate("InfoWindow", u"<URL>", None))
        self.label_2.setText(QCoreApplication.translate("InfoWindow", u"Once a change occours the <soundfile> will be played", None))
        self.label_3.setText(QCoreApplication.translate("InfoWindow", u"upon a change the url <will/will not> be opened", None))
        self.label.setText(QCoreApplication.translate("InfoWindow", u"The process has been going on for <time>", None))
        self.label_5.setText(QCoreApplication.translate("InfoWindow", u"You've sent <requestcont> requests since <starttime>", None))
        self.pushButton.setText(QCoreApplication.translate("InfoWindow", u"Stop process", None))
    # retranslateUi


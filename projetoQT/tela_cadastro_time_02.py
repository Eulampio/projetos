# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_cadastro_time_02.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 672)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.main.setStyleSheet(u"background-color: rgb(82, 129, 89);")
        self.times_cadastro = QWidget(self.main)
        self.times_cadastro.setObjectName(u"times_cadastro")
        self.times_cadastro.setGeometry(QRect(260, 120, 701, 481))
        self.times_cadastro.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.label_times = QLabel(self.times_cadastro)
        self.label_times.setObjectName(u"label_times")
        self.label_times.setGeometry(QRect(40, 20, 141, 71))
        self.lineEdit = QLineEdit(self.times_cadastro)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 100, 631, 51))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit.setFrame(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.widget = QWidget(self.main)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(260, 40, 701, 80))
        self.widget.setStyleSheet(u"background-color: rgb(143, 191, 131);")
        self.time_nome = QLabel(self.widget)
        self.time_nome.setObjectName(u"time_nome")
        self.time_nome.setGeometry(QRect(200, 20, 301, 41))
        self.time_nome.setScaledContents(False)

        self.gridLayout.addWidget(self.main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.times_cadastro.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_times.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Time</span></p></body></html>", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Times", None))
#if QT_CONFIG(tooltip)
        self.time_nome.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">times</p><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.time_nome.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">times</p><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.time_nome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Times</span></p></body></html>", None))
    # retranslateUi

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
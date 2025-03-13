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
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import add_times_rc

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
        self.times_cadastro.setGeometry(QRect(260, 90, 701, 481))
        self.times_cadastro.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.label_times = QLabel(self.times_cadastro)
        self.label_times.setObjectName(u"label_times")
        self.label_times.setGeometry(QRect(30, 0, 141, 71))
        self.cadastrar_time = QLineEdit(self.times_cadastro)
        self.cadastrar_time.setObjectName(u"cadastrar_time")
        self.cadastrar_time.setGeometry(QRect(30, 60, 631, 51))
        self.cadastrar_time.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.cadastrar_time.setFrame(False)
        self.cadastrar_time.setClearButtonEnabled(False)
        self.label_times_2 = QLabel(self.times_cadastro)
        self.label_times_2.setObjectName(u"label_times_2")
        self.label_times_2.setGeometry(QRect(30, 110, 141, 31))
        self.label_times_3 = QLabel(self.times_cadastro)
        self.label_times_3.setObjectName(u"label_times_3")
        self.label_times_3.setGeometry(QRect(30, 150, 641, 51))
        self.label_times_3.setCursor(QCursor(Qt.CursorShape.WaitCursor))
        self.label_times_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.label_times_3.setPixmap(QPixmap(u":/add_times+/add_circle_24dp_1F1F1F_FILL0_wght400_GRAD0_opsz24 (1).svg"))
        self.label_times_3.setScaledContents(False)
        self.label_times_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_times_4 = QLabel(self.times_cadastro)
        self.label_times_4.setObjectName(u"label_times_4")
        self.label_times_4.setGeometry(QRect(30, 380, 641, 51))
        self.label_times_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.label_times_4.setPixmap(QPixmap(u":/add_times+/add_circle_24dp_1F1F1F_FILL0_wght400_GRAD0_opsz24 (1).svg"))
        self.label_times_4.setScaledContents(False)
        self.label_times_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_times_5 = QLabel(self.times_cadastro)
        self.label_times_5.setObjectName(u"label_times_5")
        self.label_times_5.setGeometry(QRect(30, 210, 141, 41))
        self.cadastrar_time_2 = QLineEdit(self.times_cadastro)
        self.cadastrar_time_2.setObjectName(u"cadastrar_time_2")
        self.cadastrar_time_2.setGeometry(QRect(30, 250, 631, 51))
        self.cadastrar_time_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.cadastrar_time_2.setFrame(False)
        self.cadastrar_time_2.setClearButtonEnabled(False)
        self.label_times_6 = QLabel(self.times_cadastro)
        self.label_times_6.setObjectName(u"label_times_6")
        self.label_times_6.setGeometry(QRect(40, 320, 141, 31))
        self.widget = QWidget(self.main)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(260, 10, 701, 80))
        self.widget.setStyleSheet(u"background-color: rgb(143, 191, 131);\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.time_nome = QLabel(self.widget)
        self.time_nome.setObjectName(u"time_nome")
        self.time_nome.setGeometry(QRect(200, 20, 301, 41))
        self.time_nome.setScaledContents(False)
        self.pushButton = QPushButton(self.main)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(510, 580, 141, 41))
        self.pushButton.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
"border: 1px solid white;\n"
"border-radius: 5px;")

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
        self.label_times.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Time 01</span></p></body></html>", None))
        self.cadastrar_time.setInputMask("")
        self.cadastrar_time.setText("")
        self.cadastrar_time.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Times", None))
        self.label_times_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ESCUDO</span></p></body></html>", None))
        self.label_times_3.setText("")
        self.label_times_4.setText("")
        self.label_times_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Time 02</span></p></body></html>", None))
        self.cadastrar_time_2.setInputMask("")
        self.cadastrar_time_2.setText("")
        self.cadastrar_time_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Times", None))
        self.label_times_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ESCUDO</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.time_nome.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">times</p><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.time_nome.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">times</p><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.time_nome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Times</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Salva</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButton.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
    # retranslateUi
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

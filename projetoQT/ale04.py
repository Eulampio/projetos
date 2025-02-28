# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ale04.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QSizePolicy, QStatusBar,
    QWidget)
import santos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1001, 572)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QRect(350, -20, 541, 511))
        self.frame_2.setMinimumSize(QSize(6, 6))
        self.frame_2.setSizeIncrement(QSize(23, 23))
        self.frame_2.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.frame_2.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.usuario = QFrame(self.frame_2)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(40, 150, 511, 41))
        self.usuario.setFrameShape(QFrame.Shape.StyledPanel)
        self.usuario.setFrameShadow(QFrame.Shadow.Raised)
        self.usuario_3 = QLabel(self.usuario)
        self.usuario_3.setObjectName(u"usuario_3")
        self.usuario_3.setGeometry(QRect(10, 10, 49, 16))
        self.digit_seu_usuario = QLineEdit(self.usuario)
        self.digit_seu_usuario.setObjectName(u"digit_seu_usuario")
        self.digit_seu_usuario.setGeometry(QRect(70, 10, 361, 22))
        self.digit_seu_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.usuario_2 = QFrame(self.usuario)
        self.usuario_2.setObjectName(u"usuario_2")
        self.usuario_2.setGeometry(QRect(430, 40, 511, 41))
        self.usuario_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.usuario_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.usuario_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 49, 16))
        self.lineEdit_2 = QLineEdit(self.usuario_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 10, 361, 22))
        self.senha_fre = QFrame(self.frame_2)
        self.senha_fre.setObjectName(u"senha_fre")
        self.senha_fre.setGeometry(QRect(20, 290, 511, 41))
        self.senha_fre.setFrameShape(QFrame.Shape.StyledPanel)
        self.senha_fre.setFrameShadow(QFrame.Shadow.Raised)
        self.senha = QLabel(self.senha_fre)
        self.senha.setObjectName(u"senha")
        self.senha.setGeometry(QRect(10, 10, 49, 16))
        self.digit_senha = QLineEdit(self.senha_fre)
        self.digit_senha.setObjectName(u"digit_senha")
        self.digit_senha.setGeometry(QRect(70, 10, 361, 22))
        self.digit_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.usuario_4 = QFrame(self.senha_fre)
        self.usuario_4.setObjectName(u"usuario_4")
        self.usuario_4.setGeometry(QRect(430, 40, 511, 41))
        self.usuario_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.usuario_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.usuario_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 49, 16))
        self.lineEdit_5 = QLineEdit(self.usuario_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(70, 10, 361, 22))
        self.login = QLabel(self.frame_2)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(160, 40, 161, 51))
        font = QFont()
        font.setFamilies([u"Myanmar Text"])
        font.setPointSize(22)
        self.login.setFont(font)
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(190, 460, 101, 20))
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 330, 141, 121))
        self.label.setPixmap(QPixmap(u":/alesan/imagem/b36374ee2e63bf9a25acb156cc3651f0.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 350, 151, 111))
        self.label_3.setPixmap(QPixmap(u":/alesan/imagem/woll.png"))
        self.label_3.setScaledContents(True)
        self.login.raise_()
        self.senha_fre.raise_()
        self.usuario.raise_()
        self.checkBox.raise_()
        self.label.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.usuario_3.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.senha.setText(QCoreApplication.translate("MainWindow", u"senha", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o sou Roboo", None))
        self.label.setText("")
        self.label_3.setText("")
    # retranslateUi

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

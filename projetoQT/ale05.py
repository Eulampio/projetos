# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ale05.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)
import santos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(774, 717)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(-850, -60, 1961, 851))
        self.widget_dados = QWidget(self.widget_6)
        self.widget_dados.setObjectName(u"widget_dados")
        self.widget_dados.setGeometry(QRect(880, 100, 711, 651))
        self.widget_dados.setAutoFillBackground(False)
        self.widget_dados.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.widget_3 = QWidget(self.widget_dados)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(30, 370, 351, 41))
        self.edit_estado_civil = QTextEdit(self.widget_3)
        self.edit_estado_civil.setObjectName(u"edit_estado_civil")
        self.edit_estado_civil.setGeometry(QRect(100, 10, 201, 21))
        self.edit_estado_civil.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.estado_civil = QLabel(self.widget_3)
        self.estado_civil.setObjectName(u"estado_civil")
        self.estado_civil.setGeometry(QRect(0, 10, 91, 16))
        self.widget_4 = QWidget(self.widget_dados)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(30, 440, 341, 41))
        self.edit_naturalidade = QTextEdit(self.widget_4)
        self.edit_naturalidade.setObjectName(u"edit_naturalidade")
        self.edit_naturalidade.setGeometry(QRect(120, 10, 201, 21))
        self.edit_naturalidade.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.edit_naturalidade.setInputMethodHints(Qt.InputMethodHint.ImhDate)
        self.naturalidade = QLabel(self.widget_4)
        self.naturalidade.setObjectName(u"naturalidade")
        self.naturalidade.setGeometry(QRect(0, 10, 91, 16))
        self.widget_5 = QWidget(self.widget_dados)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(30, 500, 331, 41))
        self.edit_codigo = QTextEdit(self.widget_5)
        self.edit_codigo.setObjectName(u"edit_codigo")
        self.edit_codigo.setGeometry(QRect(100, 10, 221, 21))
        self.edit_codigo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 10, 91, 16))
        self.widget_nascimento = QWidget(self.widget_dados)
        self.widget_nascimento.setObjectName(u"widget_nascimento")
        self.widget_nascimento.setGeometry(QRect(30, 590, 321, 41))
        self.textEdit = QTextEdit(self.widget_nascimento)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(130, 10, 181, 21))
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.data_nasc = QLabel(self.widget_nascimento)
        self.data_nasc.setObjectName(u"data_nasc")
        self.data_nasc.setGeometry(QRect(0, 10, 111, 16))
        self.frame = QFrame(self.widget_dados)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 290, 701, 80))
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(40, 30, 601, 22))
        self.lineEdit_3.setMouseTracking(True)
        self.lineEdit_3.setTabletTracking(False)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.email = QLabel(self.frame)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(0, 30, 49, 16))
        self.email.raise_()
        self.lineEdit_3.raise_()
        self.widget_2 = QWidget(self.widget_dados)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(370, 370, 259, 38))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.opc_sexo = QLabel(self.widget_2)
        self.opc_sexo.setObjectName(u"opc_sexo")

        self.horizontalLayout.addWidget(self.opc_sexo)

        self.opc_masculino = QCheckBox(self.widget_2)
        self.opc_masculino.setObjectName(u"opc_masculino")

        self.horizontalLayout.addWidget(self.opc_masculino)

        self.opc_feminino = QCheckBox(self.widget_2)
        self.opc_feminino.setObjectName(u"opc_feminino")

        self.horizontalLayout.addWidget(self.opc_feminino)

        self.opc_outros = QCheckBox(self.widget_2)
        self.opc_outros.setObjectName(u"opc_outros")

        self.horizontalLayout.addWidget(self.opc_outros)

        self.widget = QWidget(self.widget_dados)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 150, 571, 151))
        self.digite_cpf = QLineEdit(self.widget)
        self.digite_cpf.setObjectName(u"digite_cpf")
        self.digite_cpf.setGeometry(QRect(90, 20, 113, 22))
        self.digite_cpf.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cpf = QLabel(self.widget)
        self.cpf.setObjectName(u"cpf")
        self.cpf.setGeometry(QRect(20, 20, 49, 16))
        self.nome_Pf = QLabel(self.widget)
        self.nome_Pf.setObjectName(u"nome_Pf")
        self.nome_Pf.setGeometry(QRect(300, 20, 49, 16))
        self.digite_nome = QLineEdit(self.widget)
        self.digite_nome.setObjectName(u"digite_nome")
        self.digite_nome.setGeometry(QRect(360, 20, 113, 22))
        self.digite_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_4 = QLineEdit(self.widget_dados)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(160, 30, 281, 71))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(16)
        self.lineEdit_4.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 774, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.edit_estado_civil.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.estado_civil.setText(QCoreApplication.translate("MainWindow", u"Estado Civil", None))
        self.edit_naturalidade.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.naturalidade.setText(QCoreApplication.translate("MainWindow", u"Naturalidade:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.data_nasc.setText(QCoreApplication.translate("MainWindow", u"Nascimento:", None))
        self.email.setText(QCoreApplication.translate("MainWindow", u"email:", None))
        self.opc_sexo.setText(QCoreApplication.translate("MainWindow", u"Sexo:", None))
        self.opc_masculino.setText(QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.opc_feminino.setText(QCoreApplication.translate("MainWindow", u"Feminio", None))
        self.opc_outros.setText(QCoreApplication.translate("MainWindow", u"Outro", None))
        self.cpf.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.nome_Pf.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"Cadastro pessoa fisica", None))
    # retranslateUi

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
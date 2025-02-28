# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_cadastro_times.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1068, 757)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 10, 1051, 701))
        self.frame.setStyleSheet(u"background-color: rgb(42, 83, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.cadastro_times = QTabWidget(self.frame)
        self.cadastro_times.setObjectName(u"cadastro_times")
        self.cadastro_times.setGeometry(QRect(190, 130, 731, 481))
        self.cadastro_times.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cadastro_clie = QWidget()
        self.cadastro_clie.setObjectName(u"cadastro_clie")
        self.widget = QWidget(self.cadastro_clie)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 721, 451))
        self.deletar_times = QToolButton(self.widget)
        self.deletar_times.setObjectName(u"deletar_times")
        self.deletar_times.setGeometry(QRect(360, 380, 151, 21))
        self.salar_times = QToolButton(self.widget)
        self.salar_times.setObjectName(u"salar_times")
        self.salar_times.setGeometry(QRect(110, 380, 151, 21))
        self.salar_times.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.salar_times.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.salar_times.setAutoRaise(False)
        self.salar_times.setArrowType(Qt.ArrowType.NoArrow)
        self.gol_times = QLineEdit(self.widget)
        self.gol_times.setObjectName(u"gol_times")
        self.gol_times.setGeometry(QRect(60, 290, 431, 22))
        self.times = QLineEdit(self.widget)
        self.times.setObjectName(u"times")
        self.times.setGeometry(QRect(60, 110, 431, 22))
        self.posicao_times = QLineEdit(self.widget)
        self.posicao_times.setObjectName(u"posicao_times")
        self.posicao_times.setGeometry(QRect(60, 200, 431, 22))
        self.buscar_times = QLineEdit(self.widget)
        self.buscar_times.setObjectName(u"buscar_times")
        self.buscar_times.setGeometry(QRect(160, 40, 151, 22))
        self.cadastro_times.addTab(self.cadastro_clie, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 390, 731, 431))
        self.widget_2 = QWidget(self.tab_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 721, 441))
        self.tela_cadastro_de_times = QTableWidget(self.widget_2)
        if (self.tela_cadastro_de_times.columnCount() < 3):
            self.tela_cadastro_de_times.setColumnCount(3)
        font = QFont()
        font.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tela_cadastro_de_times.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tela_cadastro_de_times.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tela_cadastro_de_times.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tela_cadastro_de_times.rowCount() < 12):
            self.tela_cadastro_de_times.setRowCount(12)
        font1 = QFont()
        font1.setWeight(QFont.Thin)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tela_cadastro_de_times.setItem(0, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tela_cadastro_de_times.setItem(1, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tela_cadastro_de_times.setItem(2, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.tela_cadastro_de_times.setItem(3, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.tela_cadastro_de_times.setItem(4, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.tela_cadastro_de_times.setItem(5, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.tela_cadastro_de_times.setItem(6, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.tela_cadastro_de_times.setItem(7, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.tela_cadastro_de_times.setItem(8, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        self.tela_cadastro_de_times.setItem(9, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        self.tela_cadastro_de_times.setItem(10, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.tela_cadastro_de_times.setItem(11, 1, __qtablewidgetitem14)
        self.tela_cadastro_de_times.setObjectName(u"tela_cadastro_de_times")
        self.tela_cadastro_de_times.setGeometry(QRect(200, 30, 331, 391))
        self.cadastro_times.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1068, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.cadastro_times.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.deletar_times.setText(QCoreApplication.translate("MainWindow", u"DELETAR", None))
        self.salar_times.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.gol_times.setText("")
        self.gol_times.setPlaceholderText(QCoreApplication.translate("MainWindow", u"GOLS", None))
        self.times.setText("")
        self.times.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TIMES", None))
        self.posicao_times.setText("")
        self.posicao_times.setPlaceholderText(QCoreApplication.translate("MainWindow", u"POSI\u00c7\u00c3O", None))
        self.buscar_times.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.cadastro_times.setTabText(self.cadastro_times.indexOf(self.cadastro_clie), QCoreApplication.translate("MainWindow", u"CADASTRO TIMES", None))
        self.label_2.setText("")
        ___qtablewidgetitem = self.tela_cadastro_de_times.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"TIMES", None));
        ___qtablewidgetitem1 = self.tela_cadastro_de_times.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"POSI\u00c7\u00c3O", None));
        ___qtablewidgetitem2 = self.tela_cadastro_de_times.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"GOLS", None));

        __sortingEnabled = self.tela_cadastro_de_times.isSortingEnabled()
        self.tela_cadastro_de_times.setSortingEnabled(False)
        self.tela_cadastro_de_times.setSortingEnabled(__sortingEnabled)

        self.cadastro_times.setTabText(self.cadastro_times.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"TIMES", None))
    # retranslateUi


import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
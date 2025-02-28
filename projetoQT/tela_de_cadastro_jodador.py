# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_de_cadastro_jodador.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLineEdit, QMainWindow, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1092, 899)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(82, 129, 89);")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(82, 129, 89);")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.CADASTRO = QTabWidget(self.widget)
        self.CADASTRO.setObjectName(u"CADASTRO")
        self.CADASTRO.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cadastro_jogador = QWidget()
        self.cadastro_jogador.setObjectName(u"cadastro_jogador")
        self.gridLayout_4 = QGridLayout(self.cadastro_jogador)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame = QFrame(self.cadastro_jogador)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buscar_times = QLineEdit(self.frame)
        self.buscar_times.setObjectName(u"buscar_times")

        self.gridLayout.addWidget(self.buscar_times, 0, 0, 1, 2)

        self.jogador = QLineEdit(self.frame)
        self.jogador.setObjectName(u"jogador")

        self.gridLayout.addWidget(self.jogador, 1, 0, 1, 2)

        self.posicao_jogadr = QLineEdit(self.frame)
        self.posicao_jogadr.setObjectName(u"posicao_jogadr")

        self.gridLayout.addWidget(self.posicao_jogadr, 2, 0, 1, 2)

        self.gol_jogador = QLineEdit(self.frame)
        self.gol_jogador.setObjectName(u"gol_jogador")

        self.gridLayout.addWidget(self.gol_jogador, 3, 0, 1, 2)

        self.salvar_jogador = QToolButton(self.frame)
        self.salvar_jogador.setObjectName(u"salvar_jogador")

        self.gridLayout.addWidget(self.salvar_jogador, 4, 0, 1, 1)

        self.toolButton_2 = QToolButton(self.frame)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.gridLayout.addWidget(self.toolButton_2, 4, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        self.CADASTRO.addTab(self.cadastro_jogador, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_2 = QWidget(self.tab_3)
        self.widget_2.setObjectName(u"widget_2")
        self.tabela_jogadores = QTableWidget(self.widget_2)
        if (self.tabela_jogadores.columnCount() < 3):
            self.tabela_jogadores.setColumnCount(3)
        font = QFont()
        font.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tabela_jogadores.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_jogadores.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tabela_jogadores.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tabela_jogadores.rowCount() < 12):
            self.tabela_jogadores.setRowCount(12)
        font1 = QFont()
        font1.setWeight(QFont.Thin)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tabela_jogadores.setItem(0, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tabela_jogadores.setItem(1, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tabela_jogadores.setItem(2, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.tabela_jogadores.setItem(3, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.tabela_jogadores.setItem(4, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.tabela_jogadores.setItem(5, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.tabela_jogadores.setItem(6, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.tabela_jogadores.setItem(7, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.tabela_jogadores.setItem(8, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        self.tabela_jogadores.setItem(9, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        self.tabela_jogadores.setItem(10, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.tabela_jogadores.setItem(11, 1, __qtablewidgetitem14)
        self.tabela_jogadores.setObjectName(u"tabela_jogadores")
        self.tabela_jogadores.setGeometry(QRect(660, 180, 331, 391))

        self.horizontalLayout_3.addWidget(self.widget_2)

        self.CADASTRO.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.CADASTRO, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.CADASTRO.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buscar_times.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.jogador.setText("")
        self.jogador.setPlaceholderText(QCoreApplication.translate("MainWindow", u"JOGADOR", None))
        self.posicao_jogadr.setText("")
        self.posicao_jogadr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"POSI\u00c7\u00c3O", None))
        self.gol_jogador.setText("")
        self.gol_jogador.setPlaceholderText(QCoreApplication.translate("MainWindow", u"GOL", None))
        self.salvar_jogador.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"DELETAR", None))
        self.CADASTRO.setTabText(self.CADASTRO.indexOf(self.cadastro_jogador), QCoreApplication.translate("MainWindow", u"CADASTRO JOGADORE", None))
        ___qtablewidgetitem = self.tabela_jogadores.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"JOGADOR", None));
        ___qtablewidgetitem1 = self.tabela_jogadores.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"POSI\u00c7\u00c3O", None));
        ___qtablewidgetitem2 = self.tabela_jogadores.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"GOL", None));

        __sortingEnabled = self.tabela_jogadores.isSortingEnabled()
        self.tabela_jogadores.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.tabela_jogadores.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        ___qtablewidgetitem4 = self.tabela_jogadores.item(1, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        ___qtablewidgetitem5 = self.tabela_jogadores.item(2, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        ___qtablewidgetitem6 = self.tabela_jogadores.item(3, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        ___qtablewidgetitem7 = self.tabela_jogadores.item(4, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        ___qtablewidgetitem8 = self.tabela_jogadores.item(5, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        ___qtablewidgetitem9 = self.tabela_jogadores.item(6, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        ___qtablewidgetitem10 = self.tabela_jogadores.item(7, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        ___qtablewidgetitem11 = self.tabela_jogadores.item(8, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        ___qtablewidgetitem12 = self.tabela_jogadores.item(9, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        ___qtablewidgetitem13 = self.tabela_jogadores.item(10, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        ___qtablewidgetitem14 = self.tabela_jogadores.item(11, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        self.tabela_jogadores.setSortingEnabled(__sortingEnabled)

        self.CADASTRO.setTabText(self.CADASTRO.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"JOGADORES", None))
    # retranslateUi


import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
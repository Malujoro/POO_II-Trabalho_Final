# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaGerenciar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 840)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLogo = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogo.setGeometry(QtCore.QRect(10, 0, 71, 71))
        self.btnLogo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogo.setStyleSheet("\n"
                                   "QPushButton {  \n"
                                   "    background-color: rgb(0, 75, 63);\n"
                                   "   font: 15pt \"Cooper Black\";\n"
                                   "    color: rgb(255, 255, 255); /* Cor do texto */\n"
                                   "    border-radius: 8px; /* Bordas arredondadas */\n"
                                   "    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
                                   "image:url(:/images/images/logofolha.png)\n"
                                   "    \n"
                                   "       \n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "\n"
                                   "")
        self.btnLogo.setText("")
        self.btnLogo.setObjectName("btnLogo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 931, 71))
        self.label_2.setStyleSheet("background-color: rgb(0, 75, 63);\n"
"\n"
"\n"
"")


        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 90, 301, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 670, 931, 161))
        self.label_8.setStyleSheet("background-color: rgb(0, 75, 63);\n"
"\n"
"\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.btnNomelogo = QtWidgets.QPushButton(self.centralwidget)
        self.btnNomelogo.setGeometry(QtCore.QRect(70, 10, 181, 51))
        self.btnNomelogo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNomelogo.setStyleSheet("\n"

                                       "QPushButton {  \n"
                                       "    background-color: rgb(0, 75, 63);\n"
                                       "   font: 15pt \"Cooper Black\";\n"
                                       "    color: rgb(255, 255, 255); /* Cor do texto */\n"
                                       "    border-radius: 8px; /* Bordas arredondadas */\n"
                                       "    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
                                       "    \n"
                                       "       \n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "")
        self.btnNomelogo.setObjectName("btnNomelogo")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(20, 680, 321, 131))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_25 = QtWidgets.QLabel(self.frame_5)
        self.label_25.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_5)
        self.label_26.setGeometry(QtCore.QRect(10, 30, 301, 91))
        self.label_26.setObjectName("label_26")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(420, 680, 181, 131))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_27 = QtWidgets.QLabel(self.frame_6)
        self.label_27.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame_6)
        self.label_28.setGeometry(QtCore.QRect(10, 30, 301, 91))
        self.label_28.setObjectName("label_28")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(710, 680, 171, 131))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_29 = QtWidgets.QLabel(self.frame_7)
        self.label_29.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame_7)
        self.label_30.setGeometry(QtCore.QRect(10, 30, 301, 91))
        self.label_30.setObjectName("label_30")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(70, 140, 800, 480))  # 14cm x 8cm em pixels (1cm = 100 pixels)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet("""
            QTableWidget {
                background-color: #e6ffe6;  # Fundo verde claro
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            QTableWidget::item {
                padding: 10px;
            }
            QTableWidget::horizontalHeader {
                background-color: #004b3f;  # Verde escuro
                color: white;
                font: bold;
            }
            QTableWidget::item:selected {
                background-color: #ccffcc;  # Fundo verde claro para item selecionado
            }
            QTableWidget::item:hover {
                background-color: #b3ffb3;  # Fundo verde claro para item em foco
            }
            QTableWidget::gridline-color {
                color: #004b3f;  # Verde escuro para linhas
            }
        """)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(50, 30, 700, 400))  # Tamanho proporcional e centralizado
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(50, 30, 700, 400))  # Tamanho proporcional e centralizado
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab_2, "")

        # Ajustando a largura das colunas
        self.tableWidget.setColumnWidth(0, 429)  # Produto - maior largura
        self.tableWidget.setColumnWidth(1, 150)  # Valor - largura menor
        self.tableWidget.setColumnWidth(2, 100)  # Quantidade - largura menor

        # Ajustando a largura das colunas
        self.tableWidget_2.setColumnWidth(0, 180)  # nome - maior largura
        self.tableWidget_2.setColumnWidth(1, 290)  # produtos - largura menor
        self.tableWidget_2.setColumnWidth(2, 90)  # Valor - largura menor
        self.tableWidget_2.setColumnWidth(3, 119)  # data/hora limite - largura menor

        # Adicionando funcionalidade de atualização
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(400, 625, 100, 30))
        self.updateButton.setObjectName("updateButton")
        self.updateButton.setText("Atualizar")
        self.updateButton.setStyleSheet("QPushButton {  \n"
                                    "    background-color: rgb(0, 75, 63);\n"
                                    "    font: 75 7pt \"MS Shell Dlg 2\";\n"
                                    "    color: rgb(255, 255, 255); /* Cor do texto */\n"
                                    "    border-radius: 8px; /* Bordas arredondadas */\n"
                                    "    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
                                    "    text-align: center; /* Centraliza o texto */    \n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "  background-color: #E5E5E5;\n"
                                    "    font: 75 7pt \"MS Shell Dlg 2\";\n"
                                    "    color: rgb(255, 255, 255); /* Cor do texto */\n"
                                    "    border-radius: 8px; /* Bordas arredondadas */\n"
                                    "    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
                                    "    text-align: center; /* Centraliza o texto */\n"
                                    "border: 1px solid #CCCCCC;\n"
                                    "box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "background-color: #E5E5E5;\n"
                                    "    font: 75 7pt \"MS Shell Dlg 2\";\n"
                                    "    color: rgb(255, 255, 255); /* Cor do texto */\n"
                                    "    border-radius: 8px; /* Bordas arredondadas */\n"
                                    "    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
                                    "    text-align: center; /* Centraliza o texto */\n"
                                    "border: 1px solid #CCCCCC;\n"
                                    "box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
                                    "background-color: #D6D6D6; /* Fundo mais escuro */\n"
                                    "    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2); /* Menor sombra */\n"
                                    "    transform: translateY(2px); /* Deslocamento para baixo */\n"
                                    "    border: 1px solid #AAAAAA; /* Borda mais escura */\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.updateButton.setObjectName("updateButton")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Adicionando linhas de exemplo na primeira aba
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem("Produto Exemplo"))
        self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem("R$ 10,00"))
        self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem("100"))

        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem("Produto Exemplo 2"))
        self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem("R$ 10,00"))
        self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem("100"))

        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        # Adicionando linhas de exemplo na segunda aba
        row_position_2 = self.tableWidget_2.rowCount()
        self.tableWidget_2.insertRow(row_position_2)
        self.tableWidget_2.setItem(row_position_2, 0, QtWidgets.QTableWidgetItem("Gabriel"))
        self.tableWidget_2.setItem(row_position_2, 1, QtWidgets.QTableWidgetItem("Viagra"))
        self.tableWidget_2.setItem(row_position_2, 2, QtWidgets.QTableWidgetItem("R$100,00"))
        self.tableWidget_2.setItem(row_position_2, 3, QtWidgets.QTableWidgetItem("24/01/2025"))

        row_position_2 = self.tableWidget_2.rowCount()
        self.tableWidget_2.insertRow(row_position_2)
        self.tableWidget_2.setItem(row_position_2, 0, QtWidgets.QTableWidgetItem("Gabriel"))
        self.tableWidget_2.setItem(row_position_2, 1, QtWidgets.QTableWidgetItem("Viagra"))
        self.tableWidget_2.setItem(row_position_2, 2, QtWidgets.QTableWidgetItem("R$100,00"))
        self.tableWidget_2.setItem(row_position_2, 3, QtWidgets.QTableWidgetItem("24/01/2025"))

        row_position_2 = self.tableWidget_2.rowCount()
        self.tableWidget_2.insertRow(row_position_2)



        self.label_8.raise_()
        self.label_2.raise_()
        self.label_7.raise_()
        self.btnNomelogo.raise_()
        self.btnLogo.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerenciar"))
        icon = QtGui.QIcon(":/images/images/logofolha.png")  # Caminho para sua imagem de logo
        MainWindow.setWindowIcon(icon)
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#004b3f;\">GERENCIAR ESTOQUE E RESERVAS</span></p></body></html>"))
        self.btnNomelogo.setWhatsThis(
                _translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.btnNomelogo.setText(_translate("MainWindow", "DrogaLaugh"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Sobre Nós</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">A DrogaLaugh é sua farmácia de confiança, oferecendo</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> produtos de qualidade e atendimento excepcional </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">desde 2024.</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Contatos</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">0800 123 4567</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">contato@drogalaugh.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Junco, 123</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Picos - PI</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Redes Sociais</span></p></body></html>"))
        self.label_30.setText(_translate(
            "MainWindow",
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p { white-space: nowrap; margin: 5px 0; display: flex; align-items: center; }\n"
            "img { margin-right: 8px; vertical-align: center; }\n"
            "span { font-size: 12px; color: #ffffff; }\n"
            "</style></head>\n"
            "<body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
            "<p><img src=\":/images/images/instagram.png\" height=\"16\" width=\"16\" /><span> @droga_laugh</span></p>\n"
            "<p><img src=\":/images/images/facebook.png\" height=\"16\" width=\"16\" /><span> Droga Laugh</span></p>\n"
            "</body></html>"
        ))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Produto"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Valor"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantidade"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Gerenciar Estoque"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Produtos"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Valor Total"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data/hora limite"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Gerenciar Reservas"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
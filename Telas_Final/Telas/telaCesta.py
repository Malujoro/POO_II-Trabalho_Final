# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaCesta.ui'
# Created by: PyQt5 UI code generator 5.15.11

from PyQt5 import QtCore, QtGui, QtWidgets


class TelaCestaUi(object):
    def setupUi(self, MainWindow):
        # Configuração principal da janela
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 840)
        icon = QtGui.QIcon(":/images/images/logofolha.png")  # Ícone da janela
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Frame principal
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(560, 10, 351, 791))
        self.frame_8.setStyleSheet("background-color: rgb(255, 255, 255);\nborder-radius: 15px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setObjectName("frame_8")

        # Título do frame
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 300, 41))
        self.label_7.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2';")
        self.label_7.setObjectName("label_7")

        # Título do frame
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 180, 41))
        self.label_3.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2';")
        self.label_3.setObjectName("label_3")

        # Linha decorativa
        self.label_8 = QtWidgets.QLabel(self.frame_8)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 321, 16))
        self.label_8.setStyleSheet("color:rgb(0, 120, 100)")
        self.label_8.setObjectName("label_8")

        # Campo de texto para Nome
        self.text_nome = QtWidgets.QLineEdit(self.frame_8)
        self.text_nome.setGeometry(QtCore.QRect(30, 70, 291, 31))
        self.text_nome.setPlaceholderText("Insira seu nome")
        self.text_nome.setStyleSheet("font: 10pt 'MS Shell Dlg 2';\npadding: 5px;\nborder: 1px solid #CCCCCC;\nborder-radius: 5px;")
        self.text_nome.setObjectName("text_nome")

        # Campo de texto para CPF
        self.text_cpf = QtWidgets.QLineEdit(self.frame_8)
        self.text_cpf.setGeometry(QtCore.QRect(30, 110, 291, 31))
        self.text_cpf.setPlaceholderText("Insira seu CPF")
        self.text_cpf.setStyleSheet("font: 10pt 'MS Shell Dlg 2';\npadding: 5px;\nborder: 1px solid #CCCCCC;\nborder-radius: 5px;")
        self.text_cpf.setObjectName("text_cpf")

        # Campo para Data e Hora
        self.date_time_edit = QtWidgets.QDateTimeEdit(self.frame_8)
        self.date_time_edit.setGeometry(QtCore.QRect(30, 150, 291, 31))
        self.date_time_edit.setStyleSheet(
            "font: 10pt 'MS Shell Dlg 2';\npadding: 5px;\nborder: 1px solid #CCCCCC;\nborder-radius: 5px;")
        self.date_time_edit.setObjectName("date_time_edit")

        # Configurando o formato de exibição
        self.date_time_edit.setDisplayFormat("dd/MM/yyyy HH:mm:ss")

        # Configurando o valor inicial (data e hora atual)
        self.date_time_edit.setDateTime(QtCore.QDateTime.currentDateTime())

        # Configurando limites de 8 dias
        current_date = QtCore.QDateTime.currentDateTime()
        self.date_time_edit.setMinimumDateTime(current_date)  # Hoje
        self.date_time_edit.setMaximumDateTime(current_date.addDays(8))

        # Linha decorativa
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        self.label_6.setGeometry(QtCore.QRect(20, 48, 321, 16))
        self.label_6.setStyleSheet("color:rgb(0, 120, 100)")
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setGeometry(QtCore.QRect(30, 230, 51, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        # Botão "Reservar Produtos"
        self.botaoCesta = QtWidgets.QPushButton(self.frame_8)
        self.botaoCesta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botaoCesta.setGeometry(QtCore.QRect(100, 710, 171, 38))
        self.botaoCesta.setStyleSheet("""
            QPushButton {
                background-color: rgb(0, 75, 63);
                font: 75 9pt 'MS Shell Dlg 2';
                color: rgb(255, 255, 255);
                border-radius: 8px;
                padding: 10px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #E5E5E5;
                border: 1px solid #CCCCCC;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            QPushButton:pressed {
                background-color: #D6D6D6;
                box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2);
                transform: translateY(2px);
                border: 1px solid #AAAAAA;
            }
        """)
        self.botaoCesta.setObjectName("botaoCesta")

        # Exemplo de item na cesta (Frame interno)
        self.frame_2 = QtWidgets.QFrame(self.frame_8)
        self.frame_2.setGeometry(QtCore.QRect(20, 250, 321, 111))
        self.frame_2.setStyleSheet("border-radius:8px;")
        self.frame_2.setObjectName("frame_2")

        # Imagem do item
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 91, 81))
        self.label_4.setStyleSheet("image: url(:/images/images/medicina-natural.png);")
        self.label_4.setObjectName("label_4")

        # Descrição do item
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(100, 30, 151, 31))
        self.label_5.setObjectName("label_5")

        # Preço do item
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(100, 60, 71, 21))
        self.label_9.setStyleSheet("font: 75 8pt 'MS Shell Dlg 2';\ncolor:rgb(0, 75, 63)")
        self.label_9.setObjectName("label_9")

        # Preço antigo do item (com risco)

        # Botão para remover item
        self.botaoCesta_2 = QtWidgets.QPushButton(self.frame_2)
        self.botaoCesta_2.setGeometry(QtCore.QRect(270, 30, 41, 38))
        self.botaoCesta_2.setStyleSheet("QPushButton {  \n"
                                        "     font: 75 9pt \"MS Shell Dlg 2\";\n"
                                        "    color: rgb(255, 255, 255); /* Cor do texto */\n"
                                        "    border-radius: 8px; /* Bordas arredondadas */\n"
                                        "    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
                                        "      image: url(:/images/images/lixeira-de-reciclagem.png);\n"
                                        "    image-position:left;   \n"
                                        "    text-align: right; /* Centraliza o texto */    \n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "  background-color: #E5E5E5;\n"
                                        "    font: 75 9pt \"MS Shell Dlg 2\";\n"
                                        "    color: rgb(255, 255, 255); /* Cor do texto */\n"
                                        "    border-radius: 8px; /* Bordas arredondadas */\n"
                                        "    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
                                        "    \n"
                                        "    image-position:left;   \n"
                                        "    text-align: right; /* Centraliza o texto */\n"
                                        "border: 1px solid #CCCCCC;\n"
                                        "box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: #E5E5E5;\n"
                                        "    font: 75 9pt \"MS Shell Dlg 2\";\n"
                                        "    color: rgb(255, 255, 255); /* Cor do texto */\n"
                                        "    border-radius: 8px; /* Bordas arredondadas */\n"
                                        "    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
                                        "    \n"
                                        "    image-position:left;   \n"
                                        "    text-align: right; /* Centraliza o texto */\n"
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
        self.botaoCesta_2.setText("")
        self.botaoCesta_2.setObjectName("botaoCesta_2")

        # Campo para alterar quantidade
        self.spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QtCore.QRect(260, 70, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(50)
        self.spinBox.setValue(1)
        self.spinBox.setObjectName("spinBox")

        # Configuração do status e central widget
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Reatribuir texto aos componentes
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cesta de Produtos"))
        icon = QtGui.QIcon(":/images/images/logofolha.png")  # Caminho para sua imagem de logo
        MainWindow.setWindowIcon(icon)
        self.label_7.setText(_translate("MainWindow", "Informações para reserva:"))
        self.label_3.setText(_translate("MainWindow", "Produtos na Cesta:"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" color:#004b3f;\">1 item</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "____________________________________________"))
        self.label_8.setText(_translate("MainWindow", "____________________________________________"))
        self.botaoCesta.setText(_translate("MainWindow", "RESERVAR PRODUTOS"))
        self.label_5.setText(_translate("MainWindow", "Vitamina C 1000mg"))
        self.label_9.setText(_translate("MainWindow", "R$ 76.42"))

# Execução da aplicação
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaCestaUi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

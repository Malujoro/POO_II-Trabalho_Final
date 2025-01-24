# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaCesta.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unle    ss you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class TelaCestaUi(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 840)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(560, 10, 351, 791))
        self.frame_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 15px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 61, 41))
        self.label_3.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 51, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.botaoCesta = QtWidgets.QPushButton(self.frame_8)
        self.botaoCesta.setGeometry(QtCore.QRect(100, 710, 171, 38))
        self.botaoCesta.setStyleSheet("QPushButton {  \n"
"    background-color: rgb(0, 75, 63);\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"  \n"
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
        self.botaoCesta.setObjectName("botaoCesta")
        self.frame_2 = QtWidgets.QFrame(self.frame_8)
        self.frame_2.setGeometry(QtCore.QRect(20, 100, 321, 111))
        self.frame_2.setStyleSheet("border-radius:8px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 91, 81))
        self.label_4.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius:8px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(100, 30, 151, 31))
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(100, 60, 71, 21))
        self.label_9.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 75, 63)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(160, 60, 55, 21))
        self.label_10.setStyleSheet("font: 6pt \"MS Shell Dlg 2\";\n"
"text-decoration: line-through;")
        self.label_10.setObjectName("label_10")
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
        self.spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QtCore.QRect(260, 70, 42, 22))
        self.spinBox.setObjectName("spinBox")
        # Definir o valor mínimo, máximo e valor inicial
        estoque_maximo = 50  # Exemplo de estoque máximo
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(estoque_maximo)
        self.spinBox.setValue(1)  # Valor inicial
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 321, 16))
        self.label_6.setStyleSheet("color:rgb(0, 120, 100)")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cesta de Produtos"))
        icon = QtGui.QIcon(":/images/images/logofolha.png")  # Caminho para sua imagem de logo
        MainWindow.setWindowIcon(icon)
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Cesta</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#004b3f;\">1 item</span></p></body></html>"))
        self.botaoCesta.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.botaoCesta.setText(_translate("MainWindow", "RESERVAR PRODUTOS"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Vitamina C 1000mg</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">R$ 76.42 </span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>R$ 89.90</p></body></html>"))
        self.botaoCesta_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "____________________________________________"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaCestaUi()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

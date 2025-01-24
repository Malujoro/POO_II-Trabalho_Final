from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
import sys
from telaCestaVazia import TelaCestaVazia
from telaCesta import TelaCesta
from telaGerenciar import TelaGerenciar
from Telas.telaPrincipal import TelaPrincipalUi
# from ..telaChat import TelaChat
import Telas.images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaPrincipal(TelaPrincipalUi):

    def __init__(self, mainWindow):
        super().setupUi(mainWindow)
        mainWindow.show()
        self.mainWindow = QtWidgets.QMainWindow()

        self.botaoCesta.clicked.connect(self.cesta_tela)

        self.botaoReservar.clicked.connect(self.reservar_produtos_tela)

        # self.botaoChat.clicked.connect(self.chat_tela)


    def cesta_tela(self):
        self.nova_tela = TelaCesta(self.mainWindow)
    
    def cesta_vazia_tela(self):
        self.nova_tela = TelaCestaVazia()  

    def reservar_produtos_tela(self):
        print("reservar")
        pass
        # self.nova_tela = ...
        
    # def chat_tela(self):
    #     self.nova_tela = TelaChat()


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    tela = TelaPrincipal(MainWindow)
    sys.exit(app.exec_())   
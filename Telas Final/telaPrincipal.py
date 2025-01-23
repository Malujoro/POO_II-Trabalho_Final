from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from telaCestaVazia import TelaCestaVazia
from telaCesta import TelaCesta
from telaGerenciar import TelaGerenciar
from telaOfertas import TelaOfertas
from telaBuscar import TelaBuscar
from telaBuscarVazia import TelaBuscarVazia
from telaChat import TelaChat
import images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaPrincipal(QMainWindow):
    
    def __init__(self):

        super().__init__()
        uic.loadUi(os.path.join(current_dir, 'ui/telaPrincipal.ui'), self)

        self.botao_cesta = self.findChild(QPushButton, "botaoCesta") 
        self.botao_cesta.clicked.connect(self.cesta_tela)

        self.botao_buscar = self.findChild(QPushButton, "botaoBuscar")
        self.botao_buscar.clicked.connect(self.buscar_tela)
        
        self.botao_reservar = self.findChild(QPushButton, "BotaoReservar")
        self.botao_reservar.clicked.connect(self.reservar_produtos_tela)

        self.botao_ofertas = self.findChild(QPushButton, "botaoOfertas")
        self.botao_ofertas.clicked.connect(self.ofertas_tela)

        self.botao_chat = self.findChild(QPushButton, "botaoChat")
        self.botao_chat.clicked.connect(self.chat_tela)

        
    def cesta_tela(self):
        self.nova_tela = TelaCesta()  
        self.nova_tela.show()  
    
    def cesta_vazia_tela(self):
        self.nova_tela = TelaCestaVazia()  
        self.nova_tela.show()  

    def reservar_produtos_tela(self):
        print("reservar")
        pass
        # self.nova_tela = ...
        # self.nova_tela.show()

    def ofertas_tela(self):
        self.nova_tela = TelaOfertas()
        self.nova_tela.show()
        
    def chat_tela(self):
        self.nova_tela = TelaChat()
        self.nova_tela.show()

    def buscar_tela(self):
        self.nova_tela = TelaBuscar()
        self.nova_tela.show()

    def buscar_vazia_tela(self):
        self.nova_tela = TelaBuscarVazia()
        self.nova_tela.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaPrincipal()
    tela.show()
    app.exec_()
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from telaCestaVazia import TelaCestaVazia
from telaCesta import TelaCesta
import images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaPrincipal(QMainWindow):
    
    def __init__(self):

        super().__init__()
        uic.loadUi(os.path.join(current_dir, 'ui/telaPrincipal.ui'), self)

        self.botao_cesta = self.findChild(QPushButton, "botaoCesta")  # Substitua pelo nome do botão no .ui
        self.botao_cesta.clicked.connect(self.mostrar_cesta_vazia_tela)

        # ------ botões para adicionar ------

        # ainda sem utilidade para buscar
        self.botao_buscar = self.findChild(QPushButton, "botaoBuscar")
        self.botao_buscar.clicked.connect(self.pesquisar_tela)
        
        # futura tela de reservas quando Áurea terminar 
        self.botao_reservar = self.findChild(QPushButton, "BotaoReservar")
        self.botao_reservar.clicked.connect(self.reservar_produtos_tela)

        # futura tela de ofertas quando Áurea terminar 
        self.botao_ofertas = self.findChild(QPushButton, "botaoOfertas")
        self.botao_ofertas.clicked.connect(self.visualizar_ofertas_tela)

        # futura tela de reservas quando Áurea e Marcio terminarem 
        self.botao_chat = self.findChild(QPushButton, "botaoChat")
        self.botao_chat.clicked.connect(self.chat_tela)

        # teste para abrir a tela de cesta a partir do botão de adicionar
        self.botao_add_cesta = (self.findChild(QPushButton, "BotaoAddCesta"))
        self.botao_add_cesta.clicked.connect(self.chamar_cesta_tela)
        
    def mostrar_cesta_vazia_tela(self):
        self.nova_tela = TelaCestaVazia()  
        self.nova_tela.show()  

    def reservar_produtos_tela(self):
        print("reservar")
        pass
        # self.nova_tela = ...
        # self.nova_tela.show()

    def visualizar_ofertas_tela(self):
        print("ofertas")
        pass
        # self.nova_tela = ...
        # self.nova_tela.show()

    def chat_tela(self):
        print("chat")
        pass
        # self.nova_tela = ...
        # self.nova_tela.show()

    def chamar_cesta_tela(self):
        self.nova_tela = TelaCesta()
        self.nova_tela.show()

    def pesquisar_tela(self):
        # self.nova_tela = ...
        # self.nova_tela.show()
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaPrincipal()
    tela.show()
    app.exec_()
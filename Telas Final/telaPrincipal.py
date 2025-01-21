from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from telaCestaVazia import TelaCestaVazia
import images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaPrincipal(QMainWindow):
    
    def __init__(self):

        super().__init__()
        uic.loadUi(os.path.join(current_dir, 'ui/telaPrincipal.ui'), self)

        self.botao_cesta = self.findChild(QPushButton, "botaoCesta")  # Substitua pelo nome do botão no .ui
        self.botao_cesta.clicked.connect(self.mostrar_cesta_vazia)
        
    def mostrar_cesta_vazia(self):
        self.nova_tela = TelaCestaVazia()  # Cria uma instância da nova tela
        self.nova_tela.show()  # Exibe a nova tela

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaPrincipal()
    tela.show()
    app.exec_()
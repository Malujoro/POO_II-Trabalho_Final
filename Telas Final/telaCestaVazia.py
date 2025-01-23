from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton  # Changed QDialog to QMainWindow
from telaOfertas import TelaOfertas
import sys
import images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaCestaVazia(QMainWindow):  

    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(current_dir, "ui/telaCestaVazia.ui"), self)

        self.botao_ofertas = self.findChild(QPushButton, "botaoIrparaOfertas")
        self.botao_ofertas.clicked.connect(self.ofertas_tela)

    def ofertas_tela(self):
        self.nova_tela = TelaOfertas()
        self.nova_tela.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaCestaVazia()
    tela.show()
    app.exec_()
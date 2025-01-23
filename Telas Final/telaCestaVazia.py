from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton  # Changed QDialog to QMainWindow
import sys
import images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaCestaVazia(QMainWindow):  # Changed from QDialog to QMainWindow

    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(current_dir, "ui/telaCestaVazia.ui"), self)

        # quando tiver as ofertas 
        self.botao_ofertas = self.findChild(QPushButton, "botaoIrparaOfertas")
        self.botao_ofertas.clicked.connect(self.ir_ofertas_tela)

    def ir_ofertas_tela(self):
        # self.nova_tela = ...
        # self.nova_tela.show()
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaCestaVazia()
    tela.show()
    app.exec_()
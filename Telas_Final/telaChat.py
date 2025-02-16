from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from Telas.telaPrincipal import TelaPrincipalUi
import Telas.images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaChat(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(current_dir, "ui/telaChat.ui"), self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaChat()    
    tela.show()
    app.exec_()
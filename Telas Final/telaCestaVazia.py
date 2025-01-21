from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
import sys
import images_rc

import os 

current_dir = os.path.dirname(os.path.abspath(__file__))
class TelaCestaVazia(QDialog):
    
    def __init__(self):

        super().__init__()
        uic.loadUi(os.path.join(current_dir, "ui/telaCestaVazia.ui"), self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaCestaVazia()
    tela.show()
    app.exec_()
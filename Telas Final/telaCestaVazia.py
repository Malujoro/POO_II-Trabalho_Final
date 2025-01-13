from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
import sys
import images_rc

class TelaCestaVazia(QDialog):
    
    def __init__(self):

        super().__init__()
        uic.loadUi("Telas Final/telaCestaVazia.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaCestaVazia()
    tela.show()
    app.exec_()
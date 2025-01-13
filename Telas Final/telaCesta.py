from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import images_rc

class TelaCesta(QMainWindow):
    
    def __init__(self):

        super().__init__()
        uic.loadUi("Telas Final/telaCesta.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaCesta()
    tela.show()
    app.exec_()
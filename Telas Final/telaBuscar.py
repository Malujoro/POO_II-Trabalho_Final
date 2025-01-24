from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
import images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaBuscar(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(current_dir, "ui/telaBuscar.ui"), self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaBuscar()    
    tela.show()
    app.exec_()
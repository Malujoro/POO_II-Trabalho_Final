from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from Telas.telaCesta import TelaCestaUi
import Telas.images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaCesta(TelaCestaUi):
    
    def __init__(self, mainWindow):
        super().setupUi(mainWindow)
        mainWindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    tela = TelaCesta(MainWindow)
    app.exec_()
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from Telas.telaGerenciar import TelaGerenciarUi
import Telas.images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))


class TelaGerenciar(TelaGerenciarUi):

    def __init__(self, mainWindow):
        super().setupUi(mainWindow)
        mainWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    tela = TelaGerenciar(MainWindow)    
    app.exec_()
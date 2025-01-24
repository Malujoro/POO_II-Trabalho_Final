from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton  # Changed QDialog to QMainWindow
import sys
from Telas.telaCestaVazia import TelaCestaVaziaUi
import Telas.images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaCestaVazia(TelaCestaVaziaUi):  

    def __init__(self, mainWindow):
        super().setupUi(mainWindow)
        self.mainWindow = mainWindow
        mainWindow.show()

        self.botaoIrparaOfertas.clicked.connect(self.fechar)

    def fechar(self):
        self.mainWindow.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    tela = TelaCestaVazia(MainWindow)
    app.exec_()
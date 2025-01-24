from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton  # Changed QDialog to QMainWindow
import sys
from telaCestaVazia import TelaCestaVazia
from telaCesta import TelaCesta
from telaGerenciar import TelaGerenciar
from Telas.telaBuscarVazia import TelaBuscarVaziaUi
import Telas.images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaBuscarVazia(TelaBuscarVaziaUi):  

    def __init__(self, mainWindow, string = ""):
        super().setupUi(mainWindow)
        self.mainWindow = mainWindow

        self.label_15.setText(string)
        self.label_17.setText(string)
        self.botaoCesta.clicked.connect(self.cesta_tela)
        self.botaoGerencia.clicked.connect(self.gerencia)

        mainWindow.show()

        self.botaoBuscar.clicked.connect(self.fechar)

    def fechar(self):
        self.mainWindow.close()

    def cesta_tela(self):
        if(len(self.cesta) == 0):
            self.nova_tela = TelaCestaVazia(self.mainWindow)
        else:
            self.nova_tela = TelaCesta(self.mainWindow, self.cesta)

    def gerencia(self):
        self.nova_tela = TelaGerenciar(self.mainWindow)  


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    tela = TelaBuscarVazia(MainWindow)
    app.exec_()
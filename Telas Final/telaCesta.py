from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaCesta(QMainWindow):
    
    def __init__(self):

        super().__init__()
        uic.loadUi(os.path.join(current_dir, "ui/telaCesta.ui"), self)


        # ainda não sei oq esses botões vão fazer 
        self.botao_cesta = self.findChild(QPushButton, "botaoCesta")
        self.botao_cesta.clicked.connect(self.func_botao_cesta)

        self.botao_cesta2 = self.findChild(QPushButton, "botaoCesta_2")
        self.botao_cesta2.clicked.connect(self.func_botao_cesta2)

        def func_botao_cesta(self):
            # self.nova_tela = ...
            # self.nova_tela.show()
            pass

        def func_botao_cesta2(self):
            # self.nova_tela = ...
            # self.nova_tela.show()
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = TelaCesta()
    tela.show()
    app.exec_()
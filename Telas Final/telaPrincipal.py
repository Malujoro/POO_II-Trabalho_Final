from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
import sys
from telaCestaVazia import TelaCestaVazia
from telaCesta import TelaCesta
from telaGerenciar import TelaGerenciar
from telaProdutos import TelaProdutos
from Telas.telaPrincipal import TelaPrincipalUi
# from ..telaChat import TelaChat
from functools import partial
import Telas.images_rc
import os 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bd import Postgres
from bd.entities.medicamento import Medicamento
from chat import ClientWindow


current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaPrincipal(TelaPrincipalUi):

    def __init__(self, mainWindow):
        super().setupUi(mainWindow)
        mainWindow.show()
        self.mainWindow = QtWidgets.QMainWindow()

        self.botaoCesta.clicked.connect(self.cesta_tela)

        self.botaoReservar.clicked.connect(self.reservar_produtos_tela)

        self.cesta = []

        self.banco = Postgres()
        self.get_all_products()
        self.botaoChat.clicked.connect(self.chat_tela)
        self.botaoGerencia.clicked.connect(self.gerencia)


    def cesta_tela(self):
        if(len(self.cesta) == 0):
            self.nova_tela = TelaCestaVazia(self.mainWindow)
        else:
            self.nova_tela = TelaCesta(self.mainWindow, self.cesta)
    
    def gerencia(self):
        self.nova_tela = TelaGerenciar(self.mainWindow)  


    def reservar_produtos_tela(self):
        self.nova_tela = TelaProdutos(self.mainWindow, self.medicamentos, self.cesta)
        pass
        
    def chat_tela(self):
        self.nova_tela = ClientWindow()
        self.nova_tela.show()

    def get_all_products(self):
        self.medicamentos = []

        for prod in self.banco.select_all_medicamentos():
            self.medicamentos.append(Medicamento(prod[0], prod[1], float(prod[2]), int(prod[3])))
        
        nomes = [self.label_5, self.label_12, self.label_16, self.label_21]
        precos = [self.label_9, self.label_13, self.label_17, self.label_22]
        botoes = [self.BotaoAddCesta, self.BotaoAddCesta_2, self.BotaoAddCesta_3, self.BotaoAddCesta_4]
        cont = 0
        for medic in self.medicamentos:
            nomes[cont].setText(medic.nome)
            precos[cont].setText(f"R$ {medic.preco:.2f}")
            botoes[cont].clicked.connect(partial(self.add_cesta, medic))
            
            cont += 1

    def add_cesta(self, medicamento):
        if medicamento not in self.cesta:
            self.cesta.append(medicamento)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    tela = TelaPrincipal(MainWindow)
    sys.exit(app.exec_())   
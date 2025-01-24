from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from telaCestaVazia import TelaCestaVazia
from telaCesta import TelaCesta
from telaGerenciar import TelaGerenciar
from Telas.telaBuscar import TelaBuscaUi
from functools import partial
import Telas.images_rc
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaBuscar(TelaBuscaUi):  

    def __init__(self, mainWindow, string = "", encontrados = [], cesta = []):
        super().setupUi(mainWindow)
        self.mainWindow = mainWindow
        self.encontrados = encontrados
        self.cesta = cesta
        self.botaoCesta.clicked.connect(self.cesta_tela)
        self.botaoGerencia.clicked.connect(self.gerencia)

        mainWindow.show()

        nomes = [self.label_5, self.label_12]
        botoes = [self.BotaoAddCesta, self.BotaoAddCesta_2]

        _translate = QtCore.QCoreApplication.translate
        
        self.label_7.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#004b3f;\">Resultados da busca por: </span><span style=\" font-size:10pt; color:#004b3f;\">{string}</span></p></body></html>"))

        cont = 0
        tamanho = len(encontrados)
        for nome in nomes:
            if(cont < tamanho):
                string_aux = encontrados[cont].nome
                botoes[cont].clicked.connect(partial(self.add_cesta, self.encontrados[cont]))
            else:
                string_aux = string
            nome.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" font-weight:600;\">{string_aux}</span></p></body></html>"))
            cont += 1

        self.botaoBuscar.clicked.connect(self.fechar)

    def cesta_tela(self):
        if(len(self.cesta) == 0):
            self.nova_tela = TelaCestaVazia(self.mainWindow)
        else:
            self.nova_tela = TelaCesta(self.mainWindow, self.cesta)

    def gerencia(self):
        self.nova_tela = TelaGerenciar(self.mainWindow)  

    def fechar(self):
        self.mainWindow.close()

    def add_cesta(self, medicamento):
        if medicamento not in self.cesta:
            self.cesta.append(medicamento)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    tela = TelaBuscar(MainWindow)
    app.exec_()
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGraphicsDropShadowEffect, QTableWidgetItem
from PyQt5.QtGui import QColor
import sys
from telaCestaVazia import TelaCestaVazia
from telaCesta import TelaCesta
from telaGerenciar import TelaGerenciar
from Telas.telaProdutos import TelaProdutosUi
# from ..telaChat import TelaChat
from functools import partial
import Telas.images_rc
import os 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bd import Postgres
from bd.entities.medicamento import Medicamento


current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaProdutos(TelaProdutosUi):

    def __init__(self, mainWindow, medicamentos = [], cesta = []):
        super().setupUi(mainWindow)
        mainWindow.show()
        self.medicamentos = medicamentos
        self.cesta = cesta
        self.mainWindow = QtWidgets.QMainWindow()
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.get_all_products()
        # self.botaoGerencia.clicked.connect(self.gerencia)


    def get_all_products(self):
        self.tableWidget.setRowCount(0)

        cont = 0
        for prod in self.medicamentos:
            self.tableWidget.insertRow(cont)
            self.tableWidget.setItem(cont, 0, QTableWidgetItem(prod.nome))
            self.tableWidget.setItem(cont, 1, QTableWidgetItem(f"R$ {prod.preco:.2f}"))
            self.tableWidget.setItem(cont, 2, QTableWidgetItem(f"{prod.quantidade_estoque}"))
            button = self.create_button(prod)
            self.tableWidget.setCellWidget(cont, 3, button)

            cont += 1

    def add_cesta(self, medicamento):
        if medicamento not in self.cesta:
            self.cesta.append(medicamento)

    def create_button(self, medicamento):
        button = QtWidgets.QPushButton("Adicionar à cesta")
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.clicked.connect(partial(self.add_cesta, medicamento))
        button.setStyleSheet("""
                           QPushButton {
                               background-color: rgb(0, 75, 63);
                               font: 75 7pt "MS Shell Dlg 2";
                               color: rgb(255, 255, 255); /* Cor do texto */
                               border-radius: 8px; /* Bordas arredondadas */
                               padding: 10px; /* Padding interno */
                               image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */
                               image-position:left;
                               text-align: right; /* Centraliza o texto */
                           }
                           QPushButton:hover {
                               background-color: #E5E5E5;
                               font: 75 7pt "MS Shell Dlg 2";
                               color: rgb(255, 255, 255); /* Cor do texto */
                               border-radius: 8px;
                               padding: 10px;
                               image: url(:/images/images/001-shopping-basket.png);
                               image-position:left;
                               text-align: right;
                               border: 1px solid #CCCCCC;
                               box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */
                           }
                           QPushButton:pressed {
                               background-color: #D6D6D6;
                               font: 75 7pt "MS Shell Dlg 2";
                               color: rgb(255, 255, 255); /* Cor do texto */
                               border-radius: 8px;
                               padding: 10px;
                               image: url(:/images/images/001-shopping-basket.png);
                               image-position:left;
                               text-align: right;
                               border: 1px solid #CCCCCC;
                               box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2); /* Menor sombra */
                           }
                       """)
        return button
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    tela = TelaProdutos(MainWindow)
    sys.exit(app.exec_())   
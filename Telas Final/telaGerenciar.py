from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidgetItem
import sys
from Telas.telaGerenciar import TelaGerenciarUi
import Telas.images_rc
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bd import Postgres
from bd.entities.medicamento import Medicamento

class TelaGerenciar(TelaGerenciarUi):

    def __init__(self, mainWindow):
        super().setupUi(mainWindow)
        mainWindow.show()
        self.banco = Postgres()
        self.get_all_products()

        self.updateButton.clicked.connect(self.update_table_info)

        self.tableWidget.itemChanged.connect(self.new_line)

    def get_all_products(self):
        self.tableWidget.setRowCount(0)
        self.medicamentos = []

        cont = 0
        for prod in self.banco.select_all_medicamentos():
            self.tableWidget.insertRow(cont)
            self.tableWidget.setItem(cont, 0, QTableWidgetItem(prod[1]))
            self.tableWidget.setItem(cont, 1, QTableWidgetItem(f"R$ {prod[2]:.2f}"))
            self.tableWidget.setItem(cont, 2, QTableWidgetItem(f"{prod[3]}"))
            self.medicamentos.append(Medicamento(prod[0], prod[1], float(prod[2]), int(prod[3])))
            cont += 1

        self.tableWidget.insertRow(cont)
        # for i in range(self.tableWidget.columnCount()):
        #     self.tableWidget.setItem(cont, i, None)
    
    def str_to_float(self, string):
        return float(string.split()[1])

    def update_table_info(self):
        tamanho = len(self.medicamentos)
        for row in range(self.tableWidget.rowCount()):
            if(self.is_row_empty(row)):
                if(row < tamanho):
                    self.banco.delete_medicamento_by_id(self.medicamentos[row].medicamento_id)
            else:
                nome = self.tableWidget.item(row, 0).text()
                preco = self.str_to_float(self.tableWidget.item(row, 1).text())
                quantidade = int(self.tableWidget.item(row, 2).text())
                
                if(row < tamanho):

                    if(self.medicamentos[row].nome != nome or self.medicamentos[row].preco != preco or self.medicamentos[row].quantidade_estoque != quantidade):
                        self.medicamentos[row].nome = nome
                        self.medicamentos[row].preco = preco
                        self.medicamentos[row].quantidade_estoque = quantidade
                        self.banco.update_medicamento(self.medicamentos[row])
                elif(self.is_row_filled(row)):
                    self.banco.insert_medicamento(Medicamento(None, nome, preco, quantidade))
        
        self.get_all_products()


    def is_row_empty(self, row):
        return all(
            not self.tableWidget.item(row, col) or not self.tableWidget.item(row, col).text().strip()
            for col in range(self.tableWidget.columnCount())
        )
    
    def is_row_filled(self, row):
        return all(
            self.tableWidget.item(row, col) and self.tableWidget.item(row, col).text().strip()
            for col in range(self.tableWidget.columnCount())
        )

    def new_line(self, item):
        row = item.row()
        if row == self.tableWidget.rowCount() - 2 and self.is_row_filled(row):
            self.tableWidget.insertRow(self.tableWidget.rowCount())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    tela = TelaGerenciar(MainWindow)    
    app.exec_()
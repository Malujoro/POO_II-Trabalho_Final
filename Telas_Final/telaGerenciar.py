from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidgetItem
import sys
from Telas.telaGerenciar import TelaGerenciarUi
import Telas.images_rc
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bd import Postgres
from bd.entities.medicamento import Medicamento
from bd.entities.reserva import Reserva

class TelaGerenciar(TelaGerenciarUi):

    def __init__(self, mainWindow):
        super().setupUi(mainWindow)
        mainWindow.show()
        self.banco = Postgres()
        self.get_all_products()
        self.get_all_reservas()

        self.updateButton.clicked.connect(self.update_table1_info)
        self.updateButton.clicked.connect(self.update_table2_info)

        self.tableWidget.itemChanged.connect(self.new_line1)

    def str_to_float(self, string):
        if("$ " in string):
            return float(string.split()[1])
        elif("R$" in string):
            return float(string.split("$")[1])
        else:
            return float(string)
            

    def is_row_empty(self, tableWidget, row):
        return all(
            not tableWidget.item(row, col) or not tableWidget.item(row, col).text().strip()
            for col in range(tableWidget.columnCount())
        )
    
    def is_row_filled(self, tableWidget, row):
        return all(
            tableWidget.item(row, col) and tableWidget.item(row, col).text().strip()
            for col in range(tableWidget.columnCount())
        )

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
    
    def update_table1_info(self):
        tamanho = len(self.medicamentos)
        for row in range(self.tableWidget.rowCount()):
            if(self.is_row_empty(self.tableWidget, row)):
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
                elif(self.is_row_filled(self.tableWidget, row)):
                    self.banco.insert_medicamento(Medicamento(None, nome, preco, quantidade))
        
        self.get_all_products()

    def new_line1(self, item):
        row = item.row()
        if row == self.tableWidget.rowCount() - 2 and self.is_row_filled(self.tableWidget, row):
            self.tableWidget.insertRow(self.tableWidget.rowCount())

    def get_all_reservas(self):
        self.tableWidget_2.setRowCount(0)
        self.reservas = []

        cont = 0
        for reserva in self.banco.select_all_reservas():
            for medic in self.medicamentos:
                if(medic.nome == reserva[6]):
                    prod = medic
                
            self.tableWidget_2.insertRow(cont)
            self.tableWidget_2.setItem(cont, 0, QTableWidgetItem(reserva[2]))
            self.tableWidget_2.setItem(cont, 1, QTableWidgetItem(reserva[6]))
            self.tableWidget_2.setItem(cont, 2, QTableWidgetItem(f"R$ {reserva[5]:.2f}"))
            self.tableWidget_2.setItem(cont, 3, QTableWidgetItem(reserva[3].strftime("%d/%m/%Y %H:%M:%S")))
            self.reservas.append(Reserva(reserva[0], reserva[1], reserva[2], reserva[3], [prod]))
            cont += 1

        self.tableWidget_2.insertRow(cont)
    
    def update_table2_info(self):
        tamanho = len(self.reservas)
        for row in range(self.tableWidget_2.rowCount()):
            if(self.is_row_empty(self.tableWidget_2, row)):
                if(row < tamanho):
                    self.banco.delete_reserva_by_id(self.reservas[row].reserva_id)
            else:
                nome = self.tableWidget_2.item(row, 0).text()
                
                if(row < tamanho and self.reservas[row].nome_cliente != nome):
                    self.reservas[row].nome_cliente = nome
                    self.banco.update_reserva(self.reservas[row])        
        self.get_all_reservas()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    tela = TelaGerenciar(MainWindow)    
    app.exec_()
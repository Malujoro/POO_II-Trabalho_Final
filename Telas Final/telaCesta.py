from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from Telas.telaCesta import TelaCestaUi
import Telas.images_rc
import os 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bd import Postgres
from bd.entities.reserva import Reserva

current_dir = os.path.dirname(os.path.abspath(__file__))

class TelaCesta(TelaCestaUi):
    
    def __init__(self, mainWindow, cesta = []):
        super().setupUi(mainWindow)
        mainWindow.show()
        self.cesta = cesta
        self.label_5.setText(self.cesta[0].nome)
        self.label_9.setText(f"R$ {self.cesta[0].preco:.2f}")
        self.next_item_y = 250
        self.banco = Postgres()
        
        self.botaoCesta.clicked.connect(self.reservar)
        self.populate_initial_items()

    def populate_initial_items(self):
        for item in self.cesta:
            self.add_item_to_cesta(
                self.frame_8, 
                item.nome, 
                item.preco, 
            )

    def add_item_to_cesta(self, parent_frame, description, price):
        try:
            # Frame do item
            frame = QtWidgets.QFrame(parent_frame)
            frame.setGeometry(QtCore.QRect(20, self.next_item_y, 321, 111))
            frame.setStyleSheet("border-radius:8px;")
            frame.setObjectName(f"frame_item_{self.next_item_y}")

            # Create widgets with consistent styling
            label_image = self._create_image_label(frame)
            label_description = self._create_description_label(frame, description)
            label_price = self._create_price_label(frame, price)
            remove_button = self._create_remove_button(frame)

            # Update next item position
            self.next_item_y += 120

            return frame

        except Exception as e:
            print(f"Error adding item: {e}")
            return None

    def create_image_label(self, parent):
        label = QtWidgets.QLabel(parent)
        label.setGeometry(QtCore.QRect(0, 20, 91, 81))
        label.setStyleSheet("background-color: rgb(165, 165, 165); border-radius:8px;")
        return label

    def create_description_label(self, parent, description):
        label = QtWidgets.QLabel(parent)
        label.setGeometry(QtCore.QRect(100, 30, 151, 31))
        label.setText(description)
        return label

    def create_price_label(self, parent, price):
        label = QtWidgets.QLabel(parent)
        label.setGeometry(QtCore.QRect(100, 60, 71, 21))
        label.setStyleSheet("font: 75 8pt 'MS Shell Dlg 2'; color:rgb(0, 75, 63)")
        label.setText(f"R$ {price}")
        return label

    def create_remove_button(self, parent):
        button = QtWidgets.QPushButton(parent)
        button.setGeometry(QtCore.QRect(270, 30, 41, 38))
        button.setStyleSheet("QPushButton {image: url(:/images/images/lixeira-de-reciclagem.png);}")
        return button

    def reservar(self):
        nome = self.text_nome.text()
        cpf = self.text_cpf.text()
        data = self.date_time_edit.dateTime()
        timestamp = data.toString("yyyy-MM-dd HH:mm:ss")

        reserva = Reserva(None, cpf, nome, timestamp, self.cesta)
        self.banco.insert_reserva(reserva)

# Converter para string no formato PostgreSQL (yyyy-MM-dd HH:mm:ss)

        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    tela = TelaCesta(MainWindow)
    app.exec_()
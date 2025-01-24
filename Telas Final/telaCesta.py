from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from Telas.telaCesta import TelaCestaUi
from functools import partial
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
        self.mainWindow = mainWindow
        self.cesta = cesta
        self.label_5.setText(self.cesta[0].nome)
        self.label_9.setText(f"R$ {self.cesta[0].preco:.2f}")
        self.botaoCesta_2.clicked.connect(partial(self.remover, cesta[0]))
        self.next_item_y = 250
        self.banco = Postgres()
        
        self.botaoCesta.clicked.connect(self.reservar)
        self.populate_initial_items()

    def populate_initial_items(self):
        imgs = ["medicina-natural", "drogas", "medicina", "curativo"]
        cont = 0
        for item in self.cesta:
            self.add_item_to_cesta(
                self.frame_8, 
                item,
                imgs[cont % len(imgs)]
            )
            cont += 1

    def add_item_to_cesta(self, parent_frame, item, imgurl):
        # Frame do item
        frame = QtWidgets.QFrame(parent_frame)
        frame.setGeometry(QtCore.QRect(20, self.next_item_y, 321, 111))
        frame.setStyleSheet("border-radius:8px;")
        frame.setObjectName(f"frame_item_{self.next_item_y}")

        # Create widgets with consistent styling
        label_image = QtWidgets.QLabel(frame)
        label_image.setGeometry(QtCore.QRect(0, 20, 91, 81))
        label_image.setStyleSheet(f"image: url(:/images/images/{imgurl}.png);")

        label_description = QtWidgets.QLabel(frame)
        label_description.setGeometry(QtCore.QRect(100, 30, 151, 31))
        label_description.setText(item.nome)

        label_price = QtWidgets.QLabel(frame)
        label_price.setGeometry(QtCore.QRect(100, 60, 71, 21))
        label_price.setStyleSheet("font: 75 8pt 'MS Shell Dlg 2'; color:rgb(0, 75, 63)")
        label_price.setText(f"R$ {item.preco:.2f}")
    
        remove_button = QtWidgets.QPushButton(frame)
        remove_button.setGeometry(QtCore.QRect(270, 30, 41, 38))
        remove_button.setStyleSheet("""
            QPushButton {
                image: url(:/images/images/lixeira-de-reciclagem.png);
            }
        """)
        remove_button.clicked.connect(partial(self.remover, item))

        # Quantity spinbox
        spinbox = QtWidgets.QSpinBox(frame)
        spinbox.setGeometry(QtCore.QRect(260, 70, 42, 22))
        spinbox.setMinimum(1)
        spinbox.setMaximum(50)
        spinbox.setValue(1)

        # Show the frame
        frame.show()

        # Update next item position
        self.next_item_y += 120

        return frame

    def reservar(self):
        nome = self.text_nome.text()
        cpf = self.text_cpf.text()
        data = self.date_time_edit.dateTime()
        timestamp = data.toString("yyyy-MM-dd HH:mm:ss")

        reserva = Reserva(None, cpf, nome, timestamp, self.cesta)
        self.banco.insert_reserva(reserva)
        self.mainWindow.close()

    def remover(self, medicamento):
        if medicamento in self.cesta:
            self.cesta.remove(medicamento)


            for frame in self.frame_8.findChildren(QtWidgets.QFrame):
                if frame.objectName().startswith("frame_item_"):
                    frame.deleteLater()


            self.next_item_y = 250

            self.populate_initial_items()

            self.label_2.setText(f'<html><head/><body><p><span style=" color:#004b3f;">{len(self.cesta)} item{"s" if len(self.cesta) > 1 else ""}</span></p></body></html>')
            
            if(len(self.cesta) == 0):
                self.mainWindow.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    tela = TelaCesta(MainWindow)
    app.exec_()
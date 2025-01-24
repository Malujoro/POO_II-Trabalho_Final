from postgres import Postgres
from entities import Medicamento
from entities import Reserva
from datetime import datetime



if(__name__ == '__main__'):
    timestamp = datetime.now()
    banco = Postgres()

    # medicamento = Medicamento(None, "Dipirona", 15.0, 5)
    # medicamento = Medicamento(None, "Benzetacil", 22.0, 3)
    # banco.insert_medicamento(medicamento)
    # print(banco.select_all_medicamentos())

    # medicamento.nome = "Benzetacil"
    # banco.update_medicamento(medicamento)
    # banco.delete_medicamento_by_id("1")

    # medicamentos = []

    # for prod in banco.select_all_medicamentos():
    #     medicamentos.append(Medicamento(int(prod[0]), prod[1], float(prod[2]), int(prod[3])))

    # reserva = Reserva(13, "123456789-00", "Luís", timestamp, medicamentos)
    # banco.insert_reserva(reserva)

    # print(banco.select_all_reservas())

    # reserva.cpf_cliente = "987654321-00"
    # banco.update_reserva(reserva)

    # banco.delete_reserva_by_id("13")
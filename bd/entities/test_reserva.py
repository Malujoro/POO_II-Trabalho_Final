import pytest
from unittest.mock import Mock, patch
from reserva import Reserva

class TestMedicamento:

    @pytest.fixture
    def reserva(self):
        """Fixture que retorna uma instância do reserva"""
        return Reserva("1", "111.111.111-11", "João", "01/01/2021", [("Teste1", "10.50", "20", "1")])


    def test_constructor(self, reserva: Reserva):
        """Testa a inicialização de uma instância Reserva"""
        assert reserva.reserva_id == "1"
        assert reserva.cpf_cliente == "111.111.111-11"
        assert reserva.nome_cliente == "João"
        assert reserva.data_limite == "01/01/2021"
        assert reserva.medicamentos == [("Teste1", "10.50", "20", "1")]

    
    def test_reserva_id_setter(self, reserva: Reserva):
        """Testa a alteração do id de uma instância Reserva"""
        reserva.reserva_id = "2"
        assert reserva.reserva_id == "2"
        assert reserva.cpf_cliente == "111.111.111-11"
        assert reserva.nome_cliente == "João"
        assert reserva.data_limite == "01/01/2021"
        assert reserva.medicamentos == [("Teste1", "10.50", "20", "1")]

    
    def test_cpf_cliente_setter(self, reserva: Reserva):
        """Testa a alteração do cpf do cliente de uma instância Reserva"""
        reserva.cpf_cliente = "222.222.222-22"
        assert reserva.reserva_id == "1"
        assert reserva.cpf_cliente == "222.222.222-22"
        assert reserva.nome_cliente == "João"
        assert reserva.data_limite == "01/01/2021"
        assert reserva.medicamentos == [("Teste1", "10.50", "20", "1")]


    def test_nome_cliente_setter(self, reserva: Reserva):
        """Testa a alteração do nome do cliente de uma instância Reserva"""
        reserva.nome_cliente = "José"
        assert reserva.reserva_id == "1"
        assert reserva.cpf_cliente == "111.111.111-11"
        assert reserva.nome_cliente == "José"
        assert reserva.data_limite == "01/01/2021"
        assert reserva.medicamentos == [("Teste1", "10.50", "20", "1")]

    def test_data_limite_setter(self, reserva: Reserva):
        """Testa a alteração da data limite de uma instância Reserva"""
        reserva.data_limite = "02/02/2022"
        assert reserva.reserva_id == "1"
        assert reserva.cpf_cliente == "111.111.111-11"
        assert reserva.nome_cliente == "João"
        assert reserva.data_limite == "02/02/2022"
        assert reserva.medicamentos == [("Teste1", "10.50", "20", "1")]

    def test_medicamentos_setter(self, reserva: Reserva):
        """Testa a alteração dos medicamentos de uma instância Reserva"""
        reserva.medicamentos = [("Teste2", "11.99", "12", "6")]
        assert reserva.reserva_id == "1"
        assert reserva.cpf_cliente == "111.111.111-11"
        assert reserva.nome_cliente == "João"
        assert reserva.data_limite == "01/01/2021"
        assert reserva.medicamentos == [("Teste2", "11.99", "12", "6")]
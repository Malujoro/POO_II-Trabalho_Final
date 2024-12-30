import pytest
from unittest.mock import Mock, patch, call
from postgres import PostgresDB
from datetime import datetime
from medicamento import Medicamento

class TestPostgres:

    @pytest.fixture
    def mock_connect(self):
        """Fixture que cria um Mock para simular o método connect"""
        with patch("psycopg2.connect") as mock_connect:
            mock_connect.return_value = None
            yield mock_connect

    @pytest.fixture
    def mock_conn(self):
        """Fixture que cria um Mock para simular o método commit do objeto conn"""
        mock_conn = Mock()
        mock_conn.cursor.return_value = None
        mock_conn.commit.return_value = None
        return mock_conn
    
    @pytest.fixture
    def mock_cursor(self):
        """Fixture que cria um Mock para simular o objeto cursor"""
        mock_cursor = Mock()
        mock_cursor.execute.return_value = None
        mock_cursor.executemany.return_value = None
        mock_cursor.fetchall.return_value = [(None, None)]
        mock_cursor.close.return_value = None
        mock_cursor.lastrowid.return_value = None
        return mock_cursor

    @pytest.fixture
    def postgres(self, mock_connect: Mock):
        """Fixture que retorna uma instância do postgres"""
        return PostgresDB(dbname="mydatabase", user="user", password="password", host="localhost", port="5410")

    @pytest.fixture
    def mock_medic(self):
        """Fixture que retorna uma função para criar um Mock que simula classe Medicamento"""

        def create_mock_medic(nome: str, preco: str, quantidade_estoque: str, medicamento_id: int = None) -> Mock:
            mock_medic = Mock()
            mock_medic.medicamento_id = medicamento_id
            mock_medic.nome = nome
            mock_medic.preco = preco
            mock_medic.quantidade_estoque = quantidade_estoque
            return mock_medic
        
        return create_mock_medic
    
    @pytest.fixture
    def mock_reserva(self, mock_medic):
        """Fixture que retorna uma função para criar um Mock que simula classe Reserva"""

        def create_mock_reserva(reserva_id: int, cpf_cliente: str, nome_cliente: str, data_limite: datetime, medicamentos: list[Medicamento]) -> Mock:
            mock_reserva = Mock()
            mock_reserva.reserva_id = reserva_id
            mock_reserva.cpf_cliente = cpf_cliente
            mock_reserva.nome_cliente = nome_cliente
            mock_reserva.data_limite = data_limite
            mock_reserva.medicamentos = [mock_medic(item[0], item[1], item[2], item[3]) for item in medicamentos]
            return mock_reserva
        
        return create_mock_reserva
    

    def test_constructor(self, postgres: PostgresDB, mock_connect: Mock):
        """Testa a inicialização de uma instância Postgres"""
        assert postgres._dbname == "mydatabase"
        assert postgres._user == "user"
        assert postgres._password == "password"
        assert postgres._host == "localhost"
        assert postgres._port == "5410"
        assert postgres._conn == None
        assert postgres._cursor == None
        mock_connect.assert_called_once()


    def test_connect(self, postgres: PostgresDB, mock_connect: Mock, mock_conn: Mock):
        """Testa a conexão de uma instância Postgres"""
        mock_connect.return_value = mock_conn
        
        postgres.connect()
        mock_connect.assert_called()


    def test_create_table(self, postgres: PostgresDB, mock_conn: Mock, mock_cursor: Mock):
        """Testa a criação de uma tabela de uma instância Postgres"""
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.create_table()
        
        chamadas = [
            call.execute(
                """
                CREATE TABLE IF NOT EXISTS medicamento (
                medicamento_id INT PRIMARY KEY AUTO_INCREMENT, 
                nome VARCHAR(255) NOT NULL, preco DECIMAL(10, 2), 
                quantidade_estoque INT
                )
                """
            ),
            call.execute(
                """
                CREATE TABLE IF NOT EXISTS reservas (
                    reserva_id INT PRIMARY KEY AUTO_INCREMENT,
                    cpf_cliente VARCHAR(14) NOT NULL,
                    nome_cliente VARCHAR(255) NOT NULL,
                    data_limite DATETIME DEFAULT CURRENT_TIMESTAMP
                )
                """
            ),
            call.execute(
                """
                CREATE TABLE IF NOT EXISTS reserva_medicamentos (
                    reserva_id INT NOT NULL,
                    medicamento_id INT NOT NULL,
                    quantidade INT NOT NULL,
                    PRIMARY KEY (reserva_id, medicamento_id),
                    FOREIGN KEY (reserva_id) REFERENCES reservas(reserva_id) ON DELETE CASCADE,
                    FOREIGN KEY (medicamento_id) REFERENCES medicamento(medicamento_id) ON DELETE CASCADE
                )
                """
            ),
        ]

        mock_cursor.assert_has_calls(chamadas, any_order=False)

        mock_conn.commit.assert_called_once()


    @pytest.mark.parametrize("nome, preco, quantidade_estoque", [
        ("Teste1", "10.50", "20"),
        ("Teste2", "12.00", "10"),
        ("Teste3", "2.75", "3"),
    ])
    def test_insert_medicamento(self, postgres: PostgresDB, mock_conn: Mock, mock_cursor: Mock, mock_medic: Mock, nome: str, preco: str, quantidade_estoque: str):
        """Testa a inserção de medicamentos em uma instância Postgres"""
        medicamento = mock_medic(nome, preco, quantidade_estoque)
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.insert_medicamento(medicamento)

        mock_cursor.executemany.assert_called_with("""INSERT INTO medicamento (nome, preco, quantidade_estoque) VALUES (%s, %s, %s)""", (medicamento.nome, medicamento.preco, medicamento.quantidade_estoque))
        mock_conn.commit.assert_called_once()


    def test_select_all_medicamentos(self, postgres: PostgresDB, mock_cursor: Mock):
        """Testa a recuperação de medicamentos em uma instância Postgres"""
        postgres._cursor = mock_cursor
        rows = postgres.select_all_medicamentos()

        mock_cursor.execute.assert_called_with("SELECT * FROM medicamento")
        mock_cursor.fetchall.assert_called_once()
        assert rows == [(None, None)]


    @pytest.mark.parametrize("id", [
        ("1"),
        ("2"),
        ("3"),
    ])
    def test_delete_medicamento_by_id(self, postgres: PostgresDB, mock_cursor: Mock, mock_conn: Mock, id: str):
        """Testa a deleção de um medicamento em uma instância Postgres"""
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.delete_medicamento_by_id(id)

        mock_cursor.executemany.assert_called_with("""DELETE FROM medicamento WHERE medicamento_id = %s;""", id)
        mock_conn.commit.assert_called_once()


    @pytest.mark.parametrize("nome, preco, quantidade_estoque, id", [
        ("Teste1", "10.50", "20", "1"),
        ("Teste2", "12.00", "10", "2"),
        ("Teste3", "2.75", "3", "3"),
    ])
    def test_update_medicamento(self, postgres: PostgresDB, mock_conn: Mock, mock_cursor: Mock, mock_medic: Mock, nome: str, preco: str, quantidade_estoque: str, id: str):
        """Testa a atualização de medicamentos em uma instância Postgres"""
        medicamento = mock_medic(nome, preco, quantidade_estoque, id)
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.update_medicamento(medicamento)

        mock_cursor.executemany.assert_called_with("""UPDATE medicamento SET nome = %s, preco = %s, quantidade_estoque = %s WHERE medicamento_id = %s;""", (medicamento.nome, medicamento.preco, medicamento.quantidade_estoque, medicamento.medicamento_id))
        mock_conn.commit.assert_called_once()


    @pytest.mark.parametrize("reserva_id, cpf_cliente, nome_cliente, data_limite, medicamentos", [
        ("1", "111.111.111-11", "João", "01/01/2021", [("Teste1", "10.50", "20", "1")],),
        ("2", "222.222.222-22", "José", "02/02/2022", [("Teste2", "12.00", "10", "2")],),
        ("3", "333.333.333-33", "Carlos", "03/03/2023", [("Teste3", "2.75", "3", "3")],),
    ])
    def test_insert_reserva(self, postgres: PostgresDB, mock_conn: Mock, mock_cursor: Mock, mock_reserva: Mock, reserva_id: int, cpf_cliente: str, nome_cliente: str, data_limite: datetime, medicamentos: list[Medicamento]):
        """Testa a inserção de reservas em uma instância Postgres"""
        reserva = mock_reserva(reserva_id, cpf_cliente, nome_cliente, data_limite, medicamentos)
        
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.insert_reserva(reserva)

        mock_cursor.execute.assert_called_with(
                """
                INSERT INTO reservas (cpf_cliente, nome_cliente, data_limite) VALUES (%s, %s, %s)
                """,
                (reserva.cpf_cliente, reserva.nome_cliente, reserva.data_limite)
            )
        
        reserva_id = mock_cursor.lastrowid

        reserva_medicamentos = [
            (reserva_id, medicamento.medicamento_id, medicamento.quantidade)
            for medicamento in reserva.medicamentos
        ]

        mock_cursor.executemany.assert_called_with(
                """
                INSERT INTO reserva_medicamentos (reserva_id, medicamento_id, quantidade) VALUES (%s, %s, %s)
                """,
                reserva_medicamentos
            )

        mock_conn.commit.assert_called_once()


    def test_select_all_reservas(self, postgres: PostgresDB, mock_cursor: Mock):
        """Testa a recuperação de reservas em uma instância Postgres"""
        postgres._cursor = mock_cursor
        rows = postgres.select_all_reservas()

        mock_cursor.execute.assert_called_with(
            """
            SELECT r.reserva_id, r.cpf_cliente, r.nome_cliente, r.data_limite, 
                rm.medicamento_id, m.nome, rm.quantidade
            FROM reservas r
            LEFT JOIN reserva_medicamentos rm ON r.reserva_id = rm.reserva_id
            LEFT JOIN medicamento m ON rm.medicamento_id = m.medicamento_id
            """
        )
        mock_cursor.fetchall.assert_called_once()
        assert rows == [(None, None)]


    @pytest.mark.parametrize("reserva_id", [
        ("1"),
        ("2"),
        ("3"),
    ])
    def test_delete_reserva_by_id(self, postgres: PostgresDB, mock_cursor: Mock, mock_conn: Mock, reserva_id: str):
        """Testa a deleção de um reserva em uma instância Postgres"""
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.delete_reserva_by_id(reserva_id)

        mock_cursor.execute.assert_called_with(
                """
                DELETE FROM reservas WHERE reserva_id = %s
                """,
            (reserva_id,)
        )
        mock_conn.commit.assert_called_once()


    @pytest.mark.parametrize("reserva_id, cpf_cliente, nome_cliente, data_limite, medicamentos", [
        ("1", "111.111.111-11", "João", "01/01/2021", [("Teste1", "10.50", "20", "1")],),
        ("2", "222.222.222-22", "José", "02/02/2022", [("Teste2", "12.00", "10", "2")],),
        ("3", "333.333.333-33", "Carlos", "03/03/2023", [("Teste3", "2.75", "3", "3")],),
    ])
    def test_update_reserva(self, postgres: PostgresDB, mock_conn: Mock, mock_cursor: Mock, mock_reserva: Mock, reserva_id: int, cpf_cliente: str, nome_cliente: str, data_limite: datetime, medicamentos: list[Medicamento]):
        """Testa a atualização de reservas em uma instância Postgres"""
        reserva = mock_reserva(reserva_id, cpf_cliente, nome_cliente, data_limite, medicamentos)
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.update_reserva(reserva)

        chamadas = [
            call.execute(
                """
                UPDATE reservas SET cpf_cliente = %s, nome_cliente = %s, data_limite = %s WHERE reserva_id = %s
                """,
                (reserva.cpf_cliente, reserva.nome_cliente, reserva.data_limite, reserva.reserva_id)
            ),
            call.execute(
                """
                DELETE FROM reserva_medicamentos WHERE reserva_id = %s
                """,
                (reserva.reserva_id,)
            ),
        ]

        mock_cursor.assert_has_calls(chamadas, any_order=False)

        reserva_medicamentos = [
            (reserva_id, medicamento.medicamento_id, medicamento.quantidade)
            for medicamento in reserva.medicamentos
        ]

        mock_cursor.executemany.assert_called_with(
                """
                INSERT INTO reserva_medicamentos (reserva_id, medicamento_id, quantidade) VALUES (%s, %s, %s)
                """,
                reserva_medicamentos
        )
        mock_conn.commit.assert_called_once()


    def test_disconnect(self, postgres: PostgresDB, mock_conn: Mock, mock_cursor: Mock):
        """Testa a desconexão de uma instância Postgres"""
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.disconnect()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

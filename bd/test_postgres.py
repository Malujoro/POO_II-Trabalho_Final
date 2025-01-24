import pytest
from unittest.mock import Mock, patch, call
from postgres import Postgres
from datetime import datetime
from medicamento import Medicamento
"""
Importações:
1. Importa o framework pytest utilizado para realizar testes unitários.
2. Importa Mock, patch, e call da biblioteca unittest.mock, que é usada para simular objetos e comportamentos durante os testes.
3. Importa a classe Postgres de um módulo externo, que provavelmente define operações de interação com um banco de dados PostgreSQL.
4. Importa a classe datetime da biblioteca datetime.
5. Importa a classe datetime da biblioteca datetime.
"""


class TestPostgres:
    """
    Classe de Testes para a classe Postgres:

    Esta classe contém testes unitários para verificar as funcionalidades
    de interação com o banco de dados usando a classe Postgres. Os testes
    abordam desde a criação das tabelas até a inserção, atualização,
    seleção e remoção de medicamentos e reservas.
    """

    @pytest.fixture
    def mock_connect(self):
        """
        Método mock_connect:

        Fixture que cria um Mock para simular o método connect.
        Mock simulado do objeto de conexão.

        """
        with patch("psycopg2.connect") as mock_connect:
            mock_connect.return_value = None
            yield mock_connect

    @pytest.fixture
    def mock_conn(self):
        """
        Método mock_conn:

        Fixture que cria um Mock para simular o método commit do objeto conn
        """
        mock_conn = Mock()
        mock_conn.cursor.return_value = None
        mock_conn.commit.return_value = None
        return mock_conn

    @pytest.fixture
    def mock_cursor(self):
        """
        Método mock_cursor:

        Fixture que cria um Mock para simular o objeto cursor.
        """
        mock_cursor = Mock()
        mock_cursor.execute.return_value = None
        mock_cursor.execute.return_value = None
        mock_cursor.fetchall.return_value = [(None, None)]
        mock_cursor.close.return_value = None
        mock_cursor.fetchone.return_value = [None]
        return mock_cursor

    @pytest.fixture
    def postgres(self, mock_connect: Mock):
        """
        Método postgres:

        Fixture que retorna uma instância do postgres.
        """
        return Postgres(dbname="mydatabase", user="user", password="password", host="localhost", port="5410")

    @pytest.fixture
    def mock_medic(self):
        """
        Método mock_medic:

        Fixture que retorna uma função para criar um Mock que simula classe Medicamento.
        """

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
        """
        Método mock_reserva:

        Fixture que retorna uma função para criar um Mock que simula classe Reserva.
        """

        def create_mock_reserva(reserva_id: int, cpf_cliente: str, nome_cliente: str, data_limite: datetime, medicamentos: list[Medicamento]) -> Mock:
            mock_reserva = Mock()
            mock_reserva.reserva_id = reserva_id
            mock_reserva.cpf_cliente = cpf_cliente
            mock_reserva.nome_cliente = nome_cliente
            mock_reserva.data_limite = data_limite
            mock_reserva.medicamentos = [mock_medic(
                item[0], item[1], item[2], item[3]) for item in medicamentos]
            return mock_reserva

        return create_mock_reserva

    def test_constructor(self, postgres: Postgres, mock_connect: Mock):
        """
        Método test_constructor:

        Testa a inicialização de uma instância Postgres:
        Verifica se a instância de Postgres é corretamente inicializada com
        os parâmetros esperados e se o método connect foi chamado.
        """
        assert postgres._dbname == "mydatabase"
        assert postgres._user == "user"
        assert postgres._password == "password"
        assert postgres._host == "localhost"
        assert postgres._port == "5410"
        assert postgres._conn == None
        assert postgres._cursor == None
        mock_connect.assert_called_once()

    def test_connect(self, postgres: Postgres, mock_connect: Mock, mock_conn: Mock):
        """
        Método test_connect:

        Testa a conexão de uma instância Postgres.
        """
        mock_connect.return_value = mock_conn

        postgres.connect()
        mock_connect.assert_called()

    def test_create_all_tables(self, postgres: Postgres, mock_conn: Mock, mock_cursor: Mock):
        """
        Método test_create_all_tables:

        Testa a criação de uma tabela de uma instância Postgres.
        """
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.create_all_tables()

        args = [
            """
                CREATE TABLE IF NOT EXISTS medicamento (
                medicamento_id SERIAL PRIMARY KEY, 
                nome VARCHAR(255) NOT NULL, preco DECIMAL(10, 2), 
                quantidade_estoque INT
                )
                """,
            """
                CREATE TABLE IF NOT EXISTS reservas (
                    reserva_id SERIAL PRIMARY KEY,
                    cpf_cliente VARCHAR(14) NOT NULL,
                    nome_cliente VARCHAR(255) NOT NULL,
                    data_limite TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """,
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
        ]

        chamadas = [call.execute(item) for item in args]

        mock_cursor.assert_has_calls(chamadas, any_order=False)

        mock_conn.commit.assert_called_once()

    @pytest.mark.parametrize("nome, preco, quantidade_estoque", [
        ("Teste1", "10.50", "20"),
        ("Teste2", "12.00", "10"),
        ("Teste3", "2.75", "3"),
    ])
    def test_insert_medicamento(self, postgres: Postgres, mock_conn: Mock, mock_cursor: Mock, mock_medic: Mock, nome: str, preco: str, quantidade_estoque: str):
        """
        Método test_insert_medicamento:

        Testa a inserção de medicamentos em uma instância Postgres.
        """
        medicamento = mock_medic(nome, preco, quantidade_estoque)
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.insert_medicamento(medicamento)

        mock_cursor.execute.assert_called_with("""INSERT INTO medicamento (nome, preco, quantidade_estoque) VALUES (%s, %s, %s)""", (
            medicamento.nome, medicamento.preco, medicamento.quantidade_estoque))
        mock_conn.commit.assert_called_once()

    def test_select_all_medicamentos(self, postgres: Postgres, mock_cursor: Mock):
        """
        Método test_select_all_medicamentos:

        Testa a recuperação de medicamentos em uma instância Postgres.
        """
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
    def test_delete_medicamento_by_id(self, postgres: Postgres, mock_cursor: Mock, mock_conn: Mock, id: str):
        """
        Método test_delete_medicamento_by_id:

        Testa a deleção de um medicamento em uma instância Postgres.
        """
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.delete_medicamento_by_id(id)

        mock_cursor.execute.assert_called_with(
            """DELETE FROM medicamento WHERE medicamento_id = %s;""", id)
        mock_conn.commit.assert_called_once()

    @pytest.mark.parametrize("nome, preco, quantidade_estoque, id", [
        ("Teste1", "10.50", "20", "1"),
        ("Teste2", "12.00", "10", "2"),
        ("Teste3", "2.75", "3", "3"),
    ])
    def test_update_medicamento(self, postgres: Postgres, mock_conn: Mock, mock_cursor: Mock, mock_medic: Mock, nome: str, preco: str, quantidade_estoque: str, id: str):
        """
        Método test_update_medicamento:

        Testa a atualização de medicamentos em uma instância Postgres.
        """
        medicamento = mock_medic(nome, preco, quantidade_estoque, id)
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.update_medicamento(medicamento)

        mock_cursor.execute.assert_called_with("""UPDATE medicamento SET nome = %s, preco = %s, quantidade_estoque = %s WHERE medicamento_id = %s;""", (
            medicamento.nome, medicamento.preco, medicamento.quantidade_estoque, medicamento.medicamento_id))
        mock_conn.commit.assert_called_once()

    @pytest.mark.parametrize("reserva_id, cpf_cliente, nome_cliente, data_limite, medicamentos", [
        ("1", "111.111.111-11", "João", "01/01/2021",
         [("Teste1", "10.50", "20", "1")],),
        ("2", "222.222.222-22", "José", "02/02/2022",
         [("Teste2", "12.00", "10", "2")],),
        ("3", "333.333.333-33", "Carlos", "03/03/2023",
         [("Teste3", "2.75", "3", "3")],),
    ])
    def test_insert_reserva(self, postgres: Postgres, mock_conn: Mock, mock_cursor: Mock, mock_reserva: Mock, reserva_id: int, cpf_cliente: str, nome_cliente: str, data_limite: datetime, medicamentos: list[Medicamento]):
        """
        Método test_insert_reserva:

        Testa a inserção de reservas em uma instância Postgres.
        """
        reserva = mock_reserva(reserva_id, cpf_cliente,
                               nome_cliente, data_limite, medicamentos)

        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.insert_reserva(reserva)

        mock_cursor.execute.assert_called_with(
            """
                INSERT INTO reservas (cpf_cliente, nome_cliente, data_limite) VALUES (%s, %s, %s) RETURNING reserva_id
                """,
            (reserva.cpf_cliente, reserva.nome_cliente, reserva.data_limite)
        )

        reserva_id = mock_cursor.fetchone()[0]

        reserva_medicamentos = [
            (reserva_id, medicamento.medicamento_id, medicamento.quantidade_estoque)
            for medicamento in reserva.medicamentos
        ]

        mock_cursor.executemany.assert_called_with(
            """
                INSERT INTO reserva_medicamentos (reserva_id, medicamento_id, quantidade) VALUES (%s, %s, %s)
                """,
            reserva_medicamentos
        )

        mock_conn.commit.assert_called_once()

    def test_select_all_reservas(self, postgres: Postgres, mock_cursor: Mock):
        """
        Método test_select_all_reservas:

        Testa a recuperação de reservas em uma instância Postgres.
        """
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
    def test_delete_reserva_by_id(self, postgres: Postgres, mock_cursor: Mock, mock_conn: Mock, reserva_id: str):
        """
        Método test_delete_reserva_by_id:

        Testa a deleção de um reserva em uma instância Postgres.
        """
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
        ("1", "111.111.111-11", "João", "01/01/2021",
         [("Teste1", "10.50", "20", "1")],),
        ("2", "222.222.222-22", "José", "02/02/2022",
         [("Teste2", "12.00", "10", "2")],),
        ("3", "333.333.333-33", "Carlos", "03/03/2023",
         [("Teste3", "2.75", "3", "3")],),
    ])
    def test_update_reserva(self, postgres: Postgres, mock_conn: Mock, mock_cursor: Mock, mock_reserva: Mock, reserva_id: int, cpf_cliente: str, nome_cliente: str, data_limite: datetime, medicamentos: list[Medicamento]):
        """
        Método test_update_reserva:

        Testa a atualização de reservas em uma instância Postgres.
        """
        reserva = mock_reserva(reserva_id, cpf_cliente,
                               nome_cliente, data_limite, medicamentos)
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.update_reserva(reserva)

        chamadas = [
            call.execute(
                """
                UPDATE reservas SET cpf_cliente = %s, nome_cliente = %s, data_limite = %s WHERE reserva_id = %s
                """,
                (reserva.cpf_cliente, reserva.nome_cliente,
                 reserva.data_limite, reserva.reserva_id)
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
            (reserva_id, medicamento.medicamento_id, medicamento.quantidade_estoque)
            for medicamento in reserva.medicamentos
        ]

        mock_cursor.executemany.assert_called_with(
            """
                INSERT INTO reserva_medicamentos (reserva_id, medicamento_id, quantidade) VALUES (%s, %s, %s)
                """,
            reserva_medicamentos
        )
        mock_conn.commit.assert_called_once()

    def test_disconnect(self, postgres: Postgres, mock_conn: Mock, mock_cursor: Mock):
        """
        Método test_disconnect:

        Testa a desconexão de uma instância Postgres.
        """
        postgres._cursor = mock_cursor
        postgres._conn = mock_conn
        postgres.disconnect()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

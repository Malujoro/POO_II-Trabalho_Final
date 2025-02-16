from .entities.medicamento import Medicamento
from postgresdb import PostgresDB
"""
Importação:
1. Importa a classe medicamentos
2. Importa a biblioteca do PostgreSQL.
"""


class Postgres(PostgresDB):
    """
    Classe Postgres:

    Gerencia as operações do banco de dados Postgres.
    Permite conectar, criar tabelas, inserir, atualizar, selecionar e remover dados relacionados a medicamentos e reservas.
    """

    def __init__(self, dbname: str = 'mydatabase', user: str = 'user', password: str = 'password', host: str = 'localhost', port: str = '5410') -> None:
        """
        Construção da classe:

        Inicializa a instância do Postgres e estabelece uma conexão com o banco.

        -> Atributos (privados):

        Inicializa a classe com os parâmetros de conexão do banco de dados, com dados pré definidos caso não seja informado:
        dbname (str): nome do banco (padrão: 'mydatabase');
        user (str): nome do usuário (padrão: 'user');
        password (str): senha do usuário (padrão: 'password');
        host (str): endereço do banco (padrão: 'localhost);
        port (str): porta do banco (padrão: '5410);

        conn: atributo que contém a conexão do banco (inicializado com None);
        cursor: atributo que contém o cursor do banco (inicializado com None);
        """
        super().__init__(dbname, user, password, host, port)
        self.create_all_tables()

    def create_all_tables(self) -> None:
        """
        Método create_all_tables:

        Cria as tabelas:
        - medicamento (id, nome, preco, quantidade_estoque)
        - reservas (id, cpf_cliente, nome_cliente, data_limite)
        - reserva_medicamentos (reserva_id, medicamento_id, quantidade)
        """
        
        # Tabela de reservas, relacionamento reserva_medicamento
        self.create_table([
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
        ])

    def insert_medicamento(self, medicamento: Medicamento) -> None:
        """
        Método insert:

        Insere um medicamento na tabela.

        Parâmetro:
        medicamento (Medicamento): Objeto contendo os dados do medicamento.

        Verifica se a lista não está vazia.
        Se não, o comando 'executemany' insere multiplas linhas de uma vez só (as duas strings passadas em cada tupla da lista).
        O comando 'self._conn.commit()' é usado para salvar as alterações.
        """
        if (medicamento):
            self._cursor.execute("""INSERT INTO medicamento (nome, preco, quantidade_estoque) VALUES (%s, %s, %s)""", (medicamento.nome, medicamento.preco, medicamento.quantidade_estoque))
            self._conn.commit()

    def select_all_medicamentos(self):
        """
        Método select_all_medicamentos:

        Retorna todos os medicamentos cadastrados na tabela.
        
        O comando executado 'SELECT * FROM medicamento' seleciona todas as linhas da tabela medicamento.
        Esta função retorna todas as linhas resultantes como uma lista de tuplas.
        """
        return self.select_all("medicamento")

    def delete_medicamento_by_id(self, id:str ) -> None:
        """
        Método delete_medicamento_by_id:

        Remove um medicamento pelo ID.

        Parâmetro:
        id (int): ID do medicamento a ser removido.
        """
        if (id):
            self._cursor.execute("""DELETE FROM medicamento WHERE medicamento_id = %s;""", (id,))
            self._conn.commit()

    def update_medicamento(self, medicamento: Medicamento) -> None:
        """
        Método update_medicamento:

        Atualiza os dados de um medicamento na tabela.

        Parâmetro:
        medicamento (Medicamento): Objeto contendo os dados atualizados.
        """
        if (medicamento):
            self._cursor.execute("""UPDATE medicamento SET nome = %s, preco = %s, quantidade_estoque = %s WHERE medicamento_id = %s;""", (medicamento.nome, medicamento.preco, medicamento.quantidade_estoque, medicamento.medicamento_id))
            self._conn.commit()

    def insert_reserva(self, reserva):
        """
        Método insert_reserva:
        
        Insere uma reserva na tabela e vincula os medicamentos reservados.

        Parâmetro:
        reserva (Reserva): um objeto contendo os dados da reserva.

        Insere uma nova reserva na tabela 'reservas' e vincula os medicamentos reservados na tabela 'reserva_medicamentos'.
        """
        if reserva:
            # Inserir na tabela reservas
            self._cursor.execute(
                """
                INSERT INTO reservas (cpf_cliente, nome_cliente, data_limite) VALUES (%s, %s, %s) RETURNING reserva_id
                """,
                (reserva.cpf_cliente, reserva.nome_cliente, reserva.data_limite)
            )
            reserva_id = self._cursor.fetchone()[0]

            # Inserir medicamentos na tabela reserva_medicamentos
            reserva_medicamentos = [
                (reserva_id, medicamento.medicamento_id, medicamento.quantidade_estoque)
                for medicamento in reserva.medicamentos
            ]
            self._cursor.executemany(
                """
                INSERT INTO reserva_medicamentos (reserva_id, medicamento_id, quantidade) VALUES (%s, %s, %s)
                """,
                reserva_medicamentos
            )
            self._conn.commit()

    def select_all_reservas(self):
        """
        Método delete_reserva_by_id:

        Parâmetro:
        reserva_id (int): identificador único da reserva a ser removida.

        Remove uma reserva da tabela 'reservas' e seus medicamentos associados na tabela 'reserva_medicamentos'.
        O comando 'self._conn.commit()' é usado para salvar as alterações.
        """
        self._cursor.execute(
            """
            SELECT r.reserva_id, r.cpf_cliente, r.nome_cliente, r.data_limite, 
                rm.medicamento_id, m.preco, m.nome, rm.quantidade
            FROM reservas r
            LEFT JOIN reserva_medicamentos rm ON r.reserva_id = rm.reserva_id
            LEFT JOIN medicamento m ON rm.medicamento_id = m.medicamento_id
            """
        )
        rows = self._cursor.fetchall()
        return rows

    def delete_reserva_by_id(self, reserva_id: int) -> None:
        """
        Método delete_reserva_by_id:

        Remove uma reserva e seus medicamentos associados pelo ID da reserva.
        """
        if reserva_id:
            self._cursor.execute(
                """
                DELETE FROM reservas WHERE reserva_id = %s
                """,
                (reserva_id,)
            )
            self._conn.commit()

    def update_reserva(self, reserva):
        """
        Parâmetro:
        reserva (Reserva): objeto contendo os dados atualizados da reserva.

        Atualiza os dados de uma reserva na tabela 'reservas' e os medicamentos associados na tabela 'reserva_medicamentos'.
        """
        if reserva:
            # Atualizar dados da reserva
            self._cursor.execute(
                """
                UPDATE reservas SET cpf_cliente = %s, nome_cliente = %s, data_limite = %s WHERE reserva_id = %s
                """,
                (reserva.cpf_cliente, reserva.nome_cliente, reserva.data_limite, reserva.reserva_id)
            )

            # Remover medicamentos antigos
            self._cursor.execute(
                """
                DELETE FROM reserva_medicamentos WHERE reserva_id = %s
                """,
                (reserva.reserva_id,)
            )

            # Inserir medicamentos atualizados
            reserva_medicamentos = [
                (reserva.reserva_id, medicamento.medicamento_id, medicamento.quantidade_estoque)
                for medicamento in reserva.medicamentos
            ]
            self._cursor.executemany(
                """
                INSERT INTO reserva_medicamentos (reserva_id, medicamento_id, quantidade) VALUES (%s, %s, %s)
                """,
                reserva_medicamentos
            )
            self._conn.commit()
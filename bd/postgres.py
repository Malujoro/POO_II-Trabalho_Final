import psycopg2
from entities.medicamento import Medicamento
"""
Importação:

1. Importa a biblioteca do PostgreSQL.
"""


class PostgresDB:
    """
    Classe PostgresDB:

    Gerenciar as operações do banco de dados Postgres.
    Permite conectar, inserir mensagem e desconectar.
    """

    def __init__(self, dbname: str = 'mydatabase', user: str = 'user', password: str = 'password', host: str = 'localhost', port: str = '5410') -> None:
        """
        Construção da classe:

        Inicializa a instância do PostgresDB e estabelece uma conexão com o banco.

        -> Atributos (privados):

        Inicializa a classe com os parâmetros de conexão do banco de dados, com dados pré definidos caso não seja informado:
        dbname (str): nome do banco (padrão: 'mydatabase');
        user (str): nome do usuário (padrão: 'user');
        password (str): senha do usuário (padrão: 'password');
        host (str): endereço do banco (padrão: 'localhost);
        port (str): porta do banco (padrão: '5410);

        conn: atributo que contém a conexão do banco (inicializado com None);
        cursor: atributo que contém o cursor do banco (inicializado com None);
        connect: a conexão com o banco de dados é estabelecida.
        """
        self._dbname = dbname
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._conn = None
        self._cursor = None
        self.connect()

    def connect(self) -> None:
        """
        Método connect:

        Verifica de a variável conn é None.
        Se sim, estabelece conexão com o banco de dados usando 'psycopg2.connect'.
        Inicializa o cursor para executar os comandos SQL.
        Chama o método 'create_table' para criar a tabela caso não exista.
        """
        if (self._conn == None):
            self._conn = psycopg2.connect(
                dbname=self._dbname,
                user=self._user,
                password=self._password,
                host=self._host,
                port=self._port
            )

            if(self._conn != None):
                self._cursor = self._conn.cursor()
                self.create_table()

    def create_table(self) -> None:
        """
        Método create_table:

        Cria a tabela com as colunas: id, role, message e date.
        O comando 'self._conn.commit()' é usado para salvar as alterações.
        """
        if(self._cursor != None):
            self._cursor.execute("""
                CREATE TABLE IF NOT EXISTS medicamento (
                medicamento_id INT PRIMARY KEY AUTO_INCREMENT, 
                nome VARCHAR(255) NOT NULL, preco DECIMAL(10, 2), 
                quantidade_estoque INT
                )
                """
            )
                # Tabela de reservas
            self._cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS reservas (
                    reserva_id INT PRIMARY KEY AUTO_INCREMENT,
                    cpf_cliente VARCHAR(14) NOT NULL,
                    nome_cliente VARCHAR(255) NOT NULL,
                    data_limite DATETIME DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

            # Tabela de relacionamento reserva_medicamentos
            self._cursor.execute(
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
            )
            self._conn.commit()

    def insert_medicamento(self, medicamento: Medicamento) -> None:
        """
        Método insert:

        Parâmetro:
        dado (lista[tupla[str, str]]): uma lista de tuplas, na qual cada uma contém dois elementos do tipo string.
            - O primeiro elemento corresponde ao nome de quem enviou a mensagem
            - O segundo elemento corresponde a mensagem que foi enviada

        Verifica se a lista não está vazia.
        Se não, o comando 'executemany' insere multiplas linhas de uma vez só (as duas strings passadas em cada tupla da lista).
        O comando 'self._conn.commit()' é usado para salvar as alterações.
        """
        if (medicamento):
            self._cursor.executemany("""INSERT INTO medicamento (nome, preco, quantidade_estoque) VALUES (%s, %s, %s)""", (medicamento.nome, medicamento.preco, medicamento.quantidade_estoque))
            self._conn.commit()

    def select_all_medicamentos(self):
        """
        Método select_all:
        
        O comando executado 'SELECT * FROM medicamento' seleciona todas as linhas da tabela medicamento.
        Esta função retorna todas as linhas resultantes como uma lista de tuplas.
        """
        self._cursor.execute("SELECT * FROM medicamento")
        rows = self._cursor.fetchall()
        return rows  

    def delete_medicamento_by_id(self, id:str ) -> None:
        """
        Método delete:
        """
        if (id):
            self._cursor.executemany("""DELETE FROM medicamento WHERE medicamento_id = %s;""", id)
            self._conn.commit()

    def update_medicamento(self, medicamento: Medicamento) -> None:
        """
        Método delete:
        """
        if (medicamento):
            self._cursor.executemany("""UPDATE medicamento SET nome = %s, preco = %s, quantidade_estoque = %s WHERE medicamento_id = %s;""", (medicamento.nome, medicamento.preco, medicamento.quantidade_estoque, medicamento.medicamento_id))
            self._conn.commit()

    def insert_reserva(self, reserva):
        """
        Método insert_reserva:

        Parâmetro:
        reserva (Reserva): um objeto contendo os dados da reserva.

        Insere uma nova reserva na tabela 'reservas' e vincula os medicamentos reservados na tabela 'reserva_medicamentos'.
        """
        if reserva:
            # Inserir na tabela reservas
            self._cursor.execute(
                """
                INSERT INTO reservas (cpf_cliente, nome_cliente, data_limite) VALUES (%s, %s, %s)
                """,
                (reserva.cpf_cliente, reserva.nome_cliente, reserva.data_limite)
            )
            reserva_id = self._cursor.lastrowid

            # Inserir medicamentos na tabela reserva_medicamentos
            reserva_medicamentos = [
                (reserva_id, medicamento.medicamento_id, medicamento.quantidade)
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
        Método select_all_reservas:

        Retorna todas as reservas da tabela 'reservas', incluindo os medicamentos associados.
        """
        self._cursor.execute(
            """
            SELECT r.reserva_id, r.cpf_cliente, r.nome_cliente, r.data_limite, 
                rm.medicamento_id, m.nome, rm.quantidade
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
        Método update_reserva:

        Atualiza os dados de uma reserva e os medicamentos associados.
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
                (reserva.reserva_id, medicamento.medicamento_id, medicamento.quantidade)
                for medicamento in reserva.medicamentos
            ]
            self._cursor.executemany(
                """
                INSERT INTO reserva_medicamentos (reserva_id, medicamento_id, quantidade) VALUES (%s, %s, %s)
                """,
                reserva_medicamentos
            )
            self._conn.commit()



    def disconnect(self) -> None:
        """
        Método disconnect:

        Fecha o cursor e a conexão (conn) com o banco de dados usando o comando close.
        """
        self._cursor.close()
        self._conn.close()


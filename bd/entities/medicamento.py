class Medicamento:
    def __init__(self, medicamento_id=None, nome=None, preco=None, quantidade_estoque=None):
        self._medicamento_id = medicamento_id  
        self._nome = nome  
        self._preco = preco  
        self._quantidade_estoque = quantidade_estoque 

    
    @property
    def medicamento_id(self):
        return self._medicamento_id

    @medicamento_id.setter
    def medicamento_id(self, medicamento_id):
        self._medicamento_id = medicamento_id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def quantidade_estoque(self):
        return self._quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, quantidade_estoque):
        self._quantidade_estoque = quantidade_estoque

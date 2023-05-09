from time import time
from Categoria import Categoria
from uuid import uuid4

class Utilizador:
    pass

class Expense:

    def __init__(self, user: Utilizador, categoria: Categoria, descricao: str, valor: float):
        self.__id = uuid4()
        self.__user: Utilizador = user
        self.__categoria: Categoria = categoria
        self.__descricao: str = descricao
        self.__valor: float = valor
        self.__timestamp: float = time()

    def get_id(self):
        return self.__id

    def get_user(self):
        return self.__user

    def set_user(self, user: Utilizador):
        self.__user = user

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria: Categoria):
        self.__categoria = categoria

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_timestamp(self):
        return self.__timestamp

    def set_timestamp(self, timestamp):
        self.__timestamp = timestamp


e1 = Expense()


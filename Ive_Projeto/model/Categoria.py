"class vai receber como argumento  name do tipo sting."

"Dentro do construtor, o atributo idcategoria é criado como um userid gerado pela função userid(), e o atributo __name é definido como o valor do argumento name."
from uuid import uuid4

class Categoria:
    def __init__(self, nome: str):
        self.__id = uuid4()
        self.__nome: str = nome

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__nome

    def set_name(self, nome: str):
        self.__nome = nome


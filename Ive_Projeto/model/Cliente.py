class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome
        
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
        
    def get_idade(self):
        return self.__idade
        
    def set_idade(self, nova_idade):
        self.__idade = nova_idade







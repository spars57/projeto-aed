
from abc import ABC, abstractmethod
class List(ABC):
    @abstractmethod
    def is_empty(self):
        ''' Retorna True se a colecao não contém elementos. '''
    @abstractmethod
    def size(self):
        ''' Retorna o número de elementos na colecao. '''
    @abstractmethod
    def get_first(self):
        ''' Retorna o primeiro elemento da colecao.'''
    @abstractmethod
    def get_last(self):
        ''' Retorna o último elemento da colecao.'''
    @abstractmethod
    def get(self, posicao):
        ''' Retorna o elemento na posição especificada na colecao.
            Range de posições válidas: 0, ..., size()-1. '''
    @abstractmethod
    def find(self, elemento):
        ''' Retorna a posição na colecao da primeira ocorrência
             do elemento especificado, ou -1 se o elementoo especificado
             não ocorre na colecao.. '''
    @abstractmethod
    def insert_first(self, elemento):
        ''' Insere o elemento especificado na primeira posição da colecao. '''  
    @abstractmethod
    def insert_last(self, elemento):
        ''' Insere o elemento especificado na última posição da colecao. '''
    @abstractmethod
    def insert(self, elemento, posicao):
        ''' Insira o elemento especificado na posição especificada na colecao.
             Gama de posições válidas: 0, ..., tamanho ().
             Se a posição especificada for 0, a inserção corresponde ao insertfirst.
             Se a posição especificada for tamanho (), a inserção corresponde ao insertLast.'''
    @abstractmethod
    def remove_first(self):
        '''Remove e retorna o elemento na primeira posição da colecao.'''
    @abstractmethod
    def remove_last(self):
        ''' Remove e retorna o elemento na última posição da colecao. '''
    @abstractmethod
    def remove(self, posicao):
        ''' Remove e retorna o elemento na posição especificada na colecao.
            Range de posições válidas: 0, ..., size()-1.'''
    @abstractmethod
    def make_empty(self):
        ''' Remove todos os elementos da colecao. '''
    @abstractmethod
    def iterator(self):
        ''' Retorna um iterador dos elementos da colecao (na sequência adequada). '''

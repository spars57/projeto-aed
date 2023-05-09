from model.List.List import *
from model.List.Nodes import *

class LinkedList(List):
    def __init__(self):
        self.head = None
        self.size = 0
    def is_empty(self):
        return self.head is None
    def size(self):
        return self.size
    def get_first(self):
        if self.head is None:
            raise Exception("Lista vazia")
        return self.head.get_element()

    def get_last(self):
        if self.head is None:
            raise Exception("Lista vazia")
        node = self.head
        while node.get_next_node() is not None:
            node = node.get_next_node()
        return node.get_element()

    def get(self, posicao):
        if posicao < 0 or posicao >= self.size:
            raise Exception("Posição inválida")
        node = self.head
        for i in range(posicao):
            node = node.get_next_node()
        return node.get_element()

    def find(self, elemento):
        node = self.head
        posicao = 0
        while node is not None:
            if node.get_element() == elemento:
                return posicao
            node = node.get_next_node()
            posicao += 1
        return -1
    
    def insert(self, elemento, posicao):
        if posicao < 0 or posicao > self.size:
            raise Exception("Posição inválida")
        if posicao == 0:
            self.insert_first(elemento)
        elif posicao == self.size:
            self.insert_last(elemento)
        else:
            node = self.head
            for i in range(posicao - 1):
                node = node.get_next_node()
            new_node = SingleListNode(elemento, node.get_next_node())
            node.set_next_node(new_node)
            self.size += 1

            
    def insert_first(self, elemento):
        node = SingleListNode(elemento, self.head)
        self.head = node
        self.size += 1

    def insert_last(self, elemento):
        if self.head is None:
            self.insert_first(elemento)
        else:
            node = self.head
            while node.get_next_node() is not None:
                node = node.get_next_node()
            new_node = SingleListNode(elemento, None)
            node.set_next_node(new_node)
            self.size += 1

    
    def remove_first(self):
        if self.head is None:
            raise Exception("Lista vazia")
        elemento = self.head.get_element()
        self.head = self.head.get_next_node()
        self.size -= 1
        return elemento

    def remove_last(self):
        if self.head is None:
            raise Exception("Lista vazia")
        if self.size == 1:
            return self.remove_first()
        node = self.head
        while node.get_next_node().get_next_node() is not None:
            node = node.get_next_node()
        elemento = node.get_next_node().get_element()
        node.set_next_node(None)
        self.size -= 1
        return elemento

    def remove(self, posicao):
        if posicao < 0 or posicao >= self.size:
            raise Exception("Posição inválida")
        if posicao == 0:
            return self.remove_first()
        if posicao == self.size - 1:
            return self.remove_last()
        node = self.head
        for i in range(posicao - 1):
            node = node.get_next_node()
        elemento = node.get_next_node().get_element()
        node.set_next_node(node.get_next_node().get_next_node())
        self.size -= 1
        return elemento

    def make_empty(self):
        self.head = None
        self.size = 0

    def iterator(self):
        node = self.head
        while node is not None:
            yield node.get_element()
            node = node.get_next_node()

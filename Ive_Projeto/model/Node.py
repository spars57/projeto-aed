
class Node:
    def __init__(self, data=None):
        self.__id = id (self)
        self.data = data
        self.next_node = None

    def set_node(self, node):
        self.next_node = node

    def get_id(self):
        return self.__id




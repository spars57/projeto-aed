from classes.Node import Node


class LinkedList:
    def __init__(self):
        self.__list: list[Node] = []

    def is_empty(self) -> bool:
        return len(self.__list) == 0

    def size(self) -> int:
        return len(self.__list)

    def get_first(self) -> Node | None:
        try:
            return self.__list[0]
        except IndexError:
            return None

    def get_last(self) -> any:
        try:
            return self.__list[len(self.__list) - 1]
        except IndexError:
            return None

    def get(self, index) -> any:
        try:
            [self.__list[i] for i in range(len(self.__list)) if i == index][0]
        except IndexError:
            return None

    def insert_first(self, data: any) -> None:
        first_node: Node = self.get_first()
        new_node = Node(data)

        if first_node is not None:
            new_node.set_node(first_node)

        self.__list.insert(0, new_node)

    def remove_first(self) -> None:
        first_node = self.get_first()
        self.__list = [node for node in self.__list if node.get_id() != first_node.get_id()]

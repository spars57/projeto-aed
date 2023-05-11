from typing import TypeVar, Generic

from classes.Node import Node

T = TypeVar('T')


class LinkedList(Generic[T]):
    def __init__(self):
        self.__head: Node[T] = None
        self.__size: int = 0

    def is_empty(self) -> bool:
        return self.__size == 0

    def size(self) -> int:
        return self.__size

    def get_first(self) -> Node[T] | None:
        return self.__head

    def get_last(self) -> T | None:
        if self.__head is None:
            return None

        node = self.__head.get_node()

        while node.get_node() is not None:
            node = node.get_node()

        return node

    def insert_first(self, data: T) -> None:
        first_node = self.get_first()
        new_node = Node(data)

        if first_node is not None:
            new_node.set_node(first_node)

        self.__size += 1
        self.__head = new_node

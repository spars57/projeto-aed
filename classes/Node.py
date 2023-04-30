from typing import TypeVar
from uuid import uuid4

TNode = TypeVar("TNode", bound="Node")


class Node:
    def __init__(self, data: any):
        self.__id: uuid4 = uuid4()
        self.__data = data
        self.__node: Node | None = None

    def set_node(self, node: TNode):
        self.__node = node

    def set_data(self, value):
        self.__data = value

    def get_id(self) -> uuid4:
        return self.__id

    def get_node(self):
        return self.__node

    def get_data(self):
        return self.__data

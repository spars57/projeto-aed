from typing import TypeVar, Generic
from uuid import uuid4

TNode = TypeVar("TNode", bound="Node")
T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T):
        self.__id: uuid4 = uuid4()
        self.__data: T = data
        self.__node: Node | None = None

    def set_node(self, node: TNode):
        self.__node = node

    def set_data(self, value):
        self.__data = value

    def get_id(self) -> uuid4:
        return self.__id

    def get_node(self) -> TNode:
        return self.__node

    def get_data(self) -> T:
        return self.__data

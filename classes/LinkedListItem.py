from typing import TypeVar
from uuid import uuid4

TLinkedListItem = TypeVar("TLinkedListItem", bound="LinkedListItem")


class LinkedListItem:
    def __init__(self, value, next_element: TLinkedListItem | None):
        self.__id: uuid4 = uuid4()
        self.__value = value
        self.__next: TLinkedListItem | None = next_element

    def set_id(self, id: uuid4):
        self.__id = id

    def set_value(self, value):
        self.__value = value

    def set_next(self, next: TLinkedListItem | None):
        self.__next = next

    def get_id(self) -> uuid4:
        return self.__id

    def get_value(self):
        return self.__value

    def get_next(self) -> TLinkedListItem | None:
        return self.__next

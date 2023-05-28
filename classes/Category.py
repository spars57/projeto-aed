from typing import TypeVar
from uuid import uuid4

TCategory = TypeVar("TCategory", bound="Category")


class Category:
    def __init__(self, name: str):
        self.__id: uuid4 = uuid4()
        self.__name: str = name

    def get_id(self) -> uuid4:
        return self.__id

    def set_id(self, category_id: str) -> TCategory:
        self.__id = category_id
        return self

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> TCategory:
        self.__name = name
        return self

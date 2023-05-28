from typing import TypeVar
from uuid import uuid4

from classes.Category import Category
from classes.User import User

TBudget = TypeVar("TBudget", bound="Budget")


class Budget:
    def __init__(self, name: str, user: User, category: Category, value: float, valid_from: float, valid_until: float):
        self.__id: uuid4 = uuid4()
        self.__user: User = user
        self.__category: Category = category
        self.__value: float = value
        self.__name = name
        self.__valid_from = valid_from
        self.__valid_until = valid_until

    def get_id(self) -> uuid4():
        return self.__id

    def set_id(self, category_id: str) -> TBudget:
        self.__id = category_id
        return self

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> TBudget:
        self.__name = name
        return self

    def get_user(self) -> User:
        return self.__user

    def set_user(self, user: User) -> TBudget:
        self.__user = user
        return self

    def get_category(self) -> Category:
        return self.__category

    def set_category(self, category: Category) -> TBudget:
        self.__category = category
        return self

    def get_value(self) -> float:
        return self.__value

    def set_value(self, value: float) -> TBudget:
        self.__value = value
        return self

    def get_valid_from(self) -> float:
        return self.__valid_from

    def set_valid_from(self, value: float) -> TBudget:
        self.__valid_from = value
        return self

    def get_valid_until(self) -> float:
        return self.__valid_until

    def set_valid_until(self, value: float) -> TBudget:
        self.__valid_until = value
        return self


from typing import TypeVar
from uuid import uuid4

from classes.Category import Category
from classes.User import User

TExpense = TypeVar("TExpense", bound="Expense")


class Expense:
    def __init__(self, user: User, category: Category, description: str, value: float, timestamp: float) -> None:
        self.__id: uuid4 = uuid4()
        self.__user: User = user
        self.__category: Category = category
        self.__description: str = description
        self.__value: float = value
        self.__timestamp: float = timestamp

    def get_id(self) -> uuid4:
        return self.__id

    def set_id(self, expense_id: str) -> TExpense:
        self.__id = expense_id
        return self

    def get_user(self) -> User:
        return self.__user

    def set_user(self, user: User) -> TExpense:
        self.__user = user
        return self

    def get_category(self) -> Category:
        return self.__category

    def set_category(self, category: Category) -> TExpense:
        self.__category = category
        return self

    def get_value(self) -> float:
        return self.__value

    def set_value(self, value: float) -> TExpense:
        self.__value = value
        return self

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str) -> TExpense:
        self.__description = description
        return self

    def get_timestamp(self) -> float:
        return self.__timestamp

    def set_timestamp(self, timestamp: float) -> TExpense:
        self.__timestamp = timestamp
        return self

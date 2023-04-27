from time import time
from typing import TypeVar
from uuid import uuid4

TExpense = TypeVar("TExpense", bound="User")


class Expense:
    def __init__(self, user_id: str, category_id: str, description: str, value: float) -> None:
        self.__id: str = str(uuid4())
        self.__user_id: str = user_id
        self.__category_id: str = category_id
        self.__description: str = description
        self.__value: float = value
        self.__timestamp: float = time()

    def get_id(self) -> str:
        return self.__id

    def set_id(self, expense_id: str) -> TExpense:
        self.__id = expense_id
        return self

    def get_user(self) -> str:
        return self.__user_id

    def set_user(self, user_id: str) -> TExpense:
        self.__user_id = user_id
        return self

    def get_category(self) -> str:
        return self.__category_id

    def set_category(self, category_id: str) -> TExpense:
        self.__category_id = category_id
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

    def set_timestamp(self, timestamp: str) -> TExpense:
        self.__timestamp = timestamp
        return self

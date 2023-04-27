from typing import TypeVar
from uuid import uuid4

TUser = TypeVar("TUser", bound="User")


class User:
    def __init__(self, username: str, password: str, nif: str) -> None:
        self.__id: str = str(uuid4())
        self.__username: str = username
        self.__password: str = password
        self.__nif: str = nif

    def get_id(self) -> str:
        return self.__id

    def set_id(self, user_id: str) -> TUser:
        self.__id = user_id
        return self

    def get_username(self) -> str:
        return self.__username

    def set_username(self, username: str) -> TUser:
        self.__username = username
        return self

    def get_nif(self) -> str:
        return self.__nif

    def set_nif(self, nif: str) -> TUser:
        self.__nif = nif
        return self

    def get_password(self) -> str:
        return self.__password

    def set_password(self, password: str) -> TUser:
        self.__password = password
        return self

    def json(self) -> dict:
        return self.__dict__
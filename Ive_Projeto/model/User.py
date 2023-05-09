from typing import TypeVar
from uuid import uuid4

class User:
    def __init__(self, username: str, password, nif,):
        self.__id: str = id(uuid4())
        self.__username = username
        self.__password = password
        self.__nif = nif

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_nif(self):
        return self.__nif

    def set_nif(self, nif):
        self.__nif = nif

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password



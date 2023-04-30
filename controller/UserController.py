from classes.User import User
from modal.Modal import Modal
from utils.nif import validate_nif
from utils.passwords import encrypt


class UserController:
    def __init__(self, modal: Modal):
        self.__modal: Modal = modal

    def login(self, username: str, password: str) -> bool:
        user = self.__modal.get_user_list().get_user_by_username(username)

        if user is None:
            return False

        return user.get_password() == password

    @staticmethod
    def create_user(username: str, password: str, nif: int) -> User:
        return User(username=username, password=encrypt(password), nif=nif)

    def add_user(self, user: User) -> bool:
        user_list = self.__modal.get_user_list()

        if user_list.get_user_by_username(user.get_username()) is not None:
            return False

        if not validate_nif(user.get_nif()):
            return False

        user_list.insert_first(user)

        return True

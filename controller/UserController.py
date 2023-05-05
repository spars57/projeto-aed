from classes.User import User
from modal.Modal import Modal
from utils.nif import validate_nif
from utils.passwords import encrypt


class UserController:
    def __init__(self, modal: Modal):
        self.__modal: Modal = modal

    def login(self, username: str, password: str) -> bool:
        user = self.__modal.get_user_list().get_user_by_username(username)
        return user.get_password() is encrypt(password) if user is not None else False

    @staticmethod
    def create_user(username: str, password: str, nif: int) -> User:
        return User(username=username, password=encrypt(password), nif=nif)

    def add_user(self, user: User) -> str:
        user_list = self.__modal.get_user_list()

        if user_list.get_user_by_username(user.get_username()) is not None:
            return f"Já existe um utilizador registado com o username '{user.get_username()}'."

        if not validate_nif(user.get_nif()):
            return f"O nif '{user.get_nif()}' é inválido."

        if user_list.insert_first(user):
            return f"Utilizador '{user.get_username()}' registado com sucesso"

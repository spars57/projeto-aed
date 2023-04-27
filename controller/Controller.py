from classes.Category import Category
from classes.Expense import Expense
from classes.User import User
from modal.Modal import Modal
from utils.nif import validate_nif
from utils.passwords import encrypt


class Controller:
    def __init__(self, modal: Modal):
        self.__modal: Modal = modal

    def get_modal(self) -> Modal:
        return self.__modal

    def create_user(self, username: str, password: str, nif: str) -> str | None:
        # Validate if all the provieded params are valid
        if self.__modal.get_user_list().get_by_username(username):
            return "Nome de utilizador já está registado."

        if not validate_nif(nif):
            return "Parece que há algo errado com o seu NIF."

        # Encrypt password
        encrypted = encrypt(password)

        # Add new user to userlist
        self.__modal.get_user_list().add(User(username, encrypted, nif))

        return None

    def create_expense(self, user_id: str, category_id: str, description: str, value: float | int) -> str | None:
        self.__modal.get_expense_list().add(Expense(user_id, category_id, description, value))
        return None

    def create_category(self, name: str) -> str | None:
        self.__modal.get_category_list().add(Category(name))
        return None

    def login(self, username: str, password: str) -> bool:
        user = self.get_modal().get_user_list().get_by_username(username)

        if not user:
            return False

        return user.get_password() == encrypt(password)

    @staticmethod
    def sort_expenses_by_value(expense_list: list[Expense], descending: bool = True) -> list[Expense]:
        return list(sorted(expense_list, key=lambda expense: expense.get_value(),
                           reverse=descending))


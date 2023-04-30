from classes.Category import Category
from classes.Expense import Expense
from classes.User import User
from modal.Modal import Modal


class ExpenseController:
    def __init__(self, modal: Modal):
        self.__modal: Modal = modal
        # Proxify ExpenseList Methods
        self.get_expenses_filtered = modal.get_expense_list().get_expenses_filtered

    @staticmethod
    def create_expense(user: User, category: Category, value: float, timestamp: int, description: str = "") -> Expense:
        return Expense(user=user, category=category, description=description, value=value, timestamp=timestamp)

    def add_expense(self, expense: Expense) -> bool:
        expense_list = self.__modal.get_expense_list()
        user_list = self.__modal.get_user_list()
        category_list = self.__modal.get_category_list()

        if user_list.get_user_by_username(expense.get_user().get_username()) is None:
            return False

        if category_list.get_category_by_name(expense.get_category().get_name()) is None:
            return False

        expense_list.insert_first(expense)

        return True

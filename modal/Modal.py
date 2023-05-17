from classes.BudgetList import BudgetList
from classes.CategoryList import CategoryList
from classes.ExpenseList import ExpenseList
from classes.User import User
from classes.UserList import UserList


class Modal:
    def __init__(self):
        self.__user_list: UserList = UserList()
        self.__category_list: CategoryList = CategoryList()
        self.__expense_list: ExpenseList = ExpenseList()
        self.__budget_list: BudgetList = BudgetList()
        self.__current_user: User = None

    def get_user_list(self) -> UserList:
        return self.__user_list

    def get_category_list(self) -> CategoryList:
        return self.__category_list

    def get_expense_list(self) -> ExpenseList:
        return self.__expense_list

    def get_budget_list(self) -> BudgetList:
        return self.__budget_list

    def set_current_user(self, user: User) -> None:
        self.__current_user = user

    def get_current_user(self) -> User:
        return self.__current_user

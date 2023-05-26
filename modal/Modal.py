import json

from classes.BudgetList import BudgetList
from classes.Category import Category
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

    def save_to_json(self) -> None:
        first_user = self.get_user_list().get_first()
        first_category = self.get_category_list().get_first()

        categories = []

        aux = {}

        while first_category is not None:
            categories.append(first_category.get_data().get_name())
            first_category = first_category.get_node()

        aux['categories'] = categories

        while first_user is not None:
            user = first_user.get_data()

            first_expenses = self.get_expense_list().get_first()
            expense = []

            while first_expenses is not None:
                exp = first_expenses.get_data()

                if exp.get_user().get_id() == user.get_id():
                    expense.append({
                        "id": str(exp.get_id()),
                        "category": exp.get_category().get_name(),
                        "description": exp.get_description(),
                        "value": exp.get_value(),
                        "timestamp": exp.get_timestamp()
                    })

                first_expenses = first_expenses.get_node()

            aux[user.get_username()] = {
                "id": str(user.get_id()),
                "username": user.get_username(),
                "password": user.get_password(),
                "balance": user.get_balance(),
                "nif": user.get_nif(),
                "expenses": expense,
            }

            first_user = first_user.get_node()

            file = open("data.json", "w")
            file.write(json.dumps(aux))
            file.close()

    def load_to_json(self) -> None:
        file = open("data.json", "r")
        aux: dict = json.loads(file.read())

        categories = aux['categories']

        for key in aux.keys():
            if key != 'categories':
                u = User(
                    username=aux[key]['username'],
                    password=aux[key]['password'],
                    nif=aux[key]['nif'],
                )

                u.set_balance(aux[key]['balance'])

                self.get_user_list().insert_first(u)

        for category in categories:
            self.get_category_list().insert_first(Category(
                name=category,
            ))

        return self

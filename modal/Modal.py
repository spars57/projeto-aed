import json
import os
from typing import IO

from classes.Category import Category
from classes.CategoryList import CategoryList
from classes.Expense import Expense
from classes.ExpenseList import ExpenseList
from classes.User import User
from classes.UserList import UserList


class Modal:
    def __init__(self):
        self.__user_list: UserList = UserList()
        self.__category_list: CategoryList = CategoryList()
        self.__expense_list: ExpenseList = ExpenseList()

    def get_user_list(self) -> UserList:
        return self.__user_list

    def get_category_list(self) -> CategoryList:
        return self.__category_list

    def get_expense_list(self) -> ExpenseList:
        return self.__expense_list

    def save_to_file(self, filename: str) -> bool:
        if not os.path.exists(filename):
            return False

        try:
            file: IO = open(filename, 'w')
            users_list = self.get_user_list()
            category_list = self.get_category_list()
            expense_list = self.get_expense_list()

            users = [{
                "id": user.get_id(),
                "username": user.get_username(),
                "password": user.get_password(),
                "nif": user.get_nif(),
            } for user in users_list.get()]

            categories = [{
                "id": category.get_id(),
                "name": category.get_name(),
            } for category in category_list.get()]

            expenses = [{
                "id": expense.get_id(),
                "user_id": expense.get_user(),
                "category_id": expense.get_category(),
                "description": expense.get_description(),
                "value": expense.get_value(),
                "timestamp": expense.get_timestamp()
            } for expense in expense_list.get()]

            final_dict = {
                "users": users,
                "categories": categories,
                "expenses": expenses,
            }

            file.write(json.dumps(final_dict))
            file.close()
            return True
        except FileNotFoundError:
            return False

    def read_from_file(self, filename: str) -> bool:
        if not os.path.exists(filename):
            return False

        try:
            file: IO = open(filename, 'r')
            data: any = json.load(file)

            users = data["users"]
            categories = data["categories"]
            expenses = data["expenses"]

            for user in users:
                self.get_user_list().add(
                    User(username=user["username"], password=user["password"], nif=user["nif"]).set_id(
                        user_id=user["id"]))

            for category in categories:
                self.get_category_list().add(Category(name=category["name"]).set_id(category_id=category["id"]))

            for expense in expenses:
                self.get_expense_list().add(Expense(user_id=expense["user_id"], category_id=expense["category_id"],
                                                    description=expense["description"], value=expense["value"]).set_id(
                    expense["id"]).set_timestamp(expense["timestamp"]))

            file.close()
            return True
        except FileNotFoundError:
            return False

from classes.Category import Category
from classes.Expense import Expense
from classes.LinkedList import LinkedList
from classes.Node import Node
from classes.User import User


class ExpenseList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    def get_expenses_by_timestamp_range(self, minimum: int, maximum: int) -> LinkedList | None:
        expenses_list: LinkedList = LinkedList()
        first_node: Node | None = self.get_first()

        if first_node is None:
            return None

        for index in range(self.size()):
            expense: Expense | None = first_node.get_data()
            if expense is not None and minimum < expense.get_timestamp() < maximum:
                expenses_list.insert_first(expense)
            first_node = first_node.get_node()

        if expenses_list.size() == 0:
            return None

        return expenses_list

    def get_expenses_by_user(self, user: User) -> LinkedList | None:
        expenses_list: LinkedList = LinkedList()
        first_node: Node | None = self.get_first()

        if first_node is None:
            return None

        for index in range(self.size()):
            expense: Expense | None = first_node.get_data()
            if expense is not None and expense.get_user().get_id() == user.get_id():
                expenses_list.insert_first(expense)
            first_node = first_node.get_node()

        if expenses_list.size() == 0:
            return None

        return expenses_list

    def get_expenses_by_user_and_category(self, user: User, category: Category) -> LinkedList | None:
        expenses_list: LinkedList = LinkedList()
        first_node: Node | None = self.get_first()

        if first_node is None:
            return None

        for index in range(self.size()):
            expense: Expense | None = first_node.get_data()
            if expense is not None and expense.get_user().get_id() == user.get_id() and expense.get_category().get_id() == category.get_id():
                expenses_list.insert_first(expense)
            first_node = first_node.get_node()

        if expenses_list.size() == 0:
            return None

        return expenses_list

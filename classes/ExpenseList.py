from classes.Category import Category
from classes.Expense import Expense
from classes.LinkedList import LinkedList
from classes.User import User


class ExpenseList(LinkedList[Expense]):
    def __init__(self):
        LinkedList.__init__(self)

    def get_expenses_filtered(
            self,
            user: User = None,
            categories: list[Category] = None,
            timestamp_minimum: int = None,
            timestamp_maximum: int = None,
            value_order: str = None,
            value_minimum: int = None,
            value_maximum: int = None,
            description: str = None
    ) -> LinkedList | None:
        expenses_list: list[Expense] = []
        final_list = LinkedList[Expense]()
        node = self.get_first()

        for index in range(self.size()):
            if node is not None:
                expenses_list.append(node.get_data())
            node = node.get_node()

        if user is not None:
            expenses_list = [expense for expense in expenses_list if expense.get_user().get_id() == user.get_id()]

        if categories is not None:
            aux = []
            for category in categories:
                for expense in expenses_list:
                    if expense.get_category().get_id() == category.get_id():
                        aux.append(expense)
            expenses_list = aux

        if description is not None:
            expenses_list = [expense for expense in expenses_list if description in expense.get_description()]

        if timestamp_minimum is not None:
            expenses_list = [expense for expense in expenses_list if expense.get_timestamp() > timestamp_minimum]

        if timestamp_maximum is not None:
            expenses_list = [expense for expense in expenses_list if expense.get_timestamp() < timestamp_maximum]

        if value_minimum is not None:
            expenses_list = [expense for expense in expenses_list if expense.get_value() > value_minimum]

        if value_maximum is not None:
            expenses_list = [expense for expense in expenses_list if expense.get_value() < value_maximum]

        if value_order is not None:
            if value_order == "asc":
                expenses_list = sorted(expenses_list, key=lambda x: x.get_value(), reverse=True)
            else:
                expenses_list = sorted(expenses_list, key=lambda x: x.get_value(), reverse=False)

        for expense in expenses_list:
            final_list.insert_first(expense)

        if final_list.size() == 0:
            return None

        return final_list

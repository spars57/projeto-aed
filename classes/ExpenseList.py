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
            value_minimum: int = None,
            value_maximum: int = None,
            description: str = None
    ) -> LinkedList | None:
        final_list = LinkedList[Expense]()

        if user is not None:
            first_node = self.get_first()
            final_list.clear()
            while first_node is not None:
                if first_node.get_data().get_user().get_id() == user.get_id():
                    final_list.insert_first(first_node.get_data())
                first_node = first_node.get_node()

        if categories is not None and len(categories) > 0:
            first_node = self.get_first()
            final_list.clear()
            while first_node is not None:
                if first_node.get_data().get_category().get_name() == categories[0].get_name():
                    final_list.insert_first(first_node.get_data())
                first_node = first_node.get_node()

        if description is not None:
            first_node = final_list.get_first()
            final_list.clear()

            while first_node is not None:
                if first_node.get_data().get_description() == description:
                    final_list.insert_first(first_node.get_data())
                first_node = first_node.get_node()

        if timestamp_minimum is not None:
            first_node = final_list.get_first()
            final_list.clear()

            while first_node is not None:
                if first_node.get_data().get_timestamp() >= timestamp_minimum:
                    final_list.insert_first(first_node.get_data())
                first_node = first_node.get_node()

        if timestamp_maximum is not None:
            first_node = final_list.get_first()
            final_list.clear()

            while first_node is not None:
                if first_node.get_data().get_timestamp() <= timestamp_maximum:
                    final_list.insert_first(first_node.get_data())
                first_node = first_node.get_node()

        if value_minimum is not None:
            first_node = final_list.get_first()
            final_list.clear()

            while first_node is not None:
                if first_node.get_data().get_value() >= value_minimum:
                    final_list.insert_first(first_node.get_data())
                first_node = first_node.get_node()

        if value_maximum is not None:
            first_node = final_list.get_first()
            final_list.clear()

            while first_node is not None:
                if first_node.get_data().get_value() <= value_maximum:
                    final_list.insert_first(first_node.get_data())
                first_node = first_node.get_node()

        if final_list.size() == 0:
            return None

        return final_list

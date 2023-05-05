from classes.Budget import Budget
from classes.LinkedList import LinkedList
from classes.Node import Node
from classes.User import User


class BudgetList(LinkedList[Budget]):

    def __init__(self):
        LinkedList.__init__(self)

    def get_budget_by_user(self, user: User) -> LinkedList | None:
        node: Node = self.get_first()
        aux: list[Budget] = []
        for i in range(self.size()):
            data = node.get_data()
            if data is not None and data.get_user().get_id() == user.get_id():
                aux.append(data)
            node = node.get_node()

        final_list = LinkedList()
        for budget in aux:
            final_list.insert_first(budget)

        if final_list.size() == 0:
            return None

        return final_list

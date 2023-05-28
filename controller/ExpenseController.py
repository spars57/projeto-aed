from classes.Category import Category
from classes.Expense import Expense
from classes.LinkedList import LinkedList
from classes.Node import Node
from modal.Modal import Modal


class ExpenseController:
    def __init__(self, modal: Modal):
        self.__modal: Modal = modal
        # Proxify ExpenseList Methods
        self.get_expenses_filtered = modal.get_expense_list().get_expenses_filtered

    def create_expense(self, category: Category, value: float, timestamp: float | int,
                       description: str = "") -> str:

        return self.__add_expense(
            Expense(
                user=self.__modal.get_current_user(),
                category=category,
                description=description,
                value=value,
                timestamp=timestamp
            ))

    def get_suggestions(self) -> LinkedList[Category]:
        expenses = self.__modal.get_expense_list().get_expenses_filtered(user=self.__modal.get_current_user())
        final_list = LinkedList[Category]()
        aux: dict = {}

        if expenses is None:
            return final_list

        first_node: Node[Expense] = expenses.get_first()

        if first_node is None:
            return final_list

        while first_node is not None:
            expense = first_node.get_data()
            key = expense.get_category().get_name()
            if key not in aux.keys():
                aux[key] = 0
            aux[key] += expense.get_value()
            first_node = first_node.get_node()

        aux = dict(sorted(aux.items(), key=lambda x: x[1], reverse=True))

        for key in aux.keys():
            final_list.insert_first(self.__modal.get_category_list().get_category_by_name(key))

        return final_list

    def __add_expense(self, expense: Expense) -> str:
        expense_list = self.__modal.get_expense_list()
        user_list = self.__modal.get_user_list()
        category_list = self.__modal.get_category_list()

        if user_list.get_user_by_username(expense.get_user().get_username()) is None:
            return f"Utilizador '{expense.get_user().get_username()}' não registado"

        if category_list.get_category_by_name(expense.get_category().get_name()) is None:
            return f"Categoria '{expense.get_category().get_name()}' não registada"

        if float(expense.get_value()) > expense.get_user().get_balance():
            return f"Saldo insuficiente, o seu saldo é {expense.get_user().get_balance()}€ e a operação que tentou efetuar é de {expense.get_value()}€"

        expense.get_user().set_balance(expense.get_user().get_balance() - float(expense.get_value()))
        expense_list.insert_first(expense)

        return f"Operação '{expense.get_description()}' registada com sucesso"

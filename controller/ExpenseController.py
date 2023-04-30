from classes.Budget import Budget
from classes.Category import Category
from classes.Expense import Expense
from classes.Node import Node
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

    def add_expense(self, expense: Expense) -> str:
        expense_list = self.__modal.get_expense_list()
        user_list = self.__modal.get_user_list()
        category_list = self.__modal.get_category_list()
        budget_list = self.__modal.get_budget_list().get_budget_by_user(expense.get_user())

        if user_list.get_user_by_username(expense.get_user().get_username()) is None:
            return f"Utilizador '{expense.get_user().get_username()}' não registado"

        if category_list.get_category_by_name(expense.get_category().get_name()) is None:
            return f"Categoria '{expense.get_category().get_name()}' não registada"

        if expense.get_value() > expense.get_user().get_balance():
            return f"Saldo insuficiente, o seu saldo é {expense.get_user().get_balance()}€ e a operação que tentou efetuar é de {expense.get_value()}€"

        if budget_list is not None:
            # filter budgets associated with current expense category and matching current time stamp
            aux: list[Budget] = []
            node: Node = budget_list.get_first()
            for i in range(budget_list.size()):
                if node is not None:
                    data: Budget = node.get_data()
                    if data is not None and data.get_category().get_id() == expense.get_category().get_id() and data.get_valid_from() <= expense.get_timestamp() <= data.get_valid_until():
                        aux.append(data)
                    node = node.get_node()

            # Remove value from all budgets:
            for bugdet in aux:
                final_value = bugdet.get_value() - expense.get_value()
                if final_value < 0:
                    return f"O orçamento {bugdet.get_name()} foi ultrapassado"
                bugdet.set_value(0 if final_value < 0 else final_value)

        expense.get_user().set_balance(expense.get_user().get_balance() - expense.get_value())
        expense_list.insert_first(expense)

        return f"Operação '{expense.get_description()}' registada com sucesso"

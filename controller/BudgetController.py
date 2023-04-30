from classes.Budget import Budget
from classes.Category import Category
from classes.User import User
from modal.Modal import Modal


class BudgetController:
    def __init__(self, modal: Modal):
        self.__modal: Modal = modal
        self.get_budget_by_user = modal.get_budget_list().get_budget_by_user

    @staticmethod
    def create_budget(name: str, user: User, category: Category, value: float, valid_from: float,
                      valid_until: float) -> Budget:
        return Budget(name=name, user=user, category=category, value=value, valid_from=valid_from,
                      valid_until=valid_until)

    def add_budget(self, budget: Budget) -> str:
        budget_list = self.__modal.get_budget_list()
        budget_list.insert_first(budget)
        return 'Orçamento criado com sucesso'

from controller.BudgetController import BudgetController
from controller.CategoryController import CategoryController
from controller.ExpenseController import ExpenseController
from controller.UserController import UserController
from modal.Modal import Modal


class Controller(
    UserController,
    CategoryController,
    ExpenseController,
    BudgetController
):
    def __init__(self, modal: Modal):
        self.__modal: modal = modal
        UserController.__init__(self, modal=modal)
        CategoryController.__init__(self, modal=modal)
        ExpenseController.__init__(self, modal=modal)
        BudgetController.__init__(self, modal=modal)

    def get_modal(self) -> Modal:
        return self.__modal

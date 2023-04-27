from classes.Expense import Expense


class ExpenseList:
    def __init__(self, value: Expense = None) -> None:
        if value is None:
            value = []
        self.__list: list[Expense] = value

    def add(self, expense: Expense) -> None:
        self.__list.append(expense)

    def delete_by_expense_id(self, expense_id: str) -> None:
        self.__list = [expense for expense in self.__list if expense.get_id() != expense_id]

    def get(self) -> list[Expense]:
        return self.__list

    def get_by_user_id(self, user_id: str) -> list[Expense]:
        return [expense for expense in self.__list if expense.get_user() == user_id]

    def get_by_category_id(self, category_id: str) -> list[Expense]:
        return [expense for expense in self.__list if expense.get_category() == category_id]

    def get_by_timestamp(self, timestamp: str) -> list[Expense]:
        return [expense for expense in self.__list if expense.get_timestamp() == timestamp]

    def get_by_timestamp_range(self, timestamp_range: [float, float]) -> list[Expense]:
        return [expense for expense in self.__list if timestamp_range[0] < expense.get_timestamp() < timestamp_range[1]]

    def get_by_value_range(self, value_range: [float, float]) -> list[Expense]:
        return [expense for expense in self.__list if value_range[0] < expense.get_value() < value_range[1]]

    def get_by_expense_id(self, expense_id: str) -> Expense | None:
        found: list[Expense] = [expense for expense in self.__list if expense.get_id() == expense_id]
        if len(found) > 0:
            return found[0]
        return None

    def set(self, value: list[Expense]):
        self.__list = value

    def json(self) -> dict:
        return self.__dict__

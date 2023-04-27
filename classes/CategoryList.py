from classes.Category import Category


class CategoryList:
    def __init__(self, value: Category = None) -> None:
        if value is None:
            value = []
        self.__list: list[Category] = value

    def add(self, category: Category) -> None:
        self.__list.append(category)

    def delete_by_id(self, category_id: str) -> None:
        self.__list = [category for category in self.__list if category.get_id() != category_id]

    def get(self) -> list[Category]:
        return self.__list

    def get_by_id(self, category_id: str) -> Category | None:
        found: list[Category] = [category for category in self.__list if category.get_id() == category_id]
        if len(found) > 0:
            return found[0]
        return None

    def get_by_name(self, name: str) -> Category | None:
        found: list[Category] = [category for category in self.__list if category.get_name() == name]
        if len(found) > 0:
            return found[0]
        return None

    def set(self, value: list[Category]):
        self.__list = value

    def json(self) -> dict:
        return self.__dict__

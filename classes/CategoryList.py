from classes.Category import Category
from classes.LinkedList import LinkedList


class CategoryList(LinkedList[Category]):

    def __init__(self):
        LinkedList.__init__(self)

    def get_category_by_name(self, name: str) -> Category | None:
        first_node = self.get_first()

        if first_node is None:
            return None

        for index in range(self.size()):
            category = first_node.get_data()
            if category is not None and category.get_name() == name:
                return category
            first_node = first_node.get_node()

from classes.Category import Category
from modal.Modal import Modal


class CategoryController:
    def __init__(self, modal: Modal):
        self.__modal: Modal = modal
        self.get_category_by_name = modal.get_category_list().get_category_by_name

    def create_category(self, name: str) -> str:
        return self.__add_category(Category(name=name))

    def get_all_category_names(self) -> list[str] | str:
        node = self.__modal.get_category_list().get_first()
        if node is None:
            return 'No options available'
        names: list[str] = []

        while node is not None:
            names.append(node.get_data().get_name())
            node = node.get_node()

        return names

    def __add_category(self, category: Category) -> str:
        category_list = self.__modal.get_category_list()

        if category_list.get_category_by_name(category.get_name()) is not None:
            return f"Já existe uma categoria registada com o nome '{category.get_name()}'"

        category_list.insert_first(category)

        return f"Categoria '{category.get_name()}' registada com sucesso"

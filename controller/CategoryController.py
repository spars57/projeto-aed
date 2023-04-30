from classes.Category import Category
from modal.Modal import Modal


class CategoryController:
    def __init__(self, modal: Modal):
        self.__modal: Modal = modal

    @staticmethod
    def create_category(name: str) -> Category:
        return Category(name=name)

    def add_category(self, category: Category) -> str:
        category_list = self.__modal.get_category_list()

        if category_list.get_category_by_name(category.get_name()) is not None:
            return f"Já existe uma categoria registada com o nome '{category.get_name()}'"

        category_list.insert_first(category)

        return f"Categoria '{category.get_name()}' registada com sucesso"

from classes.LinkedListItem import LinkedListItem


class LinkedList:
    def __init__(self):
        self.__list: list[LinkedListItem] = []

    def is_empty(self) -> bool:
        return len(self.__list) == 0

    def size(self) -> bool:
        return len(self.__list) == 0

    def get_first(self) -> any:
        try:
            return self.__list[0]
        except IndexError:
            return None

    def get_last(self) -> any:
        try:
            return self.__list[len(self.__list) - 1]
        except IndexError:
            return None

    def get(self, index) -> any:
        try:
            [self.__list[i] for i in range(len(self.__list)) if i == index][0]
        except IndexError:
            return None

    def insert_first(self, item: LinkedListItem) -> None:
        first_element = self.get_first()

        if first_element is not None:
            item.set_next(first_element)

        self.__list.insert(0, item)

    def remove_first(self) -> None:
        first = self.get_first()
        self.__list = [item for item in self.__list if item.get_id() != first.get_id()]

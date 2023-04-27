from classes.User import User


class UserList:
    __list: list[User] = []

    def __init__(self, value: list[User] = None):
        if value is None:
            value = []
        self.__list: list[User] = value

    def add(self, user: User) -> None:
        self.__list.append(user)

    def delete_by_id(self, user_id: str) -> None:
        self.__list = [user for user in self.__list if user.get_id() != user_id]

    def get(self) -> list[User]:
        return self.__list

    def get_by_id(self, user_id: str) -> User | None:
        found: list[User] = [user for user in self.__list if user.get_id() == user_id]
        if len(found) > 0:
            return found[0]
        return None

    def get_by_username(self, username: str) -> User | None:
        found: list[User] = [user for user in self.__list if user.get_username() == username]
        if len(found) > 0:
            return found[0]
        return None

    def set(self, value: list[User]):
        self.__list = value

    def json(self) -> dict:
        return self.__dict__

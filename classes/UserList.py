from uuid import uuid4

from classes.LinkedList import LinkedList
from classes.Node import Node
from classes.User import User


class UserList(LinkedList[User]):

    def __init__(self):
        LinkedList.__init__(self)

    def get_user_by_id(self, user_id: uuid4) -> User | None:
        first_node = self.get_first()

        if first_node is None:
            return None

        for index in range(self.size()):
            user = first_node.get_data()
            if user.get_id() == user_id:
                return user
            first_node = first_node.get_node()

    def get_user_by_username(self, username: str) -> User | None:
        first_node: Node | None = self.get_first()

        if first_node is None:
            return None

        for index in range(self.size()):
            user: User | None = first_node.get_data()

            if user is not None and user.get_username() == username:
                return user

            first_node = first_node.get_node()

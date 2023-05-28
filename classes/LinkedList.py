from typing import TypeVar, Generic

from classes.Node import Node
from collections import namedtuple

T = TypeVar('T')

LinkedListNode = namedtuple("LinkedListNode", ["name", "age", "salary"])
class LinkedList(Generic[T]):
    def __init__(self):
        self.__head: Node[T] = None
        self.__size: int = 0

    def is_empty(self) -> bool:
        return self.__size == 0

    def size(self) -> int:
        return self.__size

    def get_first(self) -> Node[T] | None:
        return self.__head

    def get_last(self) -> T | None:
        if self.__head is None:
            return None

        node = self.__head.get_node()

        while node.get_node() is not None:
            node = node.get_node()

        return node

    def insert_first(self, data: T) -> None:
        first_node = self.get_first()
        new_node = Node(data)

        if first_node is not None:
            new_node.set_node(first_node)

        self.__size += 1
        self.__head = new_node

    def sort_asc(self, attribute):
        if self.head is None or self.head.next is None:
            return

        # Realiza a classificação ascendente com base no atributo especificado
        self.head = self.merge_sort_linked_list(self.head, attribute)

    def merge_sort_linked_list(self, head, attribute):
        if head is None or head.next is None:
            return head

        # Dividir a linked list em duas partes
        mid = self.get_middle_node(head)
        mid_next = mid.next
        mid.next = None

        # Classificar recursivamente as duas partes
        left = self.merge_sort_linked_list(head, attribute)
        right = self.merge_sort_linked_list(mid_next, attribute)

        # Mesclar as duas partes classificadas
        sorted_head = self.merge_sorted_lists(left, right, attribute)

        return sorted_head

    def get_middle_node(self, head):
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_sorted_lists(self, left, right, attribute):
        dummy = LinkedListNode(None, None, None)
        current = dummy

        while left is not None and right is not None:
            if getattr(left, attribute) <= getattr(right, attribute):
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        if left is not None:
            current.next = left
        else:
            current.next = right

        return dummy.next
from LinkedList import LinkedList
from LinkedListItem import LinkedListItem

myList = LinkedList()
myElement1 = LinkedListItem("Item 1", None)
myElement2 = LinkedListItem("Item 2", None)

myList.insert_first(myElement1)
myList.insert_first(myElement2)

myList.remove_first()

test = myList.get_first()
print(test.get_value())

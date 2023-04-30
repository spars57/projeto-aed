from classes.Category import Category
from classes.Expense import Expense
from controller.Controller import Controller
from modal.Modal import Modal

myController = Controller(Modal())

u1 = myController.create_user("spars", "1234", 254799221)
u2 = myController.create_user("Jonh", "1111", 254799221)

myController.add_user(u1)
myController.add_user(u2)

c1 = Category("Category 1")
c2 = Category("Category 2")
c3 = Category("Category 3")

myController.add_category(c1)
myController.add_category(c2)
myController.add_category(c3)

e1 = Expense(user=u1, category=c1, value=99, description="A", timestamp=1)
e2 = Expense(user=u1, category=c2, value=229, description="B", timestamp=2)
e3 = Expense(user=u1, category=c3, value=657, description="C", timestamp=3)

e4 = Expense(user=u2, category=c1, value=877, description="D", timestamp=4)
e5 = Expense(user=u2, category=c2, value=421, description="E", timestamp=5)
e6 = Expense(user=u2, category=c3, value=1023, description="F", timestamp=6)

e7 = Expense(user=u2, category=c1, value=432, description="G", timestamp=4)
e8 = Expense(user=u2, category=c2, value=544, description="H", timestamp=5)
e9 = Expense(user=u2, category=c3, value=623, description="I", timestamp=6)

e10 = Expense(user=u1, category=c1, value=433, description="J", timestamp=4)
e11 = Expense(user=u1, category=c2, value=231, description="K", timestamp=5)
e12 = Expense(user=u1, category=c3, value=354, description="L", timestamp=6)

myController.add_expense(e1)
myController.add_expense(e2)
myController.add_expense(e3)
myController.add_expense(e4)
myController.add_expense(e5)
myController.add_expense(e6)
myController.add_expense(e7)
myController.add_expense(e8)
myController.add_expense(e9)
myController.add_expense(e10)
myController.add_expense(e11)
myController.add_expense(e12)

nodes = myController.get_expenses_filtered(user=u1, categories=[c3, c2, c1], order="desc")

current_node = nodes.get_first()

for i in range(nodes.size()):
    if current_node is not None:
        expense = current_node.get_data()
        print("User:", expense.get_user().get_username())
        print("Category:", expense.get_category().get_name())
        print("Value:", expense.get_value())
    current_node = current_node.get_node()

from time import time

from classes.Budget import Budget
from classes.Category import Category
from classes.Expense import Expense
from controller.Controller import Controller
from modal.Modal import Modal

myController = Controller(Modal())

u1 = myController.create_user("spars", "1234", 254799221)
u2 = myController.create_user("Jonh", "1111", 254799221)

u1.set_balance(500)
u2.set_balance(1000)

print(myController.add_user(u1))
print(myController.add_user(u2))

print('Login Spars:', myController.login("spars", u1.get_password()))
print('Login Spars:', myController.login("7777", ""))

c1 = Category("Category 1")
c2 = Category("Category 2")
c3 = Category("Category 3")

print(myController.add_category(c1))
print(myController.add_category(c2))
print(myController.add_category(c3))

b1 = Budget(name="b1", user=u1, category=c1, value=1000, valid_from=time(), valid_until=time() + 50000)
myController.add_budget(b1)

e1 = Expense(user=u1, category=c1, value=99, description="A", timestamp=time())
e2 = Expense(user=u1, category=c2, value=229, description="B", timestamp=time())
e3 = Expense(user=u1, category=c3, value=657, description="C", timestamp=time())

print(myController.add_expense(e1))
print(myController.add_expense(e2))
print(myController.add_expense(e3))
print(myController.add_expense(e1))
print(myController.add_expense(e2))
print(myController.add_expense(e3))

nodes = myController.get_budget_by_user(u1)

current_node = nodes.get_first()

for i in range(nodes.size()):
    if current_node is not None:
        budget = current_node.get_data()
    current_node = current_node.get_node()

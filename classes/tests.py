from Category import Category
from CategoryList import CategoryList
from Expense import Expense
from ExpenseList import ExpenseList
from User import User
from UserList import UserList

myUser = User(username='spars', password='spars', nif="12345")
myUser2 = User(username='Jonh', password='Jonh', nif="12345")

myCategory1 = Category('Cars')
myCategory2 = Category('Food')
myCategory3 = Category('Drugs')

expense_list = ExpenseList()

expense_list.insert_first(Expense(user=myUser, category=myCategory1, value=50, timestamp=1234, description="Expense1"))
expense_list.insert_first(Expense(user=myUser2, category=myCategory1, value=50, timestamp=1234, description="Expense2"))
expense_list.insert_first(Expense(user=myUser2, category=myCategory1, value=50, timestamp=1234, description="Expense3"))
expense_list.insert_first(Expense(user=myUser, category=myCategory1, value=50, timestamp=1234, description="Expense4"))

print(expense_list.get_expenses_by_user_and_category(myUser, myCategory2))

user_list = UserList()
category_list = CategoryList()

user_list.insert_first(myUser)
user_list.insert_first(myUser2)

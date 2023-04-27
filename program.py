import string
from random import random, choice

from config import controller
from view.View import View


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(choice(letters) for i in range(length))
    return result_str


controller.get_modal().read_from_file("./data/users.json")

myUser = controller.get_modal().get_user_list().get_by_username("spars57")

controller.create_expense(
    user_id=controller.get_modal().get_user_list().get_by_username("spars57").get_id(),
    category_id=controller.get_modal().get_category_list().get_by_name("Food").get_id(),
    description="Testing Expense",
    value=float(random())
)

controller.create_category(name=get_random_string(8))

controller.create_user(username=get_random_string(16), password=get_random_string(16), nif="254799221")

for user in controller.get_modal().get_user_list().get():
    print(user.get_username())

controller.get_modal().save_to_file("./data/users.json")

View().main()

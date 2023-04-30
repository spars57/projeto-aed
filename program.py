from controller.Controller import Controller
from modal.Modal import Modal

myController = Controller(Modal())

my_user = myController.create_user("spars", "1234", 254799221)
myController.add_user(my_user)

login = myController.login("spars", my_user.get_password())

if login:
    print('Login efetuado com sucesso!')
else:
    print('Login falhou!')

login = myController.login("não_existo", "sss")

if login:
    print('Login efetuado com sucesso!')
else:
    print('Login falhou!')

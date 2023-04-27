from tkinter import Tk
from tkinter.ttk import Frame, Label, Entry, Style, Button

from config import controller
from utils.passwords import encrypt

register_main = Tk()
register_frame = Frame(register_main, height=500, width=500)
register_frame.grid()

Style().configure("TLabel", font=('Helvetica', 13))

controller.get_modal()


def on_login_click() -> None:
    username = entryboxs['username'].get()
    password = encrypt(entryboxs['password'].get())
    user = controller.get_modal().get_user_list().get_by_username(username)

    print('Username', username)
    print('Password', password)
    print('user', user)

    if user is None:
        return None

    if len(user) == 0:
        return None

    if not user[0].get_password() == password:
        print('Login Failed')
        labels['welcome'].config(text="Something went wrong.")
    else:
        print('Login Succeded')


labels = {
    "welcome": Label(register_frame, text="Bem vindo ao gestor de despesas"),
    "username": Label(register_frame, text="Nome de utilizador"),
    "password": Label(register_frame, text="Password"),
}

entryboxs = {
    "username": Entry(register_frame, name="username"),
    "password": Entry(register_frame, name="password", show="*")
}

buttons = {
    "login": Button(register_frame, text="Login", command=on_login_click),
    "register": Button(register_frame, text="Register")
}

labels["welcome"].grid(column=0, row=0, columnspan=2)
labels["username"].grid(column=0, row=1)
entryboxs["username"].grid(column=1, row=1)
labels["password"].grid(column=0, row=3)
entryboxs["password"].grid(column=1, row=3)
buttons["login"].grid(column=1, row=4)
buttons["register"].grid(column=0, row=4, columnspan=1)

register_frame.mainloop()

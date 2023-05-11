import re
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

from controller.Controller import Controller
from modal.Modal import Modal

modal = Modal()


class Frame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(MainFrame)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class MainFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#17223b")
        self.master.resizable(False, False)
        self.master.title('Iniciar Sessão')
        self.user_controller = Controller(modal)
        self.user_controller.create_user("a", "1", 229156347)
        self.user_controller.create_user("b", "2", 229156347)

        self.welc = tk.Label(self, text="Bem Vindo ao Gestor de Despesas", font=("Comic Sans MS", 14), bg="#17223b",
                             fg="#ffa200")
        self.welc.grid(row=0, column=1)

        self.logo = tk.PhotoImage(file="Logo.png")
        self.logo = self.logo.subsample(4)
        self.logo_label = tk.Label(self, image=self.logo, bg="#17223b")
        self.logo_label.grid(rowspan=1, column=1)

        self.user_label = tk.Label(self, text="Username:", font=("Comic Sans MS", 14), bg="#17223b", fg="#ffa200")
        self.user_label.grid(row=2, column=0)
        self.user_entry = tk.Entry(self, font=(18), bg="#6b778d", fg="#17223b")
        self.user_entry.grid(row=2, column=1)

        self.password_label = tk.Label(self, text="Password:", font=("Comic Sans MS", 14), bg="#17223b", fg="#ffa200")
        self.password_label.grid(row=3, column=0)
        self.password_entry = tk.Entry(self, show="*", font=(18), bg="#6b778d", fg="#17223b")
        self.password_entry.grid(row=3, column=1)

        self.login_button = tk.Button(self, text="Iniciar Sessão", font=("Comic Sans MS", 12), bg="#6b778d",
                                      fg="#17223b",
                                      command=self.login)
        self.login_button.grid(row=4, column=1)

        self.create_button = tk.Button(self, text="Criar Utilizador", font=("Comic Sans MS", 12), bg="#6b778d",
                                       fg="#17223b",
                                       command=lambda: self.master.switch_frame(RegisterFrame))
        self.create_button.grid(row=5, column=1)

        self.exit = tk.Button(self, text="Sair", font=("Comic Sans MS", 10), bg="#6b778d", fg="#17223b",
                              command=lambda: self.master.destroy())
        self.exit.grid(row=5, column=0)

    def login(self):
        user = self.user_entry.get()
        password = self.password_entry.get()

        if not user != '' and not password != '':
            showerror('Error', 'Campos Vazios')
            return

        response = self.user_controller.login(user, password)
        print('response:', response)

        if response:
            showinfo('Sucesso', 'Login Efetuado')
            self.master.switch_frame(SessionFrame)
        else:
            showerror('Error', 'Login Falhou')


class RegisterFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title('Criar Utilizador')
        self.master.resizable(False, False)
        self.verificar_numb = (self.register(self.verficar_nif))
        self.verificar_espaco = (self.register(self.verficar_espac))
        self.user_controller = Controller(modal)

        self.create_user_label = tk.Label(self, text="Username:").grid(row=0, column=0)
        self.create_user_entry = tk.Entry(self, validate='all', validatecommand=(self.verificar_espaco, '%P'))
        self.create_user_entry.grid(row=0, column=1)

        self.create_nif_label = tk.Label(self, text="NIF:").grid(row=1, column=0)
        self.create_nif_entry = tk.Entry(self, validate='all', validatecommand=(self.verificar_numb, '%P'))
        self.create_nif_entry.grid(row=1, column=1)

        self.create_password_label = tk.Label(self, text="Password:").grid(row=2, column=0)
        self.create_password_entry = tk.Entry(self, show="*", validate='all',
                                              validatecommand=(self.verificar_espaco, '%P'))
        self.create_password_entry.grid(row=2, column=1)

        self.rep_password_label = tk.Label(self, text="Repeat Password:").grid(row=3, column=0)
        self.rep_password_entry = tk.Entry(self, show="*", validate='all',
                                           validatecommand=(self.verificar_espaco, '%P'))
        self.rep_password_entry.grid(row=3, column=1)

        self.register_button = tk.Button(self, text="Registar Utilizador", command=lambda: self.registar())
        self.register_button.grid(row=4, column=1)

        self.voltar_button = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(MainFrame)).grid(row=4,
                                                                                                                 column=0)

    def registar(self):
        user = self.create_user_entry.get()
        password = self.create_password_entry.get()
        nif = self.create_nif_entry.get()
        repeat_pass = self.rep_password_entry.get()

        if not user != '' and not password != '' and not nif != '':
            showerror('Error', 'Um dos campos que preencheu está vazio')
            return

        if not password == repeat_pass:
            showerror('Error', 'Password e repetir password são diferentes')
            return

        response = self.user_controller.create_user(
            username=user,
            password=password,
            nif=int(nif))

        if response is None:
            showinfo('Sucesso', 'Utilizador Registado com Sucesso')
            self.master.switch_frame(MainFrame)
        else:
            showerror('Erro', response)

    # Limitar o que o User pode escrever
    def verficar_nif(self, digito):
        if str.isdigit(digito) or digito == "":
            return True
        else:
            return False

    def verficar_espac(self, P):
        if re.search(r"^\w*$", P):  # O re é o RegEx basicamente o que faz é ver se a string contém X padrão
            # O \W é equivalente a [^a-zA-Z0-9] o *$ basicamente é para que corra na string toda inves de so no 1º char
            return True
        else:
            return False


class SessionFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Sessão")
        self.master.resizable(False, False)

        self.label = tk.Label(self, text="Bem Vindo").pack()

        self.criar = tk.Button(self, text="Criar Despesa", command=lambda: master.switch_frame(CreateDFrame)).pack()
        self.criar = tk.Button(self, text="Vizualizar Despesa", command=lambda: master.switch_frame(VerDFrame)).pack()

        self.retroceder = tk.Button(self, text="Terminar Sessão", command=lambda: master.switch_frame(MainFrame)).pack()


class CreateDFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Criar Despesa")
        self.master.resizable(False, False)

        self.categoria_label = tk.Label(self, text="Categoria:").pack()
        self.categoria_entry = ttk.Combobox(self).pack()

        self.valor_label = tk.Label(self, text="Valor:").pack()
        self.valor_entry = tk.Entry(self).pack()

        self.data_label = tk.Label(self, text="Data:").pack()

        self.descricao_label = tk.Label(self, text="Descrição:").pack()
        self.descricao = tk.Text(self).pack()

        self.registar = tk.Button(self, text="Registar Despesa").pack()

        self.retroceder = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(SessionFrame)).pack()


class VerDFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Ver Despesa")
        self.master.resizable(False, False)

        self.retroceder = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(SessionFrame)).pack()

import tkinter as tk
from tkinter.messagebox import*
from controller.UserController import UserController

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

    def registar(self, user, password, nif):
        UserController.create_user(self.creauser, self.creapassword, self.creanif)

    def login(self, user, password):
        UserController.login(self.user, self.password)

        
class MainFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title('Iniciar Sessão')
        self.master.geometry('400x125')

        mensagem = "Erro com o user ou pass"

        self.welc = tk.Label(self, text="Bem vindo ao gestor de despesas").grid(row=0, column=1)
        
        self.user1 = tk.Label(self, text="Username:").grid(row=1, column=0)
        self.user = tk.Entry(self)
        self.user.get()
        self.user.grid(row=1, column=1)

        self.password1 = tk.Label(self, text="Password:").grid(row=2, column=0)
        self.password = tk.Entry(self, show="*")
        self.password.get()
        self.password.grid(row=2, column=1)

        self.iniciar = tk.Button(self, text="Iniciar Sessão", command=(lambda: master.switch_frame(SessionFrame) if (master.login) else showerror('Error', mensagem))).grid(row=3, column=1)

        self.criar1 = tk.Button(self, text="Criar Utilizador", command=lambda: master.switch_frame(RegisterFrame)).grid(row=4, column=1)

class RegisterFrame(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.master.title('Criar Utilizador')
        self.master.geometry('350x135')

        mensagem2 = 'Utilizador Registado com Sucesso'
        mensagem3 = 'Erro na criação do user'

        self.creauser1 = tk.Label(self, text="Username:").grid(row=0, column=0)
        self.creauser = tk.Entry(self)
        self.creauser.get()
        self.creauser.grid(row=0, column=1)

        self.creanif1 = tk.Label(self, text="NIF:").grid(row=1, column=0)
        self.creanif = tk.Entry(self)
        self.creanif.get()
        self.creanif.grid(row=1, column=1)

        self.creapassword1 = tk.Label(self, text="Password:").grid(row=2, column=0)
        self.creapassword = tk.Entry(self, show="*")
        self.creapassword.get()
        self.creapassword.grid(row=2, column=1)

        self.crearep_pass1 = tk.Label(self, text="Repeat Password:").grid(row=3, column=0)
        self.crearep_pass = tk.Entry(self, show="*").grid(row=3, column=1)

        self.regis = tk.Button(self, text="Registrar Utilizador", command=(lambda: showerror('Sucesso', mensagem2) and master.switch_frame(MainFrame) if master.registar else showerror('Erro', mensagem3)))
        self.regis.grid(row=4, column=1)

        self.retroceder = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(MainFrame)).grid(row=4, column=0)

class SessionFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Sessão")
        self.master.geometry("300x100")

        self.label = tk.Label(self, text="Bem Vindo").pack()

        self.criar = tk.Button(self, text="Criar Despesa", command=lambda: master.switch_frame(CreateDFrame)).pack()
        self.criar = tk.Button(self, text="Vizualizar Despesa", command=lambda: master.switch_frame(VerDFrame)).pack()

        self.retroceder = tk.Button(self, text="Terminar Sessão", command=lambda: master.switch_frame(MainFrame)).pack()

class CreateDFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Criar Despesa")
        self.master.geometry("300x100")

        self.retroceder = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(SessionFrame)).pack()

class VerDFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Ver Despesa")
        self.master.geometry("300x100")

        self.retroceder = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(SessionFrame)).pack()
    

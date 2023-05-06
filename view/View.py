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

        
class MainFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title('Iniciar Sessão')
        self.master.geometry('400x125')

        mensagem = "Erro com o user ou pass"

        self.welc = tk.Label(self, text="Bem vindo ao gestor de despesas").grid(row=0, column=1)
        
        self.user_label = tk.Label(self, text="Username:").grid(row=1, column=0)
        self.user_entry = tk.Entry(self)
        self.user_entry.get()
        self.user_entry.grid(row=1, column=1)

        self.password_label = tk.Label(self, text="Password:").grid(row=2, column=0)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.get()
        self.password_entry.grid(row=2, column=1)

        self.login_button = tk.Button(self, text="Iniciar Sessão", command=(lambda: master.switch_frame(SessionFrame) if (self.login==True) else showerror('Error', mensagem))).grid(row=3, column=1)

        self.create_button = tk.Button(self, text="Criar Utilizador", command=lambda: self.master.switch_frame(RegisterFrame)).grid(row=4, column=1)

        self.exit = tk.Button(self, text="Sair", command=lambda: self.master.destroy()).grid(row=4, column=0)

    def login(self, user, password):
        if UserController.login(self.user, self.password) == True:
            return True

class RegisterFrame(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.master.title('Criar Utilizador')
        self.master.geometry('350x135')

        mensagem2 = 'Utilizador Registado com Sucesso'
        mensagem3 = 'Erro na criação do user'

        self.create_user_label = tk.Label(self, text="Username:").grid(row=0, column=0)
        self.create_user_entry = tk.Entry(self)
        self.create_user_entry.grid(row=0, column=1)

        self.create_nif_label = tk.Label(self, text="NIF:").grid(row=1, column=0)
        self.create_nif_entry = tk.Entry(self)
        self.create_nif_entry.grid(row=1, column=1)

        self.create_password_label = tk.Label(self, text="Password:").grid(row=2, column=0)
        self.create_password_entry = tk.Entry(self, show="*")
        self.create_password_entry.grid(row=2, column=1)

        self.rep_password_label = tk.Label(self, text="Repeat Password:").grid(row=3, column=0)
        self.rep_password_entry = tk.Entry(self, show="*").grid(row=3, column=1)

        self.register_button = tk.Button(self, text="Registrar Utilizador", command=(lambda: showerror('Sucesso', mensagem2) and master.switch_frame(MainFrame)
                            if (self.registar(self.creauser.get(), self.creapassword.get(), self.creanif.get())==True) else showerror('Erro', mensagem3)))
        self.register_button.grid(row=4, column=1)

        self.voltar_button = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(MainFrame)).grid(row=4, column=0)

    def registar(self, user, password, nif):
        if UserController.create_user(user, password, nif):
            return True
        return False

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
    

from view.RegisterForm import register_frame


class View:
    def main(self) -> None:
        register_frame.mainloop()


import tkinter as tk

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
        self.master.geometry('300x100')
        
        self.user1 = tk.Label(self, text="Username:").grid(row=0, column=0)
        self.user = tk.Entry(self).grid(row=0, column=1)

        self.password1 = tk.Label(self, text="Password:").grid(row=1, column=0)
        self.password = tk.Entry(self).grid(row=1, column=1)

        self.iniciar = tk.Button(self, text="Iniciar Sessão", command=lambda: master.switch_frame(SessionFrame)).grid(row=2, column=1)

        self.criar = tk.Button(self, text="Criar Utilizador", command=lambda: master.switch_frame(RegisterFrame)).grid(row=3, column=1)

class RegisterFrame(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.master.title('Criar Utilizador')
        self.master.geometry('350x135')

        self.user1 = tk.Label(self, text="Username:").grid(row=0, column=0)
        self.user = tk.Entry(self).grid(row=0, column=1)

        self.nif1 = tk.Label(self, text="NIF:").grid(row=1, column=0)
        self.nif = tk.Entry(self).grid(row=1, column=1)

        self.password1 = tk.Label(self, text="Password:").grid(row=2, column=0)
        self.password = tk.Entry(self).grid(row=2, column=1)

        self.rep_pass1 = tk.Label(self, text="Repeat Password:").grid(row=3, column=0)
        self.rep_pass = tk.Entry(self).grid(row=3, column=1)

        self.criar = tk.Button(self, text="Criar Utilizador").grid(row=4, column=1)

        self.retroceder = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(MainFrame)).grid(row=4, column=0)

class SessionFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Sessão")
        self.master.geometry("300x100")

        self.label = tk.Label(self, text="Bem Vindo User").pack()

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
    


if __name__ == "__main__":
    app = Frame()
    app.mainloop()
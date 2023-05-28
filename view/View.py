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

<<<<<<< Updated upstream
<<<<<<< Updated upstream
        self.retroceder = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(SessionFrame)).pack()
    
=======
=======
>>>>>>> Stashed changes
        

        self.cor_tabela = ttk.Style(self)
        self.cor_tabela.configure("Treeview.Heading", background="#6b778d", foreground="#17223b",
                                  font=("Comic Sans MS", 10))
        self.cor_tabela.configure("Treeview", background="#6b778d", foreground="#17223b", font=("Comic Sans MS", 10))
        self.tabela = ttk.Treeview(self, columns=["category", "description", "value", "timestamp"],
                                   show='headings', selectmode='browse', style="Treeview")

        self.tabela.heading("category", text="Category", command=lambda: self.tabela_header_click_asc("category"))
        self.tabela.heading("description", text="Description",
                            command=lambda: self.tabela_header_click_asc("description"))
        self.tabela.heading("value", text="Value", command=lambda: self.tabela_header_click_asc("value"))
        self.tabela.heading("timestamp", text="Date", command=lambda: self.tabela_header_click_asc("timestamp"))

<<<<<<< Updated upstream
        self.preencher_tabela()

=======
>>>>>>> Stashed changes
        self.tabela.grid(row=0, column=0, columnspan=2)

        self.preencher_tabela()

        self.categoria_label = tk.Label(self, text="Categoria:", font=("Comic Sans MS", 14), bg="#17223b",
                                        fg="#ffa200").grid(row=1, column=0, sticky='w')
        self.categoria_filtrar = ttk.Combobox(self, values=self.controller.get_all_category_names(), state='readonly')
        self.categoria_filtrar.grid(row=1, column=0, sticky='s')

        self.value_min = tk.Label(self, text="Valor Mínimo:", font=("Comic Sans MS", 14), bg="#17223b",
                                  fg="#ffa200").grid(row=2, column=0, sticky='w')
        self.value_min = tk.Entry(self, bg="#6b778d", fg="#17223b")
        self.value_min.grid(row=2, column=0, sticky='s')

        self.value_max = tk.Label(self, text="Valor Máximo:", font=("Comic Sans MS", 14), bg="#17223b",
                                  fg="#ffa200").grid(row=3, column=0, sticky='w')
        self.value_max = tk.Entry(self, bg="#6b778d", fg="#17223b")
        self.value_max.grid(row=3, column=0, sticky='s')

        self.date_min = tk.Label(self, text="Data Minima:", font=("Comic Sans MS", 14), bg="#17223b",
                                 fg="#ffa200").grid(row=4, column=0, sticky='w')
        self.data_min = DateEntry(self, width=16, foreground="white", bd=2, dateformat=4, date_pattern='YYYY-MM-DD')
        self.data_min.grid(row=4, column=0)

        self.data_max = tk.Label(self, text="Data Maxima:", font=("Comic Sans MS", 14), bg="#17223b",
                                 fg="#ffa200").grid(row=5, column=0, sticky='w')
        self.data_max = DateEntry(self, width=16, foreground="white", bd=2, dateformat=4, date_pattern='YYYY-MM-DD')
        self.data_max.grid(row=5, column=0)

        self.butao_filtrar = tk.Button(self, text="Filtrar", font=("Comic Sans MS", 12), bg="#6b778d",
                                       fg="#17223b", command=self.filtrar)
        self.butao_filtrar.grid(row=7, column=0, sticky='w')

        self.retroceder = tk.Button(self, text="Voltar", font=("Comic Sans MS", 12), bg="#6b778d",
                                    fg="#17223b", command=lambda: master.switch_frame(SessionFrame)).grid(
            column=0, row=8, sticky='e')

    def filtrar(self):
        category_name = self.categoria_filtrar.get() if self.categoria_filtrar.get() != "" else None
        category = self.controller.get_category_by_name(category_name)
        categories = []
        categories.append(category)
        value_minimum = int(self.value_min.get()) if self.value_min.get() != "" else None
        value_maximum = int(self.value_max.get()) if self.value_max.get() != "" else None

        if self.data_min.get_date() < self.data_max.get_date():
            date_minimum = self.data_min.get_date()
            date_maximum = self.data_max.get_date()

            date_minimum = calendar.timegm(date_minimum.timetuple())

            date_maximum = calendar.timegm(date_maximum.timetuple())

        expenses = self.controller.get_expenses_filtered(
            user=modal.get_current_user(),
            categories=categories,
            value_minimum=value_minimum,
            value_maximum=value_maximum,
            timestamp_minimum=date_minimum,
            timestamp_maximum=date_maximum
        )

        if expenses is None:
            showerror('Error', 'Sem despesas para mostrar')
        else:
            ## clear all table rows
            for i in self.tabela.get_children():
                self.tabela.delete(i)

            TABLE_ROWS = []

            node = expenses.get_first()

            while node is not None:
                data: Expense = node.get_data()

                self.tabela.insert("", "end",text=data.get_id(),values=      
                    (data.get_category().get_name(), 
                      data.get_description(), 
                      f"{str(data.get_value())}€",
                     str(datetime.fromtimestamp(data.get_timestamp()))))
                node = node.get_node()


    def preencher_tabela(self):
        expenses = self.controller.get_expenses_filtered(user=modal.get_current_user())

        if expenses is None:
            showerror('Error', 'Sem despesas para mostrar')
        else:
            node = expenses.get_first()

            while node is not None:
                data: Expense = node.get_data()

                self.tabela.insert("", "end",text=data.get_id(),values=      
                    (data.get_category().get_name(), 
                      data.get_description(), 
                      f"{str(data.get_value())}€",
                     str(datetime.fromtimestamp(data.get_timestamp()))))
                node = node.get_node()

    def tabela_header_click_asc(self, coluna):
        expenses = self.controller.get_expenses_filtered(user=modal.get_current_user())

        if expenses is None:
            showerror('Error', 'Sem despesas para mostrar')
        else:
            node = expenses.get_first()

            while node is not None:
                data: Expense = node.get_data()

                self.tabela.insert("", "end",text=data.get_id(),values=      
                    (data.get_category().get_name(), 
                      data.get_description(), 
                      f"{str(data.get_value())}€",
                     str(datetime.fromtimestamp(data.get_timestamp()))))
                node = node.get_node()
        lista_ordernar_asc = [(self.tabela.set(dados, coluna), dados) for dados in self.tabela.get_children('')]
        lista_ordernar_asc.sort(key=lambda x: x[0])

        # Reorganizar as linhas na Treeview
        for index, (value, dados) in enumerate(lista_ordernar_asc):
            self.tabela.move(dados, "", index)
        self.tabela.heading(coluna, command=lambda: self.tabela_header_click_desc(coluna))

    def tabela_header_click_desc(self, coluna):
        # Obter os dados da Treeview
        lista_ordernar_desc = [(self.tabela.set(dados, coluna), dados) for dados in self.tabela.get_children("")]

        # Classificar os dados em ordem reversa com base na coluna selecionada
        lista_ordernar_desc.sort(key=lambda x: x[0], reverse=True)

        # Reorganizar as linhas na Treeview
        for index, (value, dados) in enumerate(lista_ordernar_desc):
            self.tabela.move(dados, "", index)

        self.tabela.heading(coluna, command=lambda: self.tabela_header_click_normal(coluna))

    def tabela_header_click_normal(self, coluna):
        self.filtrar()
        # Alternar a direção da classificação ao clicar novamente no header
        self.tabela.heading(coluna, command=lambda: self.tabela_header_click_asc(coluna))

class AtualizarSaldoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Atualizar Saldo")
        self.filters = {}
        self.master.resizable(False, False)
        self.controller = Controller(modal)

        self.saldo = tk.Label(self, text="Saldo").grid(row=2, column=0, sticky='w')
        self.saldo = ttk.Entry(self)
        self.saldo.grid(row=2, column=0, sticky='s')

        self.butao_filtrar = tk.Button(self, text="Atualizar", command=self.atualizar)
        self.butao_filtrar.grid(row=3, column=0)

        self.retroceder = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(SessionFrame)).grid(
            column=0, row=4, sticky='s')

    def atualizar(self):
        saldo = self.saldo.get()
        if saldo.isnumeric():
            self.controller.get_modal().get_current_user().set_balance(int(saldo))
            showinfo('Sucesso', 'Saldo Atualizado com sucesso')
        else:
            showerror('Erro', 'Saldo Inválido')


class AtualizarSaldoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Atualizar Saldo")
        self.filters = {}
        self.master.resizable(False, False)
        self.controller = Controller(modal)

        self.saldo = tk.Label(self, text="Atualizar Saldo:").grid(row=2, column=0, sticky='w')
        self.saldo = ttk.Entry(self)
        self.saldo.grid(row=2, column=1, sticky='e')

        self.saldo_atualizar = tk.Button(self, text="Atualizar", command=self.atualizar)
        self.saldo_atualizar.grid(row=2, column=3)

        self.limite = tk.Label(self, text="Limite Mensal:").grid(row=4, column=0, sticky='w')
        self.limite_mensal = ttk.Entry(self)
        self.limite_mensal.grid(row=4, column=1, sticky='e')

        self.saldo_atualizar = tk.Button(self, text="Adicionar Limite", command=self.limite_mensal())
        self.saldo_atualizar.grid(row=4, column=3)

        self.retroceder = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(SessionFrame)).grid(
            column=1, row=6, sticky='s')

    def atualizar(self):
        saldo = self.saldo.get()
        if saldo.isnumeric():
            self.controller.get_modal().get_current_user().set_balance(int(saldo))
            showinfo('Sucesso', 'Saldo Atualizado com sucesso')
        else:
            showerror('Erro', 'Saldo Inválido')
>>>>>>> Stashed changes

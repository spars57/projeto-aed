import calendar
import re
import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkinter.messagebox import *

from tkcalendar import Calendar, DateEntry

from classes.Expense import Expense
from controller.Controller import Controller
from modal.Modal import Modal

modal = Modal()
controller = Controller(modal)

TABLE_ROWS = []


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
        self.controller = Controller(modal)

        self.controller.get_modal().load_to_json()

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
                                      fg="#17223b", width=15,
                                      command=self.f_login)
        self.login_button.grid(row=4, column=1)

        self.create_button = tk.Button(self, text="Criar Utilizador", font=("Comic Sans MS", 12), bg="#6b778d",
                                       width=15,
                                       fg="#17223b",
                                       command=lambda: self.master.switch_frame(RegisterFrame))
        self.create_button.grid(row=5, column=1)

        self.exit = tk.Button(self, text="Sair", font=("Comic Sans MS", 10), bg="#6b778d", fg="#17223b", width=15,
                              command=lambda: self.f_sair())
        self.exit.grid(row=5, column=0)

    def f_sair(self):
        modal.save_to_json()
        self.master.destroy()

    def f_login(self):
        user = self.user_entry.get()
        password = self.password_entry.get()

        if not user != '' and not password != '':
            showerror('Error', 'Campos Vazios')
            return

        response = self.controller.login(user, password)

        if response:
            self.master.switch_frame(SessionFrame)
            global nome_user
            nome_user = user
        else:
            showerror('Error', 'Login Falhou')


class RegisterFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#17223b")
        self.master.title('Criar Utilizador')
        self.master.resizable(False, False)
        self.verificar_numb = (self.register(self.f_verficar_nif))
        self.verificar_espaco = (self.register(self.f_verficar_espac))
        self.user_controller = Controller(modal)

        self.create_user_label = tk.Label(self, text="Username:", font=("Comic Sans MS", 14), bg="#17223b",
                                          fg="#ffa200")
        self.create_user_label.grid(row=0, column=0)
        self.create_user_entry = tk.Entry(self, font=(18), bg="#6b778d", fg="#17223b", validate='all',
                                          validatecommand=(self.verificar_espaco, '%P'))
        self.create_user_entry.grid(row=0, column=1)

        self.create_nif_label = tk.Label(self, text="NIF:", font=("Comic Sans MS", 14), bg="#17223b", fg="#ffa200")
        self.create_nif_label.grid(row=1, column=0)
        self.create_nif_entry = tk.Entry(self, font=(18), bg="#6b778d", fg="#17223b", validate='all',
                                         validatecommand=(self.verificar_numb, '%P'))
        self.create_nif_entry.grid(row=1, column=1)

        self.create_password_label = tk.Label(self, text="Password:", font=("Comic Sans MS", 14), bg="#17223b",
                                              fg="#ffa200")
        self.create_password_label.grid(row=2, column=0)
        self.create_password_entry = tk.Entry(self, show="*", font=(18), bg="#6b778d", fg="#17223b", validate='all',
                                              validatecommand=(self.verificar_espaco, '%P'))
        self.create_password_entry.grid(row=2, column=1)

        self.rep_password_label = tk.Label(self, text="Repeat Password:", font=("Comic Sans MS", 14), bg="#17223b",
                                           fg="#ffa200")
        self.rep_password_label.grid(row=3, column=0)
        self.rep_password_entry = tk.Entry(self, show="*", font=(18), bg="#6b778d", fg="#17223b", validate='all',
                                           validatecommand=(self.verificar_espaco, '%P'))
        self.rep_password_entry.grid(row=3, column=1)

        self.register_button = tk.Button(self, text="Registar Utilizador", font=("Comic Sans MS", 12), bg="#6b778d",
                                         fg="#17223b", command=lambda: self.f_registar())
        self.register_button.grid(row=4, column=1)

        self.voltar_button = tk.Button(self, text="Voltar", font=("Comic Sans MS", 10), bg="#6b778d", fg="#17223b",
                                       command=lambda: master.switch_frame(MainFrame))
        self.voltar_button.grid(row=4, column=0)

    def f_registar(self):
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
    def f_verficar_nif(self, digito):
        if str.isdigit(digito) and len(digito) <= 9:

            return True
        else:
            return False

    def f_verficar_espac(self, P):
        if re.search(r"^\w*$", P):  # O re é o RegEx basicamente o que faz é ver se a string contém X padrão
            # O \W é equivalente a [^a-zA-Z0-9] o *$ basicamente é para que corra na string toda inves de so no 1º char
            return True
        else:
            return False


class SessionFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#17223b")
        self.master.title("Sessão")
        self.master.resizable(False, False)

        self.label = tk.Label(self, text="Bem Vindo ", font=("Comic Sans MS", 14), bg="#17223b",
                              fg="#ffa200")
        self.label.pack()

        self.criar = tk.Button(self, text="Criar Despesa", font=("Comic Sans MS", 12), bg="#6b778d", width=15,
                               fg="#17223b", command=lambda: master.switch_frame(CreateDFrame))
        self.criar.pack()

        self.ver = tk.Button(self, text="Criar Categoria", font=("Comic Sans MS", 12), bg="#6b778d", width=15,
                             fg="#17223b", command=lambda: master.switch_frame(CriarCategoria))
        self.ver.pack()

        self.ver = tk.Button(self, text="Visualizar Despesa", font=("Comic Sans MS", 12), bg="#6b778d", width=15,
                             fg="#17223b", command=lambda: master.switch_frame(VerDFrame))
        self.ver.pack()

        self.ver = tk.Button(self, text="Atualizar Saldo", font=("Comic Sans MS", 12), bg="#6b778d", width=15,
                             fg="#17223b", command=lambda: master.switch_frame(AtualizarSaldoFrame))
        self.ver.pack()

        self.ver = tk.Button(self, text="Atualizar Limite", font=("Comic Sans MS", 12), bg="#6b778d", width=15,
                             fg="#17223b", command=lambda: master.switch_frame(AtualizarLimite))
        self.ver.pack()

        self.retroceder = tk.Button(self, text="Terminar Sessão", font=("Comic Sans MS", 12), bg="#6b778d", width=15,
                                    fg="#17223b", command=lambda: master.switch_frame(MainFrame))
        self.retroceder.pack()


class CreateDFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#17223b")
        self.user_controller = Controller(modal)
        self.master.title("Criar Despesa")
        self.master.resizable(False, False)
        self.verificar_numero = (self.register(f_verificar_numero))
        self.selected_date = None

        self.categoria_label = tk.Label(self, text="Categoria*:", font=("Comic Sans MS", 14), bg="#17223b",
                                        fg="#ffa200")
        self.categoria_label.grid(row=0, column=0)
        self.categoria_combo = ttk.Combobox(self, values=self.user_controller.get_all_category_names(),
                                            state='readonly')
        self.categoria_combo.current(0)
        self.categoria_combo.grid(row=0, column=1)

        self.valor_label = tk.Label(self, text="Valor*:", font=("Comic Sans MS", 14), bg="#17223b", fg="#ffa200")
        self.valor_label.grid(row=1, column=0)
        self.valor_entry = tk.Entry(self, validate='key', bg="#6b778d", fg="#17223b",
                                    validatecommand=(self.verificar_numero, '%P'))
        self.valor_entry.grid(row=1, column=1)

        self.data_label = tk.Label(self, text="Data*:", font=("Comic Sans MS", 14), bg="#17223b", fg="#ffa200")
        self.data_label.grid(row=2, column=0)
        self.calendar = Calendar(self, bg="#6b778d", fg="#17223b", selectmode='day', date_pattern='yyyy-mm-dd')
        self.calendar.grid(row=2, column=1)

        self.descricao_label = tk.Label(self, text="Descrição:", font=("Comic Sans MS", 14), bg="#17223b",
                                        fg="#ffa200")
        self.descricao_label.grid(row=3, column=0)
        self.descricao_entry = tk.Text(self, bg="#6b778d", fg="#17223b", width=30, height=5)
        self.descricao_entry.grid(row=3, column=1)

        self.registar = tk.Button(self, text="Registar Despesa", font=("Comic Sans MS", 12), bg="#6b778d",
                                  fg="#17223b", command=self.f_criar_despesa)
        self.registar.grid(row=4, column=1)

        self.retroceder = tk.Button(self, text="Voltar", font=("Comic Sans MS", 12), bg="#6b778d",
                                    fg="#17223b", command=lambda: master.switch_frame(SessionFrame))
        self.retroceder.grid(row=4, column=0)

    def f_criar_despesa(self):
        categoria = self.categoria_combo.get()
        valor = self.valor_entry.get()
        data = self.calendar.get_date()

        if categoria == '' or valor == '' or data == '':
            showerror('Error', 'Um dos campos que preencheu está vazio')
            return

        data = data.split("-")

        data = datetime(int(data[0]), int(data[1]), int(data[2]))
        data = calendar.timegm(data.timetuple())

        descricao = self.descricao_entry.get("1.0", "end").strip()

        categoria = self.user_controller.get_modal().get_category_list().get_category_by_name(categoria)
        valor = float(valor)

        retorno = self.user_controller.create_expense(categoria, valor, int(data), descricao)

        if retorno.startswith("Operação"):
            showinfo('Sucesso', 'Despesa Criada')
        else:
            showerror('Error', retorno)


class VerDFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#17223b")
        self.master.title("Ver Despesa")
        self.filters = {}
        self.master.resizable(False, False)
        self.controller = Controller(modal)
        self.verificar_numero = (self.register(f_verificar_numero))

        self.cor_tabela = ttk.Style(self)
        self.cor_tabela.configure("Treeview.Heading", background="#6b778d", foreground="#17223b",
                                  font=("Comic Sans MS", 10))
        self.cor_tabela.configure("Treeview", background="#6b778d", foreground="#17223b", font=("Comic Sans MS", 10))
        self.tabela = ttk.Treeview(self, columns=["category", "description", "value", "timestamp"],
                                   show='headings', selectmode='browse', style="Treeview")

        self.tabela.heading("category", text="Category", command=lambda: self.f_tabela_header_click_asc("category"))
        self.tabela.heading("description", text="Description",
                            command=lambda: self.f_tabela_header_click_asc("description"))
        self.tabela.heading("value", text="Value", command=lambda: self.f_tabela_header_click_asc("value"))
        self.tabela.heading("timestamp", text="Date", command=lambda: self.f_tabela_header_click_asc("timestamp"))

        self.f_preencher_tabela()

        self.tabela.grid(row=0, column=0, columnspan=2)

        self.categoria_label = tk.Label(self, text="Categoria:", font=("Comic Sans MS", 14), bg="#17223b",
                                        fg="#ffa200").grid(row=1, column=0, sticky='w')
        self.categoria_filtrar = ttk.Combobox(self, values=self.controller.get_all_category_names(), state='readonly')
        self.categoria_filtrar.grid(row=1, column=0, sticky='s')

        self.value_min_label = tk.Label(self, text="Valor Mínimo:", font=("Comic Sans MS", 14), bg="#17223b",
                                        fg="#ffa200").grid(row=2, column=0, sticky='w')
        self.value_min = tk.Entry(self, bg="#6b778d", fg="#17223b", validate='key',
                                  validatecommand=(self.verificar_numero, '%P'))
        self.value_min.grid(row=2, column=0, sticky='s')

        self.value_max_label = tk.Label(self, text="Valor Máximo:", font=("Comic Sans MS", 14), bg="#17223b",
                                        fg="#ffa200").grid(row=3, column=0, sticky='w')
        self.value_max = tk.Entry(self, bg="#6b778d", fg="#17223b", validate='key',
                                  validatecommand=(self.verificar_numero, '%P'))
        self.value_max.grid(row=3, column=0, sticky='s')

        self.date_min_label = tk.Label(self, text="Data Minima:", font=("Comic Sans MS", 14), bg="#17223b",
                                       fg="#ffa200").grid(row=4, column=0, sticky='w')
        self.data_min = DateEntry(self, width=16, foreground="white", bd=2, dateformat=4, date_pattern='YYYY-MM-DD')
        self.data_min.grid(row=4, column=0)

        self.data_max_label = tk.Label(self, text="Data Maxima:", font=("Comic Sans MS", 14), bg="#17223b",
                                       fg="#ffa200").grid(row=5, column=0, sticky='w')
        self.data_max = DateEntry(self, width=16, foreground="white", bd=2, dateformat=4, date_pattern='YYYY-MM-DD')
        self.data_max.grid(row=5, column=0)

        self.f_reset()

        self.butao_filtrar = tk.Button(self, text="Filtrar", font=("Comic Sans MS", 12), bg="#6b778d",
                                       fg="#17223b", command=self.f_filtrar)
        self.butao_filtrar.grid(row=7, column=0, sticky='w')

        self.butao_reset = tk.Button(self, text="Reset", font=("Comic Sans MS", 12), bg="#6b778d",
                                     fg="#17223b", command=self.f_reset)
        self.butao_reset.grid(row=7, column=0)

        self.sugestao = tk.Label(self, font=("Comic Sans MS", 14), bg="#17223b",
                                 fg="#ffa200")
        self.sugestao.grid(row=4, column=1)

        self.butao_sugestao = tk.Button(self, text="Sugestão Financeira", font=("Comic Sans MS", 12), bg="#6b778d",
                                        fg="#17223b", command=self.f_sugestao)
        self.butao_sugestao.grid(row=7, column=1)

        self.retroceder = tk.Button(self, text="Voltar", font=("Comic Sans MS", 12), bg="#6b778d",
                                    fg="#17223b", command=lambda: master.switch_frame(SessionFrame)).grid(
            column=0, row=8, sticky='e')

    def f_reset(self):
        self.f_preencher_tabela()
        self.categoria_filtrar.set('')
        self.value_min.delete(0, 'end')
        self.value_max.delete(0, 'end')
        self.data_max.delete(0, 'end')
        self.data_min.delete(0, 'end')

    def f_sugestao(self):
        lista = self.controller.get_suggestions()

        if lista is None:
            showerror('Error', 'Sem sugestões para mostrar')
        else:
            node = lista.get_first()
            while node is not None:
                category = node.get_data()
                node = node.get_node()
                self.sugestao.config(text='Sugestão: ' + category.get_name())

    def f_filtrar(self):
        category_name = self.categoria_filtrar.get() if self.categoria_filtrar.get() != "" else None
        category = self.controller.get_category_by_name(category_name)
        categories = []
        categories.append(category)
        value_minimum = int(self.value_min.get()) if self.value_min.get() != "" else None
        value_maximum = int(self.value_max.get()) if self.value_max.get() != "" else None

        if self.data_min.get_date() <= self.data_max.get_date() and (
                self.data_min.get_date() is not None or self.data_max.get_date() is not None):
            date_minimum = self.data_min.get_date()
            date_maximum = self.data_max.get_date()

            date_minimum = calendar.timegm(date_minimum.timetuple())

            date_maximum = calendar.timegm(date_maximum.timetuple())
        else:
            date_minimum = None
            date_maximum = None

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
            for i in self.tabela.get_children():
                self.tabela.delete(i)

            node = expenses.get_first()

            while node is not None:
                data: Expense = node.get_data()

                self.tabela.insert("", "end", text=data.get_id(), values=
                (data.get_category().get_name(),
                 data.get_description(),
                 f"{str(data.get_value())}€",
                 str(datetime.fromtimestamp(data.get_timestamp()))))
                node = node.get_node()

    def f_preencher_tabela(self):

        expenses = self.controller.get_expenses_filtered(user=modal.get_current_user())

        if expenses is None:
            showerror('Error', 'Sem despesas para mostrar')
        else:
            for i in self.tabela.get_children():
                self.tabela.delete(i)

            node = expenses.get_first()

            while node is not None:
                data: Expense = node.get_data()

                self.tabela.insert("", "end", text=data.get_id(), values=
                (data.get_category().get_name(),
                 data.get_description(),
                 f"{str(data.get_value())}€",
                 str(datetime.fromtimestamp(data.get_timestamp()))))
                node = node.get_node()

    def f_tabela_header_click_asc(self, coluna):
        lista_ordernar_asc = [(self.tabela.set(dados, coluna), dados) for dados in self.tabela.get_children('')]

        if coluna == "value":
            lista_ordernar_asc = sorted(lista_ordernar_asc, key=lambda x: float(x[0].replace('€', '')))
        else:
            lista_ordernar_asc.sort(key=lambda x: x[0])

        for index, (value, dados) in enumerate(lista_ordernar_asc):
            self.tabela.move(dados, "", index)
        self.tabela.heading(coluna, command=lambda: self.f_tabela_header_click_desc(coluna))

    def f_tabela_header_click_desc(self, coluna):
        # Obter os dados da Treeview
        lista_ordernar_desc = [(self.tabela.set(dados, coluna), dados) for dados in self.tabela.get_children("")]

        # Classificar os dados em ordem reversa com base na coluna selecionada
        if coluna == "value":
            lista_ordernar_desc = sorted(lista_ordernar_desc, key=lambda x: float(x[0].replace('€', '')), reverse=True)
        else:
            lista_ordernar_desc.sort(key=lambda x: x[0], reverse=True)

        # Reorganizar as linhas na Treeview
        for index, (value, dados) in enumerate(lista_ordernar_desc):
            self.tabela.move(dados, "", index)
        # Alternar a direção da classificação ao clicar novamente no header
        self.tabela.heading(coluna, command=lambda: self.f_tabela_header_click_normal(coluna))

    def f_tabela_header_click_normal(self, coluna):
        self.f_filtrar()
        self.tabela.heading(coluna, command=lambda: self.f_tabela_header_click_asc(coluna))


class CriarCategoria(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Criar Categoria")

        self.master.resizable(False, False)
        self.controller = Controller(modal)

        self.category_label = tk.Label(self, text="Nome da Categoria").grid(row=2, column=0, sticky='w')
        self.category_entry = ttk.Entry(self, validate='key')
        self.category_entry.grid(row=2, column=1, sticky='e')

        self.button = tk.Button(self, text="Criar", command=lambda: self.create_category())
        self.button.grid(row=2, column=3)

        self.retroceder = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(SessionFrame)).grid(
            column=1, row=6, sticky='s')

    def create_category(self):
        res = self.controller.create_category(self.category_entry.get())
        print(res)
        showinfo("Info", res)


class AtualizarLimite(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Atualizar Saldo")
        self.verificar_numero = (self.register(self.verificar_numero))

        self.filters = {}
        self.master.resizable(False, False)
        self.controller = Controller(modal)

        self.saldo_label = tk.Label(self, text="Atualizar Limite:").grid(row=2, column=0, sticky='w')
        self.saldo_entry = ttk.Entry(self, validate='key', validatecommand=(self.verificar_numero, '%P'))
        self.saldo_entry.grid(row=2, column=1, sticky='e')

        self.balanco = tk.Label(self, text="Limite Atual:   " + str(
            self.controller.get_modal().get_current_user().get_limit()) + "€")
        self.balanco.grid(row=4, column=0, sticky='w')

        self.limite_btn = tk.Button(self, text="Salvar", command=lambda: self.salvar_limite())
        self.limite_btn.grid(row=2, column=3)

        self.retroceder = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(SessionFrame)).grid(
            column=1, row=6, sticky='s')

    def verificar_numero(self, valor):
        try:
            float(valor)
            return True
        except ValueError:
            return False

    def salvar_limite(self):
        self.controller.get_modal().get_current_user().set_limit(float(self.saldo_entry.get()))
        self.balanco.config(
            text="Limite Atual:   " + str(self.controller.get_modal().get_current_user().get_limit()) + "€")


class AtualizarSaldoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Atualizar Saldo")
        self.verificar_numero = (self.register(f_verificar_numero))

        self.filters = {}
        self.master.resizable(False, False)
        self.controller = Controller(modal)

        self.saldo_label = tk.Label(self, text="Atualizar Saldo:").grid(row=2, column=0, sticky='w')
        self.saldo_entry = ttk.Entry(self, validate='key', validatecommand=(self.verificar_numero, '%P'))
        self.saldo_entry.grid(row=2, column=1, sticky='e')

        self.saldo_add = tk.Button(self, text="Adicionar", command=lambda: self.f_balanco(1))
        self.saldo_add.grid(row=2, column=3)

        self.saldo_remove = tk.Button(self, text="Remover", command=lambda: self.f_balanco(2))
        self.saldo_remove.grid(row=3, column=3)

        self.balanco = tk.Label(self, text="Saldo Atual:   " + str(
            self.controller.get_modal().get_current_user().get_balance()) + "€")
        self.balanco.grid(row=4, column=0, sticky='w')

        self.retroceder = tk.Button(self, text="Voltar", command=lambda: master.switch_frame(SessionFrame)).grid(
            column=1, row=6, sticky='s')

    def f_balanco(self, numb):
        saldo = self.saldo_entry.get()
        if saldo.isnumeric():
            if numb == 1:
                self.controller.get_modal().get_current_user().set_balance(
                    self.controller.get_modal().get_current_user().get_balance() + int(saldo))
            else:
                self.controller.get_modal().get_current_user().set_balance(
                    self.controller.get_modal().get_current_user().get_balance() - int(saldo))

            self.balanco.config(
                text="Saldo Atual:   " + str(self.controller.get_modal().get_current_user().get_balance()) + "€")
            self.controller.get_modal().save_to_json()
        else:
            showerror('Erro', 'Saldo Inválido')


# Global Function para validar os campos numericos
def f_verificar_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

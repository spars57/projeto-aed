# Documentação Projeto AED

## Métodos do Controller

- Autenticação:


    login(username: str, password: str) -> bool

- Criação de novas classes:


    create_user(username: str, password: str, nif: int) -> User
    create_expense(user: User, category: Category, value: float, timestamp: int, description: str = ''')
    create_category(name: str) -> Category

- Adicionar às listas:

      add_user(user: User) -> bool
      add_category(category: Category) -> bool
      add_expense(expense: Expense) -> bool

- Filtragem de Despesas:

      Aviso: Todos os parametros desta função são opcionais 
      e os filtros são acumulaveis permitindo assim filtragens complexas com multiplas condições


      get_expenses_filtered(
                user: User = None,
                categories: list[Category] = None,
                timestamp_minimum: int = None,
                timestamp_maximum: int = None,
                value_order: str = None,
                value_minimum: int = None,
                value_maximum: int = None,
                description: str = None
        ) -> LinkedList | None

- Outros:

      validate_nif(nif: int) -> bool

#### Notas:

- Este símbolo "`->`" representa o que a função retorna.
- Este símbolo "`|`" representa a condição OR.


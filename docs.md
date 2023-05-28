# Documentação Projeto AED

## Métodos do Controller

Autenticação:

    login(username: str, password: str) -> bool

Criação de Classes:

    create_user(username: str, password: str, nif: int) -> User
    create_expense(user: User, category: Category, value: float, timestamp: int, description: str = "") -> Expense
    create_category(name: str) -> Category
    create_budget(name: str, user: User, category: Category, value: float, valid_from: float, valid_until: float) -> Budget

Adicionar coisas às respectivas listas:

    add_user(user: User) -> str
    add_category(category: Category) -> str
    add_expense(expense: Expense) -> str
    add_budget(budget: Budget) -> str

Filtragem de Despesas:

    Aviso: 
        Todos os parametros desta função são opcionais 
        Os filtros são acumulaveis permitem filtragens com multiplas condições em simultanêo


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

Gets:

    get_budget_by_user(user: User) -> LinkedList | None
    get_category_by_name(name: str) -> Category | None
    get_user_by_username(username: str) -> User | None
    get_user_by_id(user_id: uuid4) -> User | None

Outros:

    validate_nif(nif: int) -> bool


#### Notas:

- Este símbolo "`->`" representa o que a função retorna.
- Este símbolo "`|`" representa a condição OR.


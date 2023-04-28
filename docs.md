# Documentação Projeto AED

#### Estrutura das classes

- `User: { id: uuid4, username: string, password: string, NIF: string }`
- `Category: { id: uuid4, name: string }`
- `Expense: { id: uuid4, user: User, category: Category, description: string, value: float, timestamp: float }`

#### Nota: Todas estas classes têm getters e setters.

Para cada classe irá existir uma outra classe que servirá para armazenar uma lista de classes:

- `UserList:`
  - Adicionar Utilizador
  - Remover Utilizador
- `CategoryList`
  - Adicionar Categoria
  - Remover Categoria
- `ExpenseList`
  - Adicionar Despesa
  - Remover Despesa

Ambas as classes terão métodos para permitir a gestão da lista, isto é: adicionar, remover, procurar.

## LinkedList

Métodos:
  - `is_empty() -> bool`
  - `size() -> int`
  - `get_first() -> User | Category | Expense `  
  - `insert_first(element: User | Category | Expense) -> None`
  - `remove_first() -> None`

## LinkedListItem

Atributos:
  - `id: uuid4`
  - `value: any`
  - `next: LinkedListItem`

Métodos: Getters e Setters

## Controller
Métodos que irão existir ( esta lista deverá ser incrementada consoante a necessidade ):

- Autenticação
  - `login(username: str, password: str) -> bool`

- Criação de novas Classes:
  - `create_expense(user: User, category: Category, description: str, value: float, timestamp: float) -> Expense`
  - `create_user(username: str, password: str) -> User`
  - `create_category(name: str) -> Category`

- Adicionar à lista:
  - `add_expense(expense: Expense) -> bool`
  - `add_category(category: Category) -> bool`
  - `add_user(user: User) -> bool`

- Remover da lista
  - `remove_expense(expense: Expense) -> bool`
  - `remove_category(category: Category) -> bool`
  - `remove_user(user: User) -> bool`

- Gets:
  - Utilizadores: 
    - `get_user_by_id(id: float) -> User | None `
    - `get_user_by_username(username: str) -> User | None`
  - Despesas:
    - `get_expenses_by_user(user: User) -> LinkedList[Expense] | None`
    - `get_expense_by_user_and_timestamp_range(user: User, min: float, max: float) -> LinkedList[Expense] | None`
    - `get_expenses_by_user_and_category(user: User, category: Category) -> LinkedList[Expense] | None`
  - Categorias:
    - `get_category_by_name(name: str) -> Category | None`
    - `get_all_categories() -> LinkedList[Category]`
- Outros:
  - `encrypt_password(password: str) -> str`
  - `validate_nif(nif: int) -> bool`
  

#### Notas:
- O que vêm depois deste "`->`" simbolo é aquilo que a função vai retornar.
- Este símbolo "|" representa a condição OR.


# Documentação Projeto AED
<!-- 
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

Ambas as classes terão métodos para permitir a gestão da lista, isto é: adicionar, remover, procurar. -->

<!-- ## LinkedList

Métodos:
  - `is_empty() -> bool`
  - `size() -> int`
  - `get_first() -> LinkedList[User | Category | Expense] `  
  - `insert_first(element: LinkedList[User | Category | Expense]) -> None`
  - `remove_first() -> None`

## LinkedListItem

Atributos:
  - `id: uuid4`
  - `value: any`
  - `next: LinkedListItem`

Métodos: Getters e Setters -->

## Métodos do Controller
Métodos que irão existir ( esta lista deverá ser incrementada consoante a necessidade ):

- Autenticação
  - `login(username: str, password: str) -> bool`

- Criação de novas classes:
  - `create_user(username: str, password: str, nif: int) -> User`

- Adicionar às listas:
  - `add_user(user: User) -> bool`

- Outros:
  - `validate_nif(nif: int) -> bool`: 
  
#### Notas:
- O que vêm depois deste "`->`" simbolo é aquilo que a função vai retornar.
- Este símbolo "`|`" representa a condição OR.


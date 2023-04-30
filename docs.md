# Documentação Projeto AED

## Métodos do Controller
- Autenticação
  - `login(username: str, password: str) -> bool`

- Criação de novas classes:
  - `create_user(username: str, password: str, nif: int) -> User`

- Adicionar às listas:
  - `add_user(user: User) -> bool`

- Outros:
  - `validate_nif(nif: int) -> bool`
  
#### Notas:
- Este símbolo "`->`" representa o que a função retorna.
- Este símbolo "`|`" representa a condição OR.


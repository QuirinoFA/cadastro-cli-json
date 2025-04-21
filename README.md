# cadastro-cli-json

Este é um projeto simples em Python que permite:

- Cadastrar nome, idade e CPF de uma pessoa
- Validar CPF (estrutura e duplicidade no sistema)
- Atrelar um ID para elas
- Validar nome e idade antes de salvar
- Salvar as informações (nome, idade e ID) num arquivo '.txt' em formato JSON
- Listar as informações salvas no sistema
- Navegar pelo menu com comandos simples


## Requisitos

- Python 3.7 ou superior

## Como executar

```markdown
1. Clone este repositório (se ainda não o fez):

```bash
git clone https://github.com/seu-usuario/cadastro-cli-json.git
cd cadastro-cli-json

2. Execute o arquivo principal no terminal:

python Teste115.py

## Estrutura do projeto

cadastro-cli-json/
├── Teste115.py          # Arquivo principal com a lógica do menu
├── dados.txt            # Arquivo onde os dados em formato JSON são armazenados
├── README.md            # Documentação do projeto
├── tests/               # (Opcional) Pasta para testes automatizados com pytest

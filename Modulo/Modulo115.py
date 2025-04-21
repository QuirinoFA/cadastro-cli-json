import json

def cadastro(nome:str, idade:int) -> None:
    """
    -> Recebe do usuário um nome e uma idade. Cadastra num arquivo .txt no formato JSON
    as informações como ID, Nome e Idade. Caso o banco esteja cheio, (999 IDs) informa
    um erro ao usuário.
    :param nome: Nome da pessoa a ser cadastrada no banco.
    :param idade: Idade da pessoa que será cadastrada no banco.
    """
    try:
        with open('Módulo115.txt', mode='r', encoding='utf-8') as f:
            banco = json.load(f)
            if len(banco) < 999:
                banco.append({'ID':999-len(banco),'Nome':nome,'Idade':idade})
            else:
                print("BANCO CHEIO! Pessoa não cadastrada.")
                return
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        banco = [{
            'ID':999,
            'Nome':nome,
            'Idade':idade
        }]
    with open('Módulo115.txt', mode='w', encoding='utf-8') as f:
        json.dump(banco, f, ensure_ascii=False,allow_nan=False, indent=4)
    print('-' * 40)

def menu() -> None:
    """
    -> Apresenta as opções de comandos para o usuário.
    """
    print('+='*20)
    print(f'{"MENU DE SELEÇÃO":^40}')
    print('+='*20)
    print(f'{"CADASTRO":<8} - Para cadastrar uma pessoa')
    print(f'{"LISTA":<8} - Para ver todos os dados')
    print(f'{"MENU":<8} - Para rever as opções')
    print(f'{"SAIR":<8} - Para encerrar o programa')
    print('-'*40)

def listagem() -> None:
    """
    -> Faz a leitura do arquivo, convertendo em formato JSON, com a base
    de cadastro e chama a função PRINTER para mostrar as informações do
    banco de dados ao usuário.
    """
    try:
        with open('Módulo115.txt', mode='r', encoding='utf-8') as l:
            lista = json.load(l)
            printer(lista)
            print('-' * 40)
    except FileNotFoundError:
        print('ERRO! Arquivo não encontrado ou corrompido!')
        print('-' * 40)
    except json.decoder.JSONDecodeError:
        print('ERRO! Arquivo vazio!')
        print('-' * 40)
    except Exception as e:
        print(f'ERRO! Erro inexperado: {e}')
        print('-' * 40)

def printer(doc:list) -> None:
    """
    -> Recebe a base de dados com as pessoas salvas já em formato JSON
    e printa essas informações para o usuário.
    :param doc: Base de dados lida na forma de lista, onde cada elemento
    é um dicionário com as informações das pessoas
    """
    print('A base contém as seguintes informações:')
    print('-'*40)
    for d in doc:
        for chave, valor in d.items():
            print(f'| {chave} - {valor} ', end='')
        print('|')
    print('-'*40)
    print('Fim da listagem!')

def valida_nome() -> str:
    while True:
        input_nome = str(input('Digite o nome da pessoa: ')).strip()
        if input_nome == '':
            print('ERRO! Nome em branco! Digite um nome válido!')
        else:
            break
    return input_nome

def valida_idade() ->int:
    while True:
        try:
            input_idade = int(input('Digite a idade da pessoa: '))
            if input_idade < 0:
                print('Idade precisa ser um número inteiro positivo!')
            else:
                break
        except ValueError:
            print('ERRO! A idade precisa ser um valor inteiro positivo!')
        except Exception as e:
            print(f'ERRO! erro inexperado: {e}')
    return input_idade

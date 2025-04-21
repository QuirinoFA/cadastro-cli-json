import json

def cadastro(nome:str, idade:int, cpf:list) -> None:
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
                count = 0
                for valor in banco:
                    if valor['CPF'] == cpf:
                        count += 1
                if count == 0:
                    banco.append({'ID':999-len(banco),'Nome':nome,'Idade':idade, 'CPF':cpf})
                else:
                    print('ERRO! CPF já cadastrado no banco!')
            else:
                print("BANCO CHEIO! Pessoa não cadastrada.")
                return
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        banco = [{
            'ID':999,
            'Nome':nome,
            'Idade':idade,
            'CPF':cpf
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

def captura_cpf() -> list:
    """
    -> Recebe um CPF do usuário, checa se possuí tamanho adequado, ajustando caso
    possível e confere se possuí caracteres que invalidam o CPF. Retorna uma
    lista com os números ajustados do CPF pronto para a conferência de validade.
    return: Retorna uma lista com os números do CPF limpo como elementos.
    """
    while True:
        cpf_usuario = str(input('Digite o CPF da pessoa: ')).strip()
        cpf_usuario = cpf_usuario.replace('.', '')
        cpf_usuario = cpf_usuario.replace('-', '')
        if len(cpf_usuario) > 11:
            print('ERRO! CPF precisa ter apenas 11 caracteres!')
        elif len(cpf_usuario) < 11:
            while len(cpf_usuario) < 11:
                cpf_usuario = '0' + cpf_usuario
        try:
            if len(cpf_usuario) == 11:
                cpf_limpo = []
                for c in cpf_usuario:
                    cpf_limpo.append(int(c))
                return cpf_limpo
        except ValueError:
            print('ERRO! CPF só pode conter números!')
        except Exception as e:
            print(f'ERRO! Erro desconhecido {e}')

def valida_cpf () -> list:
    """
    -> Função recebe um cpf na forma de LISTA usando uma outra função para
    limpar a entrada do usuário e verifica se o cpf digitado é válido ou não.
    Para de pedir ao usuário após receber um cpf válido.
    return: Retorna um cpf válido para cadastro.
    """
    while True:
        cpf_l = captura_cpf()
        cpf_num_1 = [cpf_l[m] * int(n) for m, n in enumerate(range(10, 1, -1))]
        if (11 - (sum(cpf_num_1) % 11)) <= 1:
            num_1 = 0
        else:
            num_1 = (11 - (sum(cpf_num_1) % 11))
        if cpf_l[9] == num_1:
            cpf_num_2 = [cpf_l[m] * int(n) for m, n in enumerate(range(11, 1, -1))]
            if (11 - (sum(cpf_num_2) % 11)) <= 1:
                num_2 = 0
            else:
                num_2 = (11 - (sum(cpf_num_2) % 11))
            if cpf_l[10] == num_2:
                return cpf_l
            else:
                print('ERRO! CPF inválido! Digite um CPF válido!')
        else:
            print('ERRO! CPF inválido! Digite um CPF válido!')

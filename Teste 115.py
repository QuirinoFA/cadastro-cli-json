import Modulo

if __name__ == '__main__':
    Modulo.menu()
    while True:
        try:
            funcao = str(input('Digite a função que deseja realizar: ')).upper().strip()
            if funcao == 'MENU':
                Modulo.menu()
            elif funcao == 'LISTA':
                Modulo.listagem()
            elif funcao == 'CADASTRO':
                i_nome = Modulo.valida_nome()
                i_idade = Modulo.valida_idade()
                i_cpf = Modulo.valida_cpf()
                Modulo.cadastro(i_nome, i_idade, i_cpf)
            elif funcao == 'SAIR':
                break
            else:
                print('ERRO! Precisa digitar uma função válida!')
                print('-'*40)
        except ValueError:
            print('ERRO! Digite um nome válido!')
        except Exception as e:
            print(f'ERRO! Erro inexperado {e}')

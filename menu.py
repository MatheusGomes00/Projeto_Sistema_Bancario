import textwrap
from entities import PessoaFisica, ContaCorrente, Deposito, Saque, Historico

def menu():
    menu = '''\n
    =========MENU=========
    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [NC]\tNova conta
    [LC]\tListar contas
    [NU]\tNovo usuário
    [Q]\tSair
    ======================
    ==> '''
    return input(textwrap.dedent(menu)).upper()
    '''
        input: 'textwrap.dedent(menu)' remove espaços em branco à esquerda da string 'menu'
               '.upper()' torna toda a string recebida no 'input()' em letras maiúsculas
    '''

def escolha_menu(clientes, contas):
    while True:
        escolha = menu()
        match escolha:
            case 'D':
                Deposito.depositar(clientes)
            case 'S':  
                Saque.sacar(clientes)
            case 'E': 
                Historico.exibir_extrato(clientes)

            case 'NU':
                PessoaFisica.criar_cliente(clientes)

            case 'NC':
                numero_conta = len(contas) + 1
                ContaCorrente.criar_conta(numero_conta, clientes, contas)

            case 'LC':
                ContaCorrente.listar_contas(contas)

            case 'Q': 
                break   
            case None:
                print('\n\nOpção inválida, digite novamente.')

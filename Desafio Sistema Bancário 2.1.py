from abc import ABC, abstractmethod
import textwrap, sys
from datetime import datetime


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):
        saldo = self._saldo

        if valor > saldo:
            print("\n*** Operação falhou! Você não tem saldo suficiente ***")
            
        elif valor > 0:
            self._saldo -= valor
            print("\n*** Saque realizado com sucesso! ***")
            return True
        
        else:
            print("\n*** Operação falhou! O valor informado é inválido ***")
            
        return False
   
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n*** Depósito realizado com sucesso! ***")
        else:
            print("\n*** Operação falhou! O valor informado é invalido. ***")
            return False
        
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, 
                 limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
             transacoes if transacao["tipo"] == Saque.
             __name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n*** Operação falhou! O valor do saque excede o limite. ***")
            
        elif excedeu_saques:
            print("\*** Operação falhou! Número máximo de saques excedido. ***")
            
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self._agencia}
            C/C:\t{self._numero}
            Titular:\t{self._cliente.nome}
        """
    

class Historico:
    def __init__(self):
        self._transacoes = []  # alguma estrutura de dados para armazenar???

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now(tz=None).strftime
                ("%d-%m-%Y %H:%M:%S")
            }
        )


class Transacao(ABC):    
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        self.conta = Conta
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []  # alguma estrutura de dados para armazenar???
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        

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


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente numeros): ")
    cliente = filtrar_clientes(cpf, clientes)

    if cliente:
        print("\n*** Já existe cliente com esse CPF! ***")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nasciment (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    
    clientes.append(cliente)

    print("\n*** Cliente criado com sucesso! ***")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("\nInforme o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("\n*** Cliente não encontrado, fluxo de criação de conta encerrado! ***")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente,
                                     numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n*** Conta criada com sucesso! ***")


def recuperar_conta_cliente(cliente, numb):
    if not cliente.contas:
        print("\n*** Cliente não possui conta! ***")
        return
    
    n_conta = [conta for conta in cliente.contas if conta.numero == numb]
    return n_conta[0]
    # temos que criar um método
    # FIXME: não é permitido cliente escolher a conta
    # return cliente.contas[0]  # é retornado somente a primeira conta


def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if
                          cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def listar_contas(contas):
    if len(contas) == 0:
        print("*** Não existem contas criadas! ***")
    else:
        for conta in contas:
            print("=" * 80)
            print(textwrap.dedent(str(conta)))


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    n_conta = int(input("Informe o número da conta: "))
    cliente = filtrar_clientes(cpf, clientes)
    
    if not cliente:
        print("\n*** Cliente não encontrado! ***")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente, n_conta)
    if not conta: 
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    n_conta = int(input("Informe o número da conta: "))
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("\n*** Cliente não encontrado! ***")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente, n_conta)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("\nInforme o CPF do cliente: ")
    n_conta = int(input("Informe o número da conta: "))
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("\n*** Cliente não encontrado! ***")
        return

    conta = recuperar_conta_cliente(cliente, n_conta)
    if not conta:
        return
    
    print("\n===========EXTRATO===========")
    transacoes = conta.historico.transacoes

    extrato = ""

    if not transacoes:
        extrato = "\n*** Não foram realizadas movimentações ***"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\nR$ \
            {transacao['valor']:.2f}\n{transacao['data']}"

    print(extrato)
    print(f"\nSaldo:\nR$ {conta.saldo:.2f}")
    print("=============================")


def main():
    clientes = []
    contas = []
    while True:  
        option = menu()
        if option == 'D':  
            depositar(clientes)

        elif option == 'S':  
            sacar(clientes)

        elif option == 'E': 
            exibir_extrato(clientes)
        
        elif option == 'NU':
            criar_cliente(clientes)

        elif option == 'NC':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif option == 'LC':
            listar_contas(contas)

        elif option == 'Q': 
            break  
        
        else:
            print('\n\nOpção inválida, digite novamente.')

"""
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

"""


main()
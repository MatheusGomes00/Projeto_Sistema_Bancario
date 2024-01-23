from abc import ABC, abstractmethod
from entities.cliente import PessoaFisica
from entities.conta import Conta, ContaCorrente


class Transacao(ABC):    
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        self.conta = Conta
        pass

    @staticmethod
    @abstractmethod
    def realizar_transacao(self, conta, transacao):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @staticmethod
    def realizar_transacao(conta, transacao):
        transacao.registrar(conta)

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    
    @classmethod
    def depositar(cls, clientes):
        cpf = input("Informe o CPF do cliente: ")
        n_conta = int(input("Informe o número da conta: "))
        cliente = PessoaFisica.filtrar_clientes(cpf, clientes)
        if not cliente:
            print("\n*** Cliente não encontrado! ***")
            return
        conta = ContaCorrente.recuperar_conta_cliente(cliente, n_conta)
        if not conta: 
            return        

        valor = float(input("Informe o valor do depósito: "))
        transacao = cls(valor)

        cls.realizar_transacao(conta, transacao)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    @staticmethod
    def realizar_transacao(conta, transacao):
        transacao.registrar(conta)

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

    @classmethod
    def sacar(cls, clientes):
        cpf = input("Informe o CPF do cliente: ")
        n_conta = int(input("Informe o número da conta: "))
        cliente = PessoaFisica.filtrar_clientes(cpf, clientes)

        if not cliente:
            print("\n*** Cliente não encontrado! ***")
            return

        valor = float(input("Informe o valor do saque: "))
        transacao = cls(valor)

        conta = ContaCorrente.recuperar_conta_cliente(cliente, n_conta)
        if not conta:
            return
        
        cls.realizar_transacao(conta, transacao)

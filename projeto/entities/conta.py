import textwrap
from entities.historico import Historico
from entities.cliente import PessoaFisica
import importlib
'''A biblioteca 'importlib' é utilizada para evitar a importação circular. 

    Outra técnica para evitar importações circulares em Python é usar a função 
    importlib.import_module(). Essa função permite importar um módulo de forma 
    programática, passando seu nome como uma string. Isso pode ser útil em 
    situações em que você precisa importar um módulo, mas o módulo exato a ser 
    importado não é conhecido até o momento da execução.
    fonte: https://docs.kanaries.net/pt/topics/Python/python-circular-import
'''

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
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    def sacar(self, valor):
        saldo = self.saldo

        if valor > saldo:
            print("\n*** Operação falhou! Você não tem saldo suficiente ***")
            
        elif valor > 0:
            self.saldo -= valor
            print("\n*** Saque realizado com sucesso! ***")
            return True
        
        else:
            print("\n*** Operação falhou! O valor informado é inválido ***")
        
        return False
   
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("\n*** Depósito realizado com sucesso! ***")
            return True
        else:
            print("\n*** Operação falhou! O valor informado é invalido. ***")
            return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, 
                 limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        transacoes = importlib.import_module('.transacoes', package='entities')
        numero_saques = len(
            [transacao for transacao in self.historico.
             transacoes if transacao["tipo"] == transacoes.Saque.
             __name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n*** Operação falhou! O valor do saque excede o limite de R$500,00 ***")
            
        elif excedeu_saques:
            print("\n*** Operação falhou! Número máximo de saques excedido. \n3 saques já realizados, consulte o histórico. ***")
            
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self._agencia}
            C/C:\t{self._numero}
            Titular:\t{self._cliente.nome}
        """
    
    @classmethod
    def criar_conta(cls, numero_conta, clientes, contas):
        cpf = input("\nInforme o CPF do cliente: ")
        cliente = PessoaFisica.filtrar_clientes(cpf, clientes)

        if not cliente:
            print("\n*** Cliente não encontrado, fluxo de criação de conta encerrado! ***")
            return
        else:
            conta = cls.nova_conta(numero=numero_conta, cliente=cliente)
            contas.append(conta)
            cliente.adicionar_conta(conta)

            print("\n*** Conta criada com sucesso! ***")

    @staticmethod
    def listar_contas(contas):
        if len(contas) == 0:
            print("*** Não existem contas criadas! ***")
        else:
            for conta in contas:
                print("=" * 80)
                print(textwrap.dedent(str(conta)))

    @staticmethod
    def recuperar_conta_cliente(cliente, numero_conta):
        if not cliente.contas:
            print("\n*** Cliente não possui conta! ***")
            return
        conta_cliente = [conta for conta in cliente.contas if conta.numero == numero_conta]
        return conta_cliente[0]
        # temos que criar um método
        # FIXME: não é permitido cliente escolher a conta
        # return cliente.contas[0]  é retornado somente a primeira conta



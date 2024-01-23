from datetime import datetime
from entities.cliente import PessoaFisica
import importlib

class Historico:
    def __init__(self):
        self._transacoes = []  # alguma estrutura de dados para armazenar???

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now(tz=None).strftime
                ("%d-%m-%Y %H:%M:%S")
            }
        )


    def exibir_extrato(clientes):
        cpf = input("\nInforme o CPF do cliente: ")
        n_conta = int(input("Informe o número da conta: "))
        cliente = PessoaFisica.filtrar_clientes(cpf, clientes)

        if not cliente:
            print("\n*** Cliente não encontrado! ***")
            return
        
        recuperar = importlib.import_module('.conta', package='entities')
        conta = recuperar.ContaCorrente.recuperar_conta_cliente(cliente, n_conta)
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

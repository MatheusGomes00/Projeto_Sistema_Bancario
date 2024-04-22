from entities.verifica_CPF import validar


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
        
    @property
    def contas(self):
        return self._contas


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        '''
            construtor que instancia um novo cliente com os atributos nome, data_nascimento, cpf e endereço
            a função embutida 'super()' é usada como exemplo, onde chama o atributo 'endereço' da classe pai/mãe
        '''
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

    @property
    def nome(self):
        return self._nome
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @property
    def cpf(self):
        return self._cpf

    def __str__(self):
        return {'nome': self.nome, 
                'data_nascimento': self.data_nascimento,
                'cpf': self.cpf}

    @classmethod
    def criar_cliente(cls, clientes):
        # cpf = input("Informe o CPF (somente numeros): ")
        cpf = validar()
        cliente = cls.filtrar_clientes(cpf, clientes)

        if cliente:
            print("\n*** Já existe cliente com esse CPF! ***")
            return
        else:
            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nasciment (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (logradouro-nro-bairro-cidade-sigla estado): ")

            cliente = cls(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
            
            clientes.append(cliente)

            print("\n*** Cliente criado com sucesso! ***")

    @staticmethod
    def filtrar_clientes(cpf, clientes):
        cliente_filtrado = [cliente for cliente in clientes if
                            cliente.cpf == cpf]
        return cliente_filtrado[0] if cliente_filtrado else None

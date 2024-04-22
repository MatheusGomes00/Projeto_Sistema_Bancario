def recebe_cpf():
    while True:
        cpf = input("Digite o CPF: ")
        if len(cpf) == 11 and cpf.isdigit():
            """
            A função isdigit é uma função embutida na linguagem de programação 
            Python que verifica se uma determinada cadeia de caracteres (string) 
            contém apenas dígitos numéricos
            """
            return cpf
        else:
            print("CPF é composto de 11 números inteiros. Digite novamente.")

def verifica_cpf(cpf):
    primeiro_digito_verificador = verificador_1(cpf)
    segundo_digito_verificador = verificador_2(cpf, primeiro_digito_verificador)
    if primeiro_digito_verificador == int(cpf[9]) and segundo_digito_verificador == int(cpf[10]):
        print("CPF válido.")
        return cpf
    else:
        print("CPF inválido.")
        return None
    

def soma_da_multiplicacao(cpf, indice_maior, indice_menor, soma=0):
    for i in cpf:
        soma += int(i) * indice_maior
        indice_maior -= 1
        if indice_maior < indice_menor:
            break
    return soma

def verificador_1(cpf):
    soma = soma_da_multiplicacao(cpf, indice_maior=10, indice_menor=2)
    resto = calcula_resto(soma)
    verificador_1 = verifica_resto(resto)
    return verificador_1

def verificador_2(cpf, verificador_1, soma=0, cont=11):
    soma = soma_da_multiplicacao(cpf, cont, indice_menor=3)
    soma += verificador_1 * 2
    resto = calcula_resto(soma)
    verificador_2 = verifica_resto(resto)
    return verificador_2

def calcula_resto(soma, base=11):
    return soma % base

def verifica_resto(resto, base=11):
    return 0 if resto == 0 or resto == 1 else base - resto

def validar():
    while True:
        entrada = recebe_cpf()
        cpf = verifica_cpf(entrada)
        if cpf == None:
            continue
        else:
            return cpf
        

if __name__ == "__main__":
    validar()

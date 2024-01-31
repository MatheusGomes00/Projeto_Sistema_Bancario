"""
Validador de CPF

O número do CPF é composto de 11 dígitos, sendo os dois últimos os dígitos de verificação, que têm por objetivo 
verificar se o CPF é válido. A fórmula para verificar a validade do CPF é explicada a seguir:
➢ 1º Dígito Verificador
Primeiro calcula-se a soma da multiplicação dos 9 primeiros dígitos por 10, 9, 8, ... , 3, 2, respectivamente. 
Em seguida obtém-se o resto da divisão deste número por 11 (Resto = Soma mod 11).
Agora se analisa o Resto:
Se Resto for igual a 1 ou a 0, então o 1º dígito verificador é 0.
Caso contrário, o 1º dígito verificador é o resultado da subtração de Resto de 11, ou seja, 11-Resto.
➢ 2º Dígito Verificador
Primeiro calcula-se a soma da multiplicação dos 9 primeiros dígitos por 11, 10, 9, ... , 4, 3, respectivamente 
e do 1º dígito verificador por 2.
O resto é semelhante ao que foi feito anteriormente (Resto = Soma mod 11)
E a análise do Resto:
Se Resto for igual a 1 ou a 0, então o 2º dígito verificador é 0.
Caso contrário, o 2º dígito verificador é o resultado da subtração de Resto de 11.


"""
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
    else:
        print("CPF inválido.")

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
    soma = soma_da_multiplicacao(cpf, indice_maior=11, indice_menor=3)
    soma += verificador_1 * 2
    resto = calcula_resto(soma)
    verificador_2 = verifica_resto(resto)
    return verificador_2

def calcula_resto(soma, base=11):
    return soma % base

def verifica_resto(resto, base=11):
    return 0 if resto == 0 or resto == 1 else base - resto

def main():
    cpf = recebe_cpf()
    verifica_cpf(cpf)

if __name__ == "__main__":
    main()

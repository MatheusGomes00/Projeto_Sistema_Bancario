"""
Validador de CPF

Sim, existem várias APIs externas que podem ser usadas para verificar a 
validade de um CPF. Aqui estão algumas delas:

1. **API Brasil**¹: Esta API permite que desenvolvedores acessem dados 
cadastrais de uma Pessoa Física e verifiquem sua situação fiscal junto 
à Receita Federal. Tudo isso é feito utilizando o número de CPF e a 
Data de Nascimento do indivíduo¹.

2. **API Invertexto**²: Esta API valida documentos como CPF e retorna 
um JSON com verdadeiro ou falso².

3. **NFE.io**⁵: Esta API permite a consulta de CPFs da Receita Federal. 
Ao passar o CPF e a data de nascimento da pessoa para a NFE.io, a API 
enviará esses dados para o governo, pegará as respostas e devolverá 
essas informações de uma forma padronizada e com garantia 
de confiabilidade⁵.

4. **Datavalid**⁴: Esta é uma solução digital para validação 
de identidade que é um serviço de qualificação cadastral de pessoas 
físicas e jurídicas, por meio de ferramenta (API) de inteligência⁴.

Por favor, note que o uso dessas APIs pode exigir a aceitação 
de termos de serviço, o pagamento de taxas, e/ou a obtenção 
de permissões ou licenças. Além disso, você deve garantir que o uso 
dessas APIs esteja em conformidade com todas as leis e 
regulamentos aplicáveis, incluindo, mas não se limitando a, 
leis de privacidade e proteção de dados. Espero que isso ajude! 
Se você tiver mais perguntas sobre Python ou qualquer outra coisa, 
fique à vontade para perguntar.

Origem: conversa com o Bing, 30/01/2024

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

def verificador_1(cpf, soma=0, cont=10):
    for i in cpf:
        soma += int(i) * cont
        cont -= 1
        if cont < 2:
            break
    resto = calcula_resto(soma)
    verificador_1 = verifica_resto(resto)
    return verificador_1

def verificador_2(cpf, verificador_1, soma=0, cont=11):
    for i in cpf:
        soma += int(i) * cont
        cont -= 1
        if cont < 3:
            break

    soma += verificador_1 * 2
    
    resto = calcula_resto(soma)
    verificador_2 = verifica_resto(resto)
    return verificador_2

def calcula_resto(soma, base=11):
    return soma % base

def verifica_resto(resto, base=11):
    if resto == 0 or resto == 1:
        return 0
    else:
        return base - resto


def main():
    cpf = recebe_cpf()
    verifica_cpf(cpf)

if __name__ == "__main__":
    main()

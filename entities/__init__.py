from .cliente import PessoaFisica
from .conta import ContaCorrente
from .transacoes import Deposito, Saque
from .historico import Historico

__all__ = ['PessoaFisica', 'ContaCorrente', 'Deposito', 'Saque', 'Historico']
'''
O atributo __all__ é uma lista que define a interface pública de um módulo Python. 
Ele especifica quais nomes devem ser importados quando um cliente importa um módulo 
usando a sintaxe from module import *. Gerenciando cuidadosamente o atributo __all__, 
você pode controlar quais partes de um módulo são expostas aos clientes, o que pode 
ajudar a evitar importações circulares.
fonte: https://docs.kanaries.net/pt/topics/Python/python-circular-import
'''

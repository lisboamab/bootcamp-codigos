"""
Exercício 7:

Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os elementos desta lista para inteiro.

Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, converta todos os elementos para int.
"""

lista = ["1", "7", "99", "15"]

lista_int = []
lista_str = []

print(f"Lista original: {lista}")

for x in lista:
    lista_int.append(int(x))

print(f"Lista com elementos convertidos para 'int': {lista_int}\n")

print(f"E agora convertendo novamente para 'str': ")

for y in lista_int:
    lista_str.append(str(y))

print(lista_str)
"""
Exercício 3:

Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições. Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser
 O maior elemento é 8 e está na posição 3
 O menor elemento é 3 e está na posição 4

Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição.

"""

lista = [10, 5, -24, 18, 78, 1]

maior_numero = max(lista)

menor_numero = min(lista)

print(f"O maior número da lista é {maior_numero} e a sua posição é {lista.index(maior_numero)}")

print(f"O menor número da lista é {menor_numero} e a sua posição é {lista.index(menor_numero)}")
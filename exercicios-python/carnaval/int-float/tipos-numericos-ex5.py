"""
Exercício 5:
Escreva um programa que leia do usuário um número de 4 dígitos e imprima a soma destes dígitos. 
Exemplo, se o usuário digitar 3141 seu programa deverá imprimir na tela 3+1+4+1=9.
"""

digitos = input("Digite uma sequencia de 4 números: ")

soma = int(digitos[0]) + int(digitos[1]) + int(digitos[2]) + int(digitos[3])

print(f"A soma de {digitos[0]} + {digitos[1]} + {digitos[2]} + {digitos[3]} = {soma}")
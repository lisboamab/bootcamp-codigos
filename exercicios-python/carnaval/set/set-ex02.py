"""
Exercício 2:

Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado. Exemplo:

 Digite um estado: SP
 O nome completo do estado é São Paulo.

"""

estados_siglas = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "CE": "Ceará", "MA": "Maranhão", "PE": "Pernambuco", "BA": "Bahia", "SC": "Santa Catarina"}

seu_estado = estados_siglas[input("Digite a sigla do seu estado: ")]

print(f"\nO nome do seu estado é: {seu_estado}\n")
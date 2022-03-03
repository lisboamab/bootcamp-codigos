"""
Exercício 6:

Faça um programa que remova strings vazias de uma lista de strings. Exemplo: dada a lista [“Olá”, “”, “meu”, “nome”, “”, “é”, “facilitador”, “”] a saída deve ser
 [“Olá”, “meu”, “nome”, “é”, “facilitador”]

"""

palavras = ["Olá", "meu", "", "nome", "", "é", "Marcos", ":D", "e", "", "eu", "acho", "python", "incrivel", ""]

for espaco in palavras:
    if espaco == "":
        palavras.pop(palavras.index(""))

print(palavras)
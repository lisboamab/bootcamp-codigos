"""
Exercício 4:

Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. Exemplo: dada o dicionário
>> {1: “vermelho”, 2: “azul”, 3: “marrom”}
A saída deverá ser
>> {1: 8, 2: 4, 3: 6}

"""
cores = {1: "vermelho", 2: "azul", 3: "marrom"}

#reescreve o dicionario com o len(), comprimento, da string relacionada com a key
for i in cores:
    cores[i] = len(cores[i])

print(cores)
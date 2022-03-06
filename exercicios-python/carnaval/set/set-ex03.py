"""
Exercício 3:

Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário
>> {“matemática”: 81, “física”: 83, “química”: 87} 
a saída deve ser 
>> {“química”: 87, “física”: 83, matemática”: 81}

"""
#dicionario = {"matemática": 81, "física": 83, "química": 87} 

#notas_ordenadas = {}

notas_desordenadas = {'matemática': 81, 'física': 83, 'química': 87} 

print(notas_desordenadas)

notas_ordenadas = dict(sorted(notas_desordenadas.items(), key=lambda nota: nota[1], reverse=True))

print(notas_ordenadas)


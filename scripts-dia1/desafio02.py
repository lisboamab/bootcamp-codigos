"""
How Bootcamps - Stone - /código[s]
Data: 15/02/2022
Autor: Henrique Junqueira Branco
Enunciado: O programa recebe o usuario a quantidade de km percorridos e o numero de dias que o cliente ficou com o carro, depois com precos ja estabelecidos nas variaveis 'preco_por_dia' e
'preco_por_km' o script multiplica as variaveis que receberam input 'qtd_km' e 'qtd_dias' respectivamente por 'preco_por_km' e 'preco_por_dia'. 'preco_total_km' e 'preco_total_dia'
recebem essa multiplicao e sao somadas posteriormente na variavel 'preco_a_pagar'. O usuario ao final tem impresso na sua tela o preco total a pagar.
"""

# Desafio 02: o que esse pequeno trecho de código faz?

qtd_km = int(input("Digite a quantidade de quilometros percorridos: "))

qtd_dias = int(input("Digite quantos dias você ficou com o carro:"))

preco_por_dia = 60
preco_por_km = 0.15

preco_total_km = qtd_km * preco_por_km
preco_total_dia = qtd_dias * preco_por_dia

preco_a_pagar = preco_total_km + preco_total_dia

print(f"Total a pagar: R$ {preco_a_pagar:7.2f}")

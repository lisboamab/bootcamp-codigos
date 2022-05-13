#  2 - extra, considerando um array que tenha os valores das vendas feitas por um vendedor durante o dia, imprima o valor da total da comissão do vendedor e se o vendedor bateu a meta.
#  O código deve funcionar pra qualquer array de vendas que siga o exemplo abaixo:

#  let vendas = [100, 40.3, 51.4 , 200, 49.9, 30]


#  * A comissão do vendedor é 5% em cima de cada venda;
#  * A meta do vendedor é de 150 reais de comissão por dia;

vendas = [100, 40.3, 51.4 , 200, 49.9, 30]
comissao = []

for i in vendas:
    comissaoUnitaria = i * 0.05
    print(f"A comissão é de R$ {comissaoUnitaria}")
    comissao.append(comissaoUnitaria)

comissaoTotal = 0
for i in comissao:
    comissaoTotal = comissaoTotal + i

print(f"Valor da comissão {comissaoTotal:2.2f}")

# comissaoTotal = sum(comissao)
# if comissaoTotal < 150:
#     print(f"A sua comissão total é de {comissaoTotal:2.2f}\n Você não bateu a meta")
    
# else:
#     print(f"A sua comissão total é de {comissaoTotal:2.2f}\n Parabéns!!! Você bateu a meta!")

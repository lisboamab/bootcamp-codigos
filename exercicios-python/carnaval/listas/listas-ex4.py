"""
Exercício 4:

Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: Exemplo de saída:
 Meses com temperatura acima da média anual de 35,5°:
 1 – janeiro
 3 – março
 6 – junho

"""



lista_temp = []

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

for mes in meses:
    lista_temp.append(float(input(f"Digite a temperatura para o mês de {mes}: "))) # o metodo append Recebe as temperaturas e adiciona ao final da lista


temp_media = (sum(lista_temp)/len(lista_temp))

print(f"A temperatura média do ano foi de: {temp_media:.1f}°C")

for temp in lista_temp: #
    if temp > temp_media:
        print(f"{temp} - {meses[lista_temp.index(temp)]}") #Aqui foi utilizado o metodo index para capturar a posição repectiva da temperatura e exibir o mês correspondente.


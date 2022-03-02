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
# ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

lista_temp = []

lista_temp.append(float(input("Digite a temperatura para o mês de janeiro: "))) #Recebe as temperaturas e adiciona ao final da lista
lista_temp.append(float(input("Digite a temperatura para o mês de fevereiro: ")))
lista_temp.append(float(input("Digite a temperatura para o mês de março: ")))
lista_temp.append(float(input("Digite a temperatura para o mês de abril: ")))
lista_temp.append(float(input("Digite a temperatura para o mês de maio: ")))
lista_temp.append(float(input("Digite a temperatura para o mês de junho: ")))
lista_temp.append(float(input("Digite a temperatura para o mês de julho: ")))
lista_temp.append(float(input("Digite a temperatura para o mês de agosto: ")))
lista_temp.append(float(input("Digite a temperatura para o mês de setembro: ")))
lista_temp.append(float(input("Digite a temperatura para o mês de outubro: ")))
lista_temp.append(float(input("Digite a temperatura para o mês de novembro: ")))
lista_temp.append(float(input("Digite a temperatura para o mês de dezembro: ")))

temp_media = (sum(lista_temp)/len(lista_temp))

print(f"A temperatura média do ano foi de: {temp_media}°C")
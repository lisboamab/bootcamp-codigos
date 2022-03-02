#Exercicio 4
#Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o Índice de Massa Corporal (IMC) do usuário.

peso = float(input("Olá! Vamos calcular o seu Indice de Massa Corporal (IMC)\nPrimeiro digite seu peso em kg: "))

altura = float(input("Digite a sua altura, use ponto para dividir os metros de centimetros: "))

imc = peso/(altura**2)

print(f"Seu IMC é de {imc:.2f}kg/m²")

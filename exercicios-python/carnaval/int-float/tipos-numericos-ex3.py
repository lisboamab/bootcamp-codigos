"""
Exercício 3:

No exercício acima você calculou a área de um triângulo a partir da sua base e altura. 
Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área. 
Compare a resposta com o exercício acima, dada das mesmas entradas. 
Os resultados devem ser idênticos.

"""

variavelA = float(input("Digite, em centimetros, os três lados do triângulo: "))
variavelB = float(input())
variavelC = float(input())

soma = (variavelA + variavelB + variavelC)/2

area = ((soma*(soma-variavelA)*(soma-variavelB)*(soma-variavelC))**(1/2))

print(f"A área do triangulo em centimetros é de : {area:.2f}")

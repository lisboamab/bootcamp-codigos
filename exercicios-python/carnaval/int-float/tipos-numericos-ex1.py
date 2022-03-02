"""
Exercício 1:

Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
•	A soma de A e B;
•	A diferença quando se subtrai B de A;
•	O produto (multiplicação) entre A e B;
•	O quociente (parte inteira da divisão) quando se divide A por B;
•	O resto da divisão entre A e B;
•	O resultado de log10 de A;
•	O resultado de A elevado a B;
"""

from math import log10

variavelA = float(input("Digite o valor A: "))

variavelB = float(input("Digite o valor B: "))

somaab = variavelA + variavelA

subtracaoab = variavelA - variavelB

multiplicaab = variavelA * variavelB

divideab = variavelA // variavelB

restoab = variavelA % variavelB

potenciaab = variavelA ** variavelB

print(f"Soma de {variavelA} e {variavelB}: {somaab}\n")
print(f"Diferença quando se subtrai {variavelB} de {variavelA} é de: {subtracaoab}\n")
print(f"Produto da multiplicação e {variavelA} e {variavelB}: {multiplicaab}\n")
print(f"Quociente, inteiro, da divisão de {variavelA} por {variavelB}: {divideab}\n")
print(f"Resto da divisão {variavelA} por {variavelB}: {restoab}\n")
print(f"Logaritimo de {variavelA}: {log10(variavelA)}")
print(f"Resultado de {variavelA} elevado a {variavelB}: {potenciaab}")
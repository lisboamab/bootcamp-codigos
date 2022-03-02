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
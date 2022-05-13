from operator import index


intervalos = ([0, 25], [25, 50], [50, 75], [75, 100])
numero = 1
print("Caso você queira sair, basta apertar -1")

while numero != -1:
    numero = float(input("Olá, coloque aqui seu número e vou dizer em qual intervalo você se enquanda "))

    if numero >= intervalos[0][0] and numero <= intervalos[0][1]:
        print (f"O seu numero é {numero} e ele está contido no intervalo de {intervalos[0][0]} a {intervalos[0][1]}")
    elif numero > intervalos[1][0] and numero <= intervalos[1][1]:
        print (f"O seu numero é {numero} e ele está contido no intervalo de {intervalos[1][0]} a {intervalos[1][1]}")
    elif numero > intervalos[2][0] and numero <= intervalos[2][1]:
        print (f"O seu numero é {numero} e ele está contido no intervalo de {intervalos[2][0]} a {intervalos[2][1]}")
    elif numero > intervalos[3][0] and numero <= intervalos[3][1]:
        print (f"O seu numero é {numero} e ele está contido no intervalo de {intervalos[3][0]} a {intervalos[3][1]}")
    elif numero == -1:
        print("Encerrando programa!")
    else:
        print("Número fora de intervalo, por favor tente novamente")
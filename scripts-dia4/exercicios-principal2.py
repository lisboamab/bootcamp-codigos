#Exercicio do dia 4 do bootcamp codigo[s]

aluno = input("Qual é o nome do aluno?")

notas = []

notas.append(float(input("Digite a primeira nota: ")))

notas.append(float(input("Digite a primeira segunda: ")))

notas.append(float(input("Digite a primeira terceira: ")))


media = sum(notas) / len(notas)
nota_minima_rec = 6
nota_minima_apr = 7

if media >= nota_minima_apr:
    status = "aprovado"
elif media >= nota_minima_rec:
    #Qual é a nota minima?
    nota_minima = min(notas)

    #Qual é o indice (posição) da nota mínima na lista?
    nota_minima_indice = notas.index(nota_minima)

    #Remove a nota mínima a partir da sua posição
    notas.pop(nota_minima_indice)

    #Recalcula a média
    media_recalculada = sum(notas) / len(notas)

    if media_recalculada >= nota_minima_apr:
        status = f"aprovado com {len(notas)} notas"
    else:
        status = "reprovado"

media_final = round(media_recalculada, 2)

print (f"\nA média do aluno {aluno} é {media_final} e o mesmo está {status} ")

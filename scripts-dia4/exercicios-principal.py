#Exercicio do dia 4 do bootcamp codigo[s]

aluno = input("Qual é o nome do aluno?")

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunta nota: "))

nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
nota_minima_rec = 6
nota_minima_apr = 7

if media >= nota_minima_apr:
    status = "aprovado"
elif media >= nota_minima_rec:
    status = "recuperação"
    print(f"\nAluno está de {status}\n")
    nota_rec = float(input("Digite a nota da Recuperação: "))
    mediafinal = (nota_rec + media) / 2

if mediafinal >= 7:
    status = "aprovado recuperação"
else:
    status = "reprovado"

media_final = round(media, 2)

print (f"\nA média do aluno {aluno} é {media_final} e o mesmo está {status} ")

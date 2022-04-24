fechamento = dict()

numero_alunos = int(input("Digite o número de alunos: "))
numero_notas = int(input("Digite o número de notas: "))

for _ in range(numero_alunos):
    nome = input("Digite o nome do aluno ")

    for _ in range(numero_notas):

        nota = int(input(f"Difite a nota do {nome}: "))

        fechamento[nome].append(nota)

for aluno, notas in fechamento.items():
    media = sum(notas)/len(notas)
    print(f"A média do aluno {aluno} foi {media}!")
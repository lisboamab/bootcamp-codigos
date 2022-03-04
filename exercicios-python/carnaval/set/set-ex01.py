"""
Exercício 1:

Digamos que existam 2 cursos de idiomas em uma escola, inglês e francês, e que existam alunos matriculados conforme abaixo:
•	Alunos matriculados em inglês:
o	João Alves dos Santos
o	Maria Magalhães
o	Antônio da Silva Ferreira
o	José Júnior Jarbas
o	Henrique da Silva Sauro
o	Joaquina Ferreira da Silva
o	Fabiana Aparecida Bianco
o	Marrone Gutierres
o	Carlos Magno Farad
o	Antônio da Silva Júnior Amaral

•	Alunos matriculados em francês:
o	João Alves dos Santos
o	Antônio da Silva Ferreira
o	Fernanda Abdala Mohamed
o	Abner Mignon Alib
o	Alisson Figueiredo
o	Henrique da Silva Sauro
o	Maria Magalhães
o	Marrone Gutierres
o	Joaquina Ferreira da Silva

Faça um programa que responda as seguintes perguntas:

"""
alunos_ingles = ["João Alves dos Santos", "Maria Magalhães", "Antônio da Silva Ferreira", "José Júnior Jarbas", "Henrique da Silva Sauro", "Joaquina Ferreira da Silva", "Fabiana Aparecida Bianco", "Marrone Gutierres", "Carlos Magno Farad", "Antônio da Silva Júnior Amaral"]

alunos_frances = ["João Alves dos Santos", "Antônio da Silva Ferreira", "Fernanda Abdala Mohamed", "Abner Mignon Alib", "Alisson Figueiredo", "Henrique da Silva Sauro", "Maria Magalhães", "Marrone Gutierres", "Joaquina Ferreira da Silva"]

alunos_ambos = []

all_alunos = alunos_ingles + alunos_frances

conjunto_alunos = set(all_alunos) #função set, conjunto, não possui elementos repetidos

#1.	Quantos alunos estão matriculados na escola, no total?

print(f"{len(conjunto_alunos)} alunos\n") 

#2.	Quantos e quais estão matriculados APENAS em INGLES?

alunos_ingles_only = (set(alunos_ingles)) - (set(alunos_frances))

print(f"\nO numero de alunos que fazem apenas inglês é de: {len(alunos_ingles_only)}\nE são os seguintes:\n")

for i in alunos_ingles_only:
    print(i)

#3.	Quantos e quais estão matriculados APENAS em FRANCES?

alunos_frances_only = (set(alunos_frances)) - (set(alunos_ingles))

print(f"\nO numero de alunos que fazem apenas francês é de: {len(alunos_frances_only)}\nE são os seguintes:\n")

for i in alunos_frances_only:
    print(i)

#4.	Quantos e quais estão matriculados EM AMBOS os cursos?

for i in all_alunos:
    #Checa se o elemento do conjunto 'all_alunos' está presente na lista 'alunos_inglês' e se também está presente na 'alunos_frances'.
    #Se a condição for verdadeira, adciona o elemento na lista 'alunos_ambos'.
    if i in alunos_ingles and i in alunos_frances: 
        alunos_ambos.append(i)

print(f"\nO numero de alunos que fazem ambos os cursos é de: {len(set(alunos_ambos))}\nE são os seguintes:\n")

for i in set(alunos_ambos):
    print(i)

#5.	Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?

print(f"\n\nO número total de alunos que fazem apenas um curso é de: {(len(alunos_frances_only)) + (len(alunos_ingles_only))}")
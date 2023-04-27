qntAlunos = int(input("Quantidade de alunos:  "))
alunos = []

for x in range(qntAlunos):
    alunos.append(input("Digite o nome do aluno: "))
pesq = str(input("Pesquisar nome na lista: "))
for y in range(qntAlunos):
    if pesq == alunos[y]:
        print(y, alunos[y])
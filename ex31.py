qntAlunos = int(input("Quantidade de alunos:  "))
alunos = []

for x in range(qntAlunos):
    alunos.append(input("Digite o nome do aluno: "))

#outra forma de fazer Java
#for x in alunos:
    #print(x)

for y in range(qntAlunos):
    print(alunos[y],y)
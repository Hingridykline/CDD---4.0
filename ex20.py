soma= 0
i=1
quantAlunos = int(input("Digite a quantidade de alunos: "))

while i <= quantAlunos:
    notas = float(input("Digite a nota deles: "))
    soma+=notas
    i=i+1

media = soma/quantAlunos

print(media)
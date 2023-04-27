notaAlunos = []
soma = 0
cont = 0
for x in range(5):
    notaAlunos.append(float(input("Digite uma nota: ")))

for y in range(5):
    soma += notaAlunos[y]
media = soma/5

for i in range(5):
    if notaAlunos[i] >= media:
        cont+=1
print(cont)
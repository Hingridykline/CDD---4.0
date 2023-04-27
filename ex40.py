A = []
soma = 0
cont = 0
for x in range(5):
    A.append(int(input("Digite 5 valor: ")))


for y in range(5):
    if A[y] % 2 == 0:
        print(A[y],' ', end='')

for z in range(5):
    soma+= A[z]
media = soma/5

for w in range(5):
    if A[w] > media:
        cont+=1
print(cont)

menor = A[0]
maior = A[0]

for i in range(5):
    if A[i] < menor:
        menor=A[i]
    if A[i] > maior:
        maior = A[i]

print(menor)
print(maior)

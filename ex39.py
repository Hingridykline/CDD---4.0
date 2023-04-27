A = []
cont = 0
for x in range(10):
    A.append(int(input("Digite um número: ")))

B = int(input("Digite outro valor: "))

for y in range(10):
   if B == A[y]:
       cont+=1

print(f'O número {B} apareceu {cont} vezes ')

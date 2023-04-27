A = []
B = []
C = []

N = int(input("Digite o valor de N: "))

for x in range(N):
    A.append(int(input('Digite o Valor de A: ')))
    B.append(int(input('Digite o Valor de B: ')))

for y in range(N):
    C.append(A[y]+B[y])

print(A)
print(B)
print(C)
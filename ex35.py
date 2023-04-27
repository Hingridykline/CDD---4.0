lista = []
for x in range(5):
    lista.append(int(input("Digite um número: ")))
    #lista.sort(reverse=True)

for y in range(5):
    print(lista[y], end=' ')

print()
#primeira maneira
for c in range(5):
    print(lista[4-c], end=' ')

#segunda maneira
for h in range (4, -1,-1):
    print(lista[h], end=' ')


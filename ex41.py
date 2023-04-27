nomes = []

for x in range(5):
    nomes.append(input("Digite os nomes: "))
print(nomes, ' ', end='')
print('')

for y in range(4, -1, -1):
    print(nomes[y], ' ', end='')
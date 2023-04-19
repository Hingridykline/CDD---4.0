dentro=0
fora=0
for x in range(10):
    num = int(input("Digite 10 números: "))
    if num >= 10 and num <= 20:

        dentro=dentro+1
    else:
        fora=fora+1
print("Quantidade de números que estão dentro do intervalo de 10 a 20:", dentro)
print("Quantidade de números que NÃO estão dentro do intervalo de 10 a 20:", fora)


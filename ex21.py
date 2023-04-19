n1  = float(input("Digite um numero: "))
n2  = float(input("Digite outro numero: "))

while n2 == 0:
    n2 = float(input("Número inválido! Digite um valor diferente de zero: "))

resul = n1 / n2
print(resul)
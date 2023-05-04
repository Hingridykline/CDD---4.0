resp = 's'
while resp == 's':
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))

    if n1 == n2:
        print("Números iguais, digite números diferentes:")


    if n1 < n2:
        print(n1, n2)

    else:
        print(n2, n1)

    resp = input("Deseja recomeçar?")
    if resp != 's':
        print("Acabou")



operacao = 0

while operacao != 6:

    numero1 = float(input("Digite o primeiro número"))
    numero2 = float(input("Digite o segundo número"))

    operacao = int(input("Selecione a operaçao:"
                         "[1] soma "
                         "[2] sub"
                         "[3] mult"
                         "[4] div"
                         "[5] novo numero"
                         "[6] para sair "))

    if operacao == 1:
        print(numero1+numero2)

    elif operacao == 2:
        print(numero1-numero2)

    elif operacao == 3:
        print(numero1*numero2)

    elif operacao == 4:
        print(numero1/numero2)

    elif operacao == 5:
        continue

    elif operacao == 6:
        print('Fim do programa')

    else:
        print('Operação inválida, digite de 1 a 6')
        break

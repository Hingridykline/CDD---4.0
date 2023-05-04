pergunta = 0
invalido = 5

while invalido ==5:
    while pergunta !=4:

        pergunta = int(input("Digite [1] para calcular a área do triângulo e [2] para calcular a área do retângulo e [3] para sair do programa: "))

        if pergunta == 1:
            baseT = float(input("Digite o valor da base do triângulo: "))
            alturaT = float(input("Digite o valor da altura do triângulo: "))

            At = (baseT*alturaT)/2

            print(f'O valor da área do triangulo é:{At}')

        elif pergunta == 2:
            baseR = float(input("Digite o valor da base do retângulo: "))
            alturaR = float(input("Digite o valor da altura retângulo: "))

            Ar = baseR*alturaR

            print(f'O valor da área do retângulo é:{Ar}')

        elif pergunta == 3:
            print("Fim do programa!")

        else:
            invalido = int(input("Número inválido, digite 5 se deseja começar o programa novamente: "))
            if invalido != 5:
                print("Erro")
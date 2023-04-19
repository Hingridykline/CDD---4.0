novocalculo = 's'
while novocalculo == 's':

    nota1 = float(input("Digite a primeira nota: "))

    while nota1 <0 or nota1 > 10:
        nota1 = float(input("Nota inválida, digite novamente: "))

    nota2 = float(input("Digite a segunda nota: "))

    while nota2 <0 or nota2 > 10:
        nota2 = float(input("Nota inválida, digite novamente: "))

    media = (nota1+nota2)/2

    print("A média do aluno é: ", media)

    novocalculo = input("Deseja realizar novo cálculo?")


if novocalculo != 's':
    print("Obrigada")
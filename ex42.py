medias = []
continuar = 'sim'
while continuar == 'sim':

    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    media = (nota1+nota2)/2
    medias.append(media)
    print(media)

    if media >= 7:
        print("Aprovado")

    elif media >=4:
        print("Recuperação")

    else:
        print("Reprovado!")

    continuar = input("Deseja começar de novo? ")

print(medias)
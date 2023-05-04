horaI = int(input("Digite a hora de início: "))
horaF = int(input("Digite a hora do fim: "))
duracao = horaF-horaI

if horaI < horaF:
    print(duracao)
else:
    print(24-horaI+horaF)
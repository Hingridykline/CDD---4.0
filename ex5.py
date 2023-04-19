time1 = input("Primeiro time: ")
time2 = input("Segundo time: ")
golsTime1 = int(input("Gols marcados do primeiro time: "))
golsTime2 = int(input("Gols marcados do segundo time: "))

if golsTime1 != golsTime2:
    if golsTime1 > golsTime2:
        print(f" O {time1} venceu com {golsTime1} gols!")

    else:
        print(f" O {time2} venceu com {golsTime2} gols!")
else:
        print("Empate")

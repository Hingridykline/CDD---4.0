qntmaca = int(input("Digite a quantidade de maças compradas: "))
total1 = 1.30*qntmaca
total2 = 1*qntmaca

if qntmaca < 12:
    print(f"{total1:.2f}")
else:
    print(f'{total2:.2f}')
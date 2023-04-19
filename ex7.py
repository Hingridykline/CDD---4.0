number = int(input("Digite um número para saber se ele é ímpar ou par"))
if number == 0:
    print("Número neutro!")
elif number %2==0:
    print("Número par!")
else:
    print("Número impar!")
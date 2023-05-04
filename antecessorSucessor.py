numero = int(input("Digite um número: "))

if numero < 0:
    numero = numero + 1
    print(numero)

elif numero > 0:
    numero = numero - 1
    print(numero)

else:
    print("erro")


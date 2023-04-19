combustivel = input("Digite G para Gasolina e E para Etanol")
lt = float(input("Quantos litros?"))

if combustivel == "g" or combustivel == "e":
    if combustivel == "g":
        print(f"O valor é: ", lt*5.80)
    else:
        print("O valor a ser pago é: ", lt*4.90)
else:
    print("Inválido")

    
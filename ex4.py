numb1 = int(input("Numero 1: "))
numb2 = int(input("Numero 2: "))

if numb1 != numb2:
    if numb1 < numb2 :
        print(numb1,numb2)
    else:
        print(numb2,numb1)
else:
    print("Numeros iguais")

a = []
cont = 0
impar = 0
while True:
    if cont %2 !=0:
        a.append(cont)
        impar+=1
    if impar == 10:
        break
    cont+=1
print(a)

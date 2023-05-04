t_eleitores = int(input("Total de eleitores: "))
nulo = int(input("Digite os votos nulos: "))
branco = int(input("Digite os votos brancos: "))
validos = int(input("Digite os votos válidos: "))

porcentagemNulo = (nulo/t_eleitores)*100
porcentagemBranco = (branco*100)/t_eleitores
porcentagemValido = (validos*100)/t_eleitores

print(f'Porcentagem Nulos:{porcentagemNulo} Porcentagem Brancos:{porcentagemBranco} Porcentagem Válidos:{validos}')

if porcentagemValido + porcentagemBranco + porcentagemNulo > 100:
    print("Inválido!")

elif porcentagemValido + porcentagemBranco + porcentagemNulo < 100:
    print("Inválido")
else:
    print(porcentagemNulo)
    print(porcentagemValido)
    print(porcentagemBranco)
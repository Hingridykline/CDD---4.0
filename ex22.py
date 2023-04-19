senha = '12345'
cont = 1
senha1 = input("Digite sua senha: ")
while senha1 != senha:
    cont += 1
    senha1 = input("Senha errada! Digite novamente:")
    if senha1 == senha:
        print('Login efetuado com sucesso!')
        break
    if cont >=3:
        print("Senha bloqueada!")
        break
else:
    print('Login efetuado!')

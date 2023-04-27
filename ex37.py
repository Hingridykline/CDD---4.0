nome = []
senha = []

for x in range(1):
    nome.append(input("Cadastrar nome: "))
    senha.append(int(input("Cadastrar  senha: ")))
    novoNome = input("Digite o nome: ")
    novaSenha = int(input("Digite a senha: "))

for y in range(1):
    if nome[y] == novoNome and senha[y]  == novaSenha:
        print("Acesso liberado!")

    else:
        print("Nome ou senha incorreta! Tente novamente!")



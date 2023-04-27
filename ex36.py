nome = []
senha = []

for x in range(5):
    nome.append(input("Digite o nome: "))
    senha.append(int(input("Digite a senha")))

for y in range(5):
    print(f'Nome: {nome[y]} Senha: {senha[y]} Na posição: {y} ')
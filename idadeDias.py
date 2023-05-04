nome = input("Nome do usuário: ")
idade = int(input("Digite sua idade:  "))
meses = int(input("Meses: "))
dias = int(input("Dias: "))

idade = idade*365
meses = meses*30

print(f'{nome} tem {idade+meses+dias} dias de vida.')

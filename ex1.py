nome = input("Digite o nome do Usuário: ")
idade = input("Digite a idade: ")
salario = float(input("Digite o salário do usuário: "))
aumentop = float(input("Qual o percentual de aumento?"))

aumento = (salario*aumentop)/100

novoSalario = (salario+aumento)


print(f"Nome: {nome}\nIdade: {idade}\nAumento: {aumento}\nSalário: {novoSalario}")
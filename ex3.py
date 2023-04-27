nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1+nota2+nota3)/3
if media < 4 or media == 0:
    print("Aluno Reprovado!")
elif media >= 4 and media <=6:
    print("Aluno em recuperação!")
else:
    print("Aprovado!")
a = []
m = []
for i in range(10):
    a.append(int(input("Digite os numeros")))

x = int(input("Digite um novo numero: "))

for e in range(10):
    m.append(a[e]*x)
print(a)
print(x)
print(m)
n = int(input("Digite um número inteiro: "))

soma = 0
x = 1
y = 1

print("S = 1/1", end=' ')
soma += (x/y)

for i in range(1, n):
    x += 1
    y += 2
    soma += (x/y)

    print("+ {}/{}".format(x, y), end=' ')

print("= {:.2f}".format(soma))
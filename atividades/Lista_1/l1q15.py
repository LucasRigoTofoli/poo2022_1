n = int(input("Digite um número inteiro qualquer: "))
total = 1

print("{}! =".format(n), end=' ')
for i in range(n, 1, -1):
    total *= i
    print("{}*".format(i), end='')
print("1 = {}".format(total))


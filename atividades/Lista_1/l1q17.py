n = int(input("Digite um número inteiro: "))
ant1 = 1
ant2 = 0
if n == 1:
    termo = 1
else:
    for i in range(1, n):
        termo = ant1 + ant2
        ant2 = ant1
        ant1 = termo

print(termo)
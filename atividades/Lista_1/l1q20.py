num = input("Digite um número inteiro: ")

cont = 0

for i in range(5):
    if num[i] == num[4-i]:
        cont += 1

if cont == 5:
    print("Palíndromo")
else:
    print("Não é um palíndromo")
'''
n = int(input("Digite um número: "))
impar = 1
par = 0

for n in range(1, n+1, 1):
    if n%2 == 0:
        par = par + n
    else:
        impar = n * impar

print("par: ", par)
print("impar: ", impar)
'''
#----------------------------------------------------------
'''
maiornota = -1
menornota = 100000000
soma = 0
media = 0

for var in range(0, 5):
    nota = int(input("Digite a nota do aluno: "))
    soma = soma + nota

    if nota >= maiornota:
        maiornota = nota
    elif nota <= menornota:
        menornota = nota

media = soma/5
print("Média =", media, "- Maior Nota =", maiornota, "- Menor Nota =", menornota)
'''
#--------------------------------------------------------------
'''
i = 1
j = 1

for i in range(1, 11):
    for j in range(1, 11):
        print("{} * {} = {}".format(i, j, i*j))
    print("--------------")
'''
#--------------------------------------------------------------
'''
num = int(input("Digite um número: "))
count = 0

for i in range(num, 0, -1):
    if num%i == 0:
        count += 1

if count <= 2:
    print("primo!")
else:
    print("não é primo!")
'''
#--------------------------------------------------------------
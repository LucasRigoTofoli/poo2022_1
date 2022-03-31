"""
nome = 'Lucas Rigo Tofoli'

print('\nNome:', nome)
print('\n1ª letra:', nome[0])
print('\nTamnho:', len(nome))
#print('\nÚltimo caractere:', nome[len(nome)-1])
print('\nÚltimo caractere:', nome[-1])

#for c in nome:
    #print(c)

print('\n')
for i in range(len(nome)):
    print(nome[i])


nome = input("Digite seu nome:")
print(nome)

for i in range(len(nome)):
    print(nome[i], end=' ')

#ái oa
print("\nSubstring 1:", nome[:5])
print("\nSubstring 2:", nome[6:])
print("\nSubstring 3:", nome[3:15:2])

for i in range(len(nome)):
    print(ord(nome[i]), end=' ')
"""
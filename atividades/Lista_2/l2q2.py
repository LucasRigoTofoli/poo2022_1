texto = input("Digite uma mensagem para ser convertida: ")
aux = ''

for i in range(len(texto)):
    if texto[i] == 'a' or texto[i] == 'A':
        aux = aux + '4'
    elif texto[i] == 'b' or texto[i] == 'B':
        aux = aux + '8'
    elif texto[i] == 'e' or texto[i] == 'E':
        aux = aux + '3'
    elif texto[i] == 'o' or texto[i] == 'O':
        aux = aux + '0'
    elif texto[i] == 's' or texto[i] == 'S':
        aux = aux + '5'
    elif texto[i] == 't' or texto[i] == 'T':
        aux = aux + '7'
    else:
        aux = aux + texto[i]

print("A palavra convertida é:", aux)

cont = 0
perg1 = input("Telefonou para a vítima? (sim/nao)\n")
if perg1 == 'sim':
    cont += 1
perg2 = input("Esteve no local do crime? (sim/nao)\n")
if perg2 == 'sim':
    cont += 1
perg3 = input("Mora perto da vítima?? (sim/nao)\n")
if perg3 == 'sim':
    cont += 1
perg4 = input("Devia para a vítima? (sim/nao)\n")
if perg4 == 'sim':
    cont += 1
perg5 = input("Já trabalhou com a vítima? (sim/nao)\n")
if perg5 == 'sim':
    cont += 1

if cont >= 2:
    if cont > 2 and cont < 5:
        print("\nCúmplice")
    elif cont == 5:
        print("\nAssassino")
    else:
        print("\nSuspeita")
else:
    print("\nInocente")
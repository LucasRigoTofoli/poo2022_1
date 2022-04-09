n = int(input("Digite o valor inteiro em reais: "))

cem = n // 100
resto = n - (cem*100)

cinq = resto // 50
resto = resto - (cinq*50)

dez = resto // 10
resto = resto - (dez*10)

cinco = resto // 5
resto = resto - (cinco*5)

um = resto // 1

print("Serão:\n{} notas de cem\n{} notas de cinquenta\n{} notas de dez\n{} notas de cinco\n{} moedas de um".format(cem, cinq, dez, cinco, um))
#print("{}".format(resto))
dist = float(input("Qual a distância você deseja percorrer em km? "))

if dist <= 200:
    passagem = 0.50*dist
else:
    passagem = 0.45*dist

print("Valor da passagem = R${:.2f}".format(passagem))
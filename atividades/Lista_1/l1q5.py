peso = float(input("Digite quantos kkg foram pescados:"))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 5

    print("A pesca excedeu {:.2f} quilos e a multa será de R${:.2f}".format(excesso, multa))
else:
    print("Não excedeu o limite de 50kg!")

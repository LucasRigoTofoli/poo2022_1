valor = float(input("Valor do imóvel: "))
numparc = int(input("Número de parcelas: "))
salario = float(input("Salário: "))

prestacao = valor/numparc

if prestacao < (salario*0.30):
    print("Compra aprovada, o valor da prestação é de R${:.2f}".format(prestacao))
else:
    print("O valor da prestação é maior que 30% do salário, por isso a compra não pode ser feita.")

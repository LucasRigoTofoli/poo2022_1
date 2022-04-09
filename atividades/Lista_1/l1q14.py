quant = float(input("Digite a quantidade de kWh consumida: "))
tipo = input("Digite o tipo de instalação (R, C, I): ")

if tipo == 'R':
    if quant <= 500:
        total = quant*0.40
    else:
        total = quant*0.65
elif tipo == 'C':
    if quant <= 1000:
        total = quant*0.55
    else:
        total = quant*0.60
elif tipo == 'I':
    if quant <= 5000:
        total = quant*0.55
    else:
        total = quant*0.60

print("O valor total a ser pago ficou em R${:.2f}".format(total))
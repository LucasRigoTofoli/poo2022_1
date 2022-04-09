valorh = float(input("Digite o valor por hora recebido: "))
horas = float(input("Digite o número de horas trabalhadas: "))

salbruto = valorh*horas

salliq = salbruto - (salbruto*0.11 + salbruto*0.08 + salbruto*0.05)

print("Salário Bruto = R${:.2f} \nSalário Líquido = R${:.2f}".format(salbruto, salliq))
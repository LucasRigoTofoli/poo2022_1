total = 0
preco = float(input("Digite o preço do produto: "))

while(preco != 0):
    total += preco

    preco = float(input("Digite o preço do produto: "))

compra = input("Deseja pagar a vista ou no cartão?(vista/cartao) ")

if compra == 'vista':
    total = total*0.85
    print("O valor total ficou = R${:.2f}".format(total))
elif compra == 'cartao':
    parcela = total/4
    print("O total ficou em 4 parcelas de R${:.2f}".format(parcela))
else:
    print("Opção inválida!")


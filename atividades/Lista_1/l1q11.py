carne = input("Qual carne deseja comprar?(File/Alcatra/Picanha)\n")
kgs = float(input("Quantos quilos de {}?\n".format(carne)))
cartao = input("Irá pagar com o cartão do supermercado?(sim/nao)\n")

if carne == 'File' or carne == 'file':
    if kgs > 5:
        total = 15.80*kgs
    else:
        total = 14.90*kgs
elif carne == 'Alcatra' or carne == 'alcatra':
    if kgs > 5:
        total = 16.80*kgs
    else:
        total = 15.90*kgs
elif carne == 'Picanha' or carne == 'picanha':
    if kgs > 5:
        total = 17.80*kgs
    else:
        total = 16.90*kgs

if cartao == 'sim':
    total = total*0.95

print("\nValor total a pagar = R${:.2f}".format(total))
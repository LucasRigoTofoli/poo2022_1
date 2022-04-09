nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2)/2

if media >= 7:
    if media >= 9.5:
        print("Aprovado com Distinção")
    else:
        print("Aprovado")
else:
    print("Reprovado")

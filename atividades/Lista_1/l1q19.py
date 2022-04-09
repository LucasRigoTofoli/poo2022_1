from re import X


n = int(input("Número que deseja obter a raiz: "))
azero = float(input("Uma aproximação da raiz quadrada desse número: "))

x = azero**2 - n

if x < 0:
    x = -X

while x > 0.0001:
    azero = (azero + (n/azero)) / 2
    
    x = azero**2 -n

    if x < 0:
        x = -x

print("Raiz quadrada do número {} é = {}".format(n, azero))
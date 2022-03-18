from cmath import log10

"""
x = int(input('Informe um número: '))

y = x % 2

if y == 0:
    print('O número é par!')
else:
    print('O número é ímpar!')
"""

x = float(input('Informe x: '))
y = float(input('Informe y: '))
sinal = input('Informe a operação entre x e y: ')

if sinal == '+':
    result = x + y
    print('O resultado da + entre', x,'e', y,'é igual a', result)
elif sinal == '-':
    result = x-y
    print('O resultado da - entre', x,'e', y,'é igual a', result)
elif sinal == '*':
    result = x*y
    print('O resultado da * entre', x,'e', y,'é igual a', result)
    #print('{:.2f}'.format(x))
    #print(f'{x:.2f}')
elif sinal == '/':
    result = x/y
    print('O resultado da / entre', x,'e', y,'é igual a', result)

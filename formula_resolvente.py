import math

a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))
x1 = 0
x2 = 0
delta = (b ** 2 ) - (4 * a *c)

if delta < 0 :
    print('Esta equacao nao possui raizes reais.')
else:
    x1 = ((-b) + math.sqrt(delta)) / (2 * a)
    x2 = ((-b) - math.sqrt(delta)) / (2 * a)
    print(f'X1: {x1:.4f}')
    print(f'X2: {x2:.4f}')

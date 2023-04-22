print('Digite as tres distancias: ')

d1 = float(input())
d2 = float(input())
d3 = float(input())

if d1 > d2 and d1 > d3:
    print(f'MAIOR DISTANCIA = {d1}')
elif d2 > d3:
    print(f'MAIOR DISTANCIA = {d2}')
else:
    print(f'MAIOR DISTANCIA = {d3}')
    
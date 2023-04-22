numero_1 = float(input('Primeiro valor: '))
numero_2 = float(input('Segundo valor: '))
numero_3 = float(input('Tereiro valor: '))

menor: int

if numero_1 < numero_2  and numero_1 < numero_3:
    print(f'MENOR: {numero_1}')
elif numero_2 < numero_3:
    print(f'MENOR: {numero_2}')
else:
    print(f'MENOR: {numero_3}')

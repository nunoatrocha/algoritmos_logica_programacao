x = int(input('Quantos numeros voce vai digitar? '))

for i in range(x):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0 and numero > 0:
        print('PAR POSITIVO')
    elif numero % 2 == 0 and numero < 0:
        print('PAR NEGATIVO')
    elif numero % 2 != 0 and numero > 0:
        print('IMPAR POSITIVO')
    elif numero % 2 != 0 and numero < 0:
        print('IMPAR NEGATIVO')
    else:
        print('NULO')


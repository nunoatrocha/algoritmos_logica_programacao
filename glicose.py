glicose = float(input('Digite a medida da glicose: '))

if glicose <= 100:
    print(f'Classificacao: normal')
elif glicose <= 140:
    print(f'Classificacao: elevado')
else:
    print(f'Classificacao: diabetes')

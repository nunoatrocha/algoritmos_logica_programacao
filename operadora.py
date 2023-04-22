minutos_utilizados = int(input('Digite a quantidade de minutos: '))

minutos_plano_base = 100

if minutos_utilizados <= minutos_plano_base:
    print(f'Valor a pagar: 50 euros')
else:
    extra_minutos = minutos_utilizados - minutos_plano_base
    valor_extra = 2 * extra_minutos + 50
    print(f'Valor a pagar: {valor_extra}')


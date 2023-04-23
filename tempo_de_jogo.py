hora_inicial = int(input('Hora inicial: '))
hora_final = int(input('Hora inicial: '))

if hora_inicial < hora_final:
    horas_de_jogo = hora_final - hora_inicial
else:
    horas_de_jogo = (24 + hora_final) - hora_inicial

print(f'O JOGO DUROU = {horas_de_jogo}')


escolha = input('Voce vai digitar a temperatura em qual escala (C/F)?')
temperatura = float(input('Digite a temperatura em Fahrenheit: '))

if escolha == "F" or escolha == "f":
    c = (temperatura -32) * (5 / 9)
    print(f'Temperatura equivalente em Celsius: {c:.2f}')
elif escolha == "C" or escolha == "c":
    f = temperatura * 1.8 + 32
    print(f'Temperatura equivalente em Celsius: {f:.2f}')
else:
    print('Escolha uma opção válida.')


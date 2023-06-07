numeros = int(input('Quantos numeros voce vai digitar? '))
dentro = 0
fora = 0
for i in range(numeros):
    x = int(input('Digite um numero: '))
    if x >= 10 and x <=20:
        dentro += 1
    else:
        fora += 1

print(f'{dentro} Dentro')
print(f'{fora} Fora')

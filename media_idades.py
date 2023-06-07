idade = int(input('Digite as idades: '))
somatorio = 0
contador = 0

if idade < 0:
    print('IMPOSSIVEL CALCULAR')
else:
    while idade >= 0:
        somatorio += idade
        contador += 1
        idade = int(input())
    
    media = somatorio / contador
    print(f'MEDIA = {media:.2f}')
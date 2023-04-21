nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_final = nota_1 +  nota_2
print(f'NOTA FINAL = {nota_final:.1f}')
if nota_final < 60 :
    print('REPROVADO')

salario =  float(input('Digite o salario da pessoa: '))
novo_salario = 0

if salario <= 1000:
    novo_salario = (salario * 0.2) + salario
    print(f'Novo salario = {novo_salario:.2f}')
    print(f'Aumento = {(novo_salario - salario):.2f}')
    print(f'Porcentagem = 20%')
elif salario <= 3000:
    novo_salario = (salario * 0.15) + salario
    print(f'Novo salario = {novo_salario:.2f}')
    print(f'Aumento = {(novo_salario - salario):.2f}')
    print(f'Porcentagem = 15%')
elif salario <= 8000:
    novo_salario = (salario * 0.10) + salario
    print(f'Novo salario = {novo_salario:.2f}')
    print(f'Aumento = {(novo_salario - salario):.2f}')
    print(f'Porcentagem = 10%')
else:
    novo_salario = (salario * 0.05) + salario
    print(f'Novo salario = {novo_salario:.2f}')
    print(f'Aumento = {(novo_salario - salario):.2f}')
    print(f'Porcentagem = 5%')

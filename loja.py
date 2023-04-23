codigo_produto = input('Codigo do produto comprado: ')
quantidade_comprada = int(input('Quantidade comprada: '))
total_a_pagar = 0

if codigo_produto == "1":
    total_a_pagar = quantidade_comprada * 5
elif codigo_produto == "2":
    total_a_pagar = quantidade_comprada * 3.5
elif codigo_produto == "3":
    total_a_pagar = quantidade_comprada * 4.8
elif codigo_produto == "4":
    total_a_pagar = quantidade_comprada * 8.9
elif codigo_produto == "5":
    total_a_pagar = quantidade_comprada * 7.32

print(f'Valor a pagar: {total_a_pagar:.2f}')

preco_unitario = float(input('Preço unitário do produto: '))
quantidade_comprada = int(input('Quantidade comprada: '))
dinheiro_recebido =  float(input('Dinheiro recebido: '))

valor_a_pagar = preco_unitario * quantidade_comprada

if valor_a_pagar > dinheiro_recebido:
    print(f'DINHEIRO INSUFICIENTE. FALTAM {(valor_a_pagar - dinheiro_recebido):.2f} euros')
else:
    print(f'TROCO = {(dinheiro_recebido - valor_a_pagar):.2f}euros')
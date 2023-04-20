preco = float(input('Preço unitário do produto: '))
quantidade = int(input('Quantidade comprada: '))
dinheiro_recebido = float(input('Dinheiro recebido: '))

troco = dinheiro_recebido - (preco * quantidade)

print(f'TROCO = {troco:.2f}')

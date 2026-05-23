# Dado um conjunto contendo o número de itens vendidos em 20 dias de trabalho,
# deseja-se saber:
# - a quantidade total de itens vendidos
# - a media de vendas por dia
# - qual a maior quantidade de itens vendidos

vendas = [8, 12, 6, 14, 12, 8, 30, 45, 21, 8, 8, 12, 6, 14, 12, 8, 35, 23, 21, 8 ]

total_vendas = sum(vendas)

qtde_vendas = len(vendas)

media_vendas = total_vendas / qtde_vendas

maior = vendas[0] # assume que o primeiro dia foi o maior

for i in range(qtde_vendas):
    proximo = vendas[i]
    if( proximo > maior ):
        maior = proximo

print('Total de vendas', total_vendas)
print('Media de vendas', media_vendas)
print('A maior venda foi', maior)
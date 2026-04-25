# Escreva um programa que leia 4 números digitados pelo usuário
# e calcule a média destes números

soma = 0
for cont in range(1, 5):
    msg = 'Digite o '+ str(cont) +'º número: '
    numero = int(input(msg))
    soma += numero

media = soma / cont
print('média = ', media)
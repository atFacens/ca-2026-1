# Escreva um programa que leia vários números digitados pelo usuário
# e calcule a média destes números
# Antes de iniciar a leitura dos números pergunte ao usuário quantos números serão digitados

qtde = int(input('Quantos números serão digitados? '))

soma = 0
# for cont in range(1, qtde+1):
for cont in range(qtde):
    numero = int(input('Digite um número: '))
    soma += numero

media = soma / qtde
print('média = ', media)
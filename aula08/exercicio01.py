# Escreva um programa que leia vários números digitados pelo usuário
# e calcule a média destes números.
# A entrada de dados termina quando o usuário digitar 0 (zero)

numero = 1
soma = 0
cont = 0
while(numero != 0):
    numero = int(input('Digite um número(0 = final): '))
    if(numero != 0):
        soma += numero
        cont += 1

media = soma / cont
print('média = ', media)


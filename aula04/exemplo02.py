# Escreva um programa que leia um valor inteiro digitado pelo usuário
# e classifique esse número em: positivo, negativo e zero

entrada = input('Digite um valor inteiro:')
# print(entrada)
# print(type(entrada))

numero = int(entrada)

# print(numero + 5)
# print(type(numero))

if( numero > 0):
    print('Esse número é positivo')
else:
    if(numero < 0):
        print('Esse número é negativo')
    else:
        print('Esse número é zero')

# if(True):
#     print('')
# elif(True):
#     print('')
# elif(True):
#     print('')
# elif(True):
#     print('')
# elif(True):
#     print('')
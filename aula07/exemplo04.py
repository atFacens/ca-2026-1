soma = 0

cont = 1 
while(cont <= 3): 
    numero = int(input('Digite um número positivo: '))

    if(numero <= 0):
        soma -= numero
        # pass : serve para completar um local de instrução para poder executar, mas não faz nada
    else:
        soma += numero

    cont = cont + 1


print('soma =',soma)
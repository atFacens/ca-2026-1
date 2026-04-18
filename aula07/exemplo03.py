soma = 0

numero = 1
cont = 1 
while(cont <= 3 and numero > 0): 
    numero = int(input('Digite um número positivo: '))

    soma += numero

    cont = cont + 1


print('soma =',soma)
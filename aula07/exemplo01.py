# caso o usuário digite um valor inválido,
# interrompa a leitura dos valores

soma = 0

cont = 1 
while(cont <= 3): 
    numero = int(input('Digite um número positivo: '))
    if(numero <= 0):
        break # interrompe o laço "mais próximo"

    soma += numero

    cont = cont + 1


print('soma =',soma)
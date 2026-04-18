# caso o usuário digite um valor inválido,
# desconsidere esse número e continue a leitura

soma = 0

cont = 1 
while(cont <= 3): 
    numero = int(input('Digite um número positivo: '))
    if(numero <= 0):
        continue # volta para o início do laço

    soma += numero

    cont = cont + 1


print('soma =',soma)
matriz = [ 
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9] 
]

for linha in range(0, 3):
    print('linha:', linha, matriz[linha])
    for coluna in range(3):
        print('coluna:', coluna, matriz[linha][coluna], end=' ==> ')
        if(matriz[linha][coluna] % 2 == 0):
            print('Par')
        else:
            print('Impar')
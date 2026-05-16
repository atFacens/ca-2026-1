
numeros = [2, 5, 3, 8, 1, 9, 7]

print(numeros)

print('Primeiro:', numeros[0])
print('Segundo:', numeros[1])

print('Tamanho:', len(numeros))

numeros.append(10)

print(numeros)
print('Tamanho:', len(numeros))

valorProcurado = 8
for i in range(len(numeros)):
    if(numeros[i] == valorProcurado):
        print('achei o', valorProcurado,'no índice', i)
        break
    else:
        print('não achei')

# numeros[i] = 'X'
# print(numeros)
numeros.remove(valorProcurado)

numeros.sort()
print(numeros)
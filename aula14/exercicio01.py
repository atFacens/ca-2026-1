# Escreva uma função chamada calcular_media, que recebe três números 
# como parâmetros e retorna a média desses números. 
# Em seguida, escreva um código que chame essa função 
# com diferentes conjuntos de valores e exiba os resultados.

def calcular_media(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    return media


resposta = calcular_media(10, 20, 30)
print('A média entre 10, 20 e 30 é', resposta)

print(calcular_media(5, 10, 20))

# Crie uma função chamada estatisticas que recebe 
# uma lista de números e retorna um dicionário contendo a média, 
# o maior valor, o menor valor e a mediana dos números.

def estatisticas(lista):
    lista_ordenada = sorted(lista)
    print(lista_ordenada)
    # print('menor: ', lista_ordenada[0])
    # print('menor: ', min(lista))
    tamanho = len(lista)
    # print('maior: ', lista_ordenada[tamanho-1])
    # print('maior: ', max(lista))
    maior = max(lista)
    menor = min(lista)

    if(tamanho % 2 == 0):
        mediana = (lista_ordenada[tamanho // 2 -1] + lista_ordenada[tamanho // 2]) / 2
    else:
        mediana = lista_ordenada[tamanho // 2]

    dados = {
        "maior": maior,
        "menor": menor,
        "mediana": mediana
    }

    return dados
    

resultado = estatisticas([3, 7, 1, 9, 2, 10, 6])
print(resultado)
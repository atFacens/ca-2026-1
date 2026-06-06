def cabecalho(texto, simbolo):
    tam = len(texto)
    linha(tam, simbolo)
    print(texto)
    linha(tam, simbolo)


def linha(tamanho, caracter):
    for i in range(tamanho):
        print(caracter, end='')
    print()


cabecalho('Meu sistema v 1.0', '-')


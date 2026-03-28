
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

print('Operações: + - * /')
operacao = input('Qual operação vc quer fazer? ')


# if(operacao == '+')

match operacao:
    case '+': resultado = 'Resposta = ' + str(numero1 + numero2) 
    case '-': resultado = 'Resposta = ' + str(numero1 - numero2) 
    case '*': resultado = 'Resposta = ' + str(numero1 * numero2) 
    case '/': 
        if(numero2 == 0):
            resultado = "Divisão por zero!!!"
        else:
            resultado = 'Resposta = ' + str(numero1 / numero2) 
    case _: resultado = 'Operação desconhecida'

print(resultado)
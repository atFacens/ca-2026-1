dia_semana = 1

if(dia_semana == 1):
    print('Domingo')
else:
    if(dia_semana == 2):
        print('Segunda-feira')
    else:
        if(dia_semana == 3):
            print('Terça-feira')
        else:
            if(dia_semana == 4):
                print('Quarta-feira')
            else:
                if(dia_semana == 5):
                    print('Quinta-feira')
                else:
                    if(dia_semana == 6):
                        print('Sexta-feira')
                    else:
                        if(dia_semana == 7):
                            print('Sábado')
                        else:
                            print('Inválido')

if(dia_semana == 1):
    print('Domingo')
elif(dia_semana == 2):
    print('Segunda-feira')
elif(dia_semana == 3):
    print('Terça-feira')
elif(dia_semana == 4):
    print('Quarta-feira')
elif(dia_semana == 5):
    print('Quinta-feira')
elif(dia_semana == 6):
    print('Sexta-feira')
elif(dia_semana == 7):
    print('Sábado')
else:
    print('Inválido')

match dia_semana:
    case 1: 
        print('Hoje é')
        print('Domingo')
    case 2: print('Segunda-feira')
    case 3: print('Terça-feira')
    case 4: print('Quarta-feira')
    case 5: print('Quinta-feira')
    case 6: print('Sexta-feira')
    case 7: print('Sábado')
    case _: print('Inválido')



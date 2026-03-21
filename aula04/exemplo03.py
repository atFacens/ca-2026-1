
media = 4

if(media >= 7):
    print('Aprovado')
else:
    if( media >= 5):
        print('Exame')
    else:
        print('Reprovado')

if(media < 7):
    if(media >= 5):
        print('Exame')
    else:
        print('Reprovado')
else:
    print('Aprovado')
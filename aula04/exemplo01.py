
# para trocar uma lâmpada, preciso de uma lâmpada igual ou então semelhante

tenho_lampada_igual = True
tenho_lampada_similar = False

posso_trocar_lampada = tenho_lampada_igual or tenho_lampada_similar

print(posso_trocar_lampada)

# SE a resposta for verdadeira, mostra a mensagem de troca
# SENÃO (caso contrário), mostra a mensagem de impossível trocar

if( posso_trocar_lampada == True ):
    print('Você pode trocar a lâmpada')
    print('segundo comando do if')
else:
    print('Você Não pode trocar a lâmpada')
    print('segundo comando do else')

print('Fim do programa')
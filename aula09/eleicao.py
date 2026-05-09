candidato1 = 0
candidato2 = 0
candidato3 = 0
nulos = 0
brancos = 0

eleitores = int(input('Quantos eleitores terão?'))

for cont in range(0, eleitores):
    voto = int(input('Digite o seu voto: '))

    match voto:
        case 1: candidato1 += 1
        case 2: candidato2 += 1
        case 3: candidato3 += 1
        case 4: brancos += 1
        case _: nulos += 1

votos_validos = candidato1 + candidato2 + candidato3

print('______________________________________________________________________')
print('Candidato 1:', candidato1, " - ", (candidato1 / votos_validos) * 100, "%")
print('Candidato 2:', candidato2, " - ", (candidato2 / votos_validos) * 100, "%")
print('Candidato 3:', candidato3, " - ", (candidato3 / votos_validos) * 100, "%")
print('Votos em Branco:', brancos, " - ", (brancos / eleitores) * 100, "%")
print('Votos Nulos:', nulos, " - ", (nulos / eleitores) * 100, "%")
print('______________________________________________________________________')

vencedor = 0
if(candidato1 > candidato2 and candidato1 > candidato3):
    vencedor = 1
else: 
    if(candidato2 > candidato1 and candidato2 > candidato3):
        vencedor = 2
    else:
        if(candidato3 > candidato1 and candidato3 > candidato2):
            vencedor = 3

print('*** Resultado ***')
if(vencedor == 0):
    print('Tivemos um empate!')
else:
    print('O candidato', vencedor, ' venceu!')
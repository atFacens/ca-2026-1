# Um consultório atende adultos e jovens (menos 18 anos) apenas
# No início do dia temos uma lista de atendimentos contendo a idade
# de cada paciente a ser atendido
# Escreva um programa que, dada a lista de idades, conte quantos
# pacientes são adultos e quantos são jovens

idades = [14, 32, 15, 23, 45, 12, 24, 32, 15, 16]

adultos = 0
# jovens = 0
qtde_atendimentos = len(idades) 

for i in range(qtde_atendimentos):
    if(idades[i] > 17):
        adultos += 1
    # else:
    #     jovens += 1

print('Total de atendimentos', qtde_atendimentos)
print('Total de adultos', adultos)
# print('Total de jovens', jovens)
print('Total de jovens', qtde_atendimentos - adultos)
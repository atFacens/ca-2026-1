# operadores lógicos
# E(and) OU(or) NAO(not)

esta_sol = False
eh_feriado = False

vou_para_praia = esta_sol and eh_feriado
print('Vou para a praia?',vou_para_praia)

tem_lapada_igual = True
tem_lampada_semelhante = True

troca_lampada = tem_lapada_igual or tem_lampada_semelhante

print('Troca a lampada?', troca_lampada)

print('Não Troca lampada?', not troca_lampada)
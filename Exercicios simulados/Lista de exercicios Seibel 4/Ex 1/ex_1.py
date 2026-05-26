# As tarifas de táxi consistem em uma tarifa básica de R$4,00, mais R$0,25 para cada 140 metros percorridos.
# Escreva uma função que calcule a distância percorrida (em quilômetros) como único parâmetro e retorna a tarifa total como único resultado.

def tarifa(km):
    metros = km * 1000
    fun = 4 + (0.25 * (metros / 140))
    return fun

print('R$ {}'.format(tarifa(12)))
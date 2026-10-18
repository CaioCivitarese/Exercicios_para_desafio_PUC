# Escreva um programa em Python 3 que leia um número real representando a temperatura em graus Celsius.
# O programa deve imprimir:
# • CONGELANTE se a temperatura for menor que 0.
# • AGRADAVEL se a temperatura estiver entre 0 e 25 (inclusive).
# • QUENTE se for maior que 25 e menor ou igual a 38.
# • EXTREMO se for maior que 38.

T = float(input())

if T < 0:
    print('CONGELANTE')
elif T <= 25:
    print('AGRADAVEL')
elif T > 25 and T <= 38:
    print('QUENTE')
elif T > 38:
    print('EXTREMO')
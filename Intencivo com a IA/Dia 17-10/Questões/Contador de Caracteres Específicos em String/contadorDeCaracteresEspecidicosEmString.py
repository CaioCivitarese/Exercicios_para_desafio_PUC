# Escreva um programa em Python 3 que leia uma palavra ou frase S e um caractere C.
# O programa deve contar quantas vezes o caractere C aparece em S de forma case-insensitive (ignorando
# maiúsculas/minúsculas) e imprimir a mensagem TOTAL: X

S = input()
C = input().upper()
N = 0
lista = list(map(str, S.upper()))

for i in range(len(lista)):
    if lista[i] == C:
        N += 1

print('TOTAL:', N)
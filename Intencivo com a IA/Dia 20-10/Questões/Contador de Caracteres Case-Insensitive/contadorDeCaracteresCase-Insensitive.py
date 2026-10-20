# Escreva um programa que leia uma string S na primeira linha e um caractere X na segunda linha. O programa deve contar quantas
# vezes o caractere X aparece na string S de forma case-insensitive (ignorando maiúsculas e minúsculas) e imprimir no formato
# OCORRENCIAS: N.

S = input().upper()
X = input().upper()
N = 0

ListaS = list(map(str, S))

for i in range(len(ListaS)):
    if ListaS[i] == X:
        N += 1
    
print('OCORRENCIAS:', N)

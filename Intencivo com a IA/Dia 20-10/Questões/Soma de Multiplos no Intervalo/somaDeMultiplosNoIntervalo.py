# Escreva um programa que leia três inteiros A, B e K (um por linha). O programa deve calcular e imprimir a soma de todos os
# inteiros no intervalo fechado [A, B] que são múltiplos de K. Se não houver nenhum múltiplo no intervalo, imprima SOMA: 0'

A = int(input())
B = int(input())
K = int(input())
N = 0

for i in range(A, B + 1):
    if i % K == 0:
        N += i
    
print('SOMA:', N)

# Escreva um programa em Python 3 que receba dois inteiros positivos A e B (com A <= B).
# O programa deve calcular e imprimir a soma de todos os números pares no intervalo fechado [A, B].

A = int(input())
B = int(input())
sub = B - A
Num = 0
for i in range(sub + 1):
    N = A + i
    if N % 2 == 0:
        Num += N

print(Num)

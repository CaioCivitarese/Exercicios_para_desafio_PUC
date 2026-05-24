# 1) ­Crie um programa que leia dois inteiros do teclado, a e b, calcule e exiba:
#     ◦ a soma de a e b 
#     ◦ o valor da diferença entre b e a 
#     ◦ o produto de a e b
#     ◦ o quociente de a dividido por b
#     ◦ o resto da divisão entre a e b
#     ◦ o resultado de log10 a 
#     ◦ o resultado de ab 
# Obs: Use o módulo math para calcular o log10 a.
from math import log10

a = int(input('Digite um valor para (a): '))
b = int(input('Digite um valor para (b): '))

s = a + b
dif = a - b
mult = a * b
resto_div = a % b
div = a / b
log = log10(a)

print('a soma e igual a: {}, a diferença e igual a: {}, a multplicação e igual a: {}, o resto e igual a: {}, a divição e igual a: {}, já o log10 e igual a: {}.'.format(s, dif, mult, resto_div, div, log, a, b))

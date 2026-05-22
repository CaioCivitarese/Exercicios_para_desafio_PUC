# Elaborar um programa que tenha a funcionalidade de uma “calculadora” de dois operandos:
# Entrada de dados Entre com o operando 1: 6 Entre com o operador: * < ’+’, ’-‘, ‘*’, ‘/’, ‘%’,
# ‘^’=exponencial, e outros Entre com o operando 2: 3 Saída 6*3=18

n1 = float(input('Escreva um numero: '))
n2 = float(input('Escreva Outro numero: '))
n3 = input('Escreva o operador: ')

if n3 == '+':
    print(n1 + n2)
elif n3 ==  '-':
    print(n1 - n2)
elif n3 == '*':
    print( n1 * n2)
elif n3 == '/':
    print(n1 / n2)
elif n3 == '^':
    print(n1 ** n2)
else:
    print('Operador Invalodo')

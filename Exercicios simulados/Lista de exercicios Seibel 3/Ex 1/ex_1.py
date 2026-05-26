# Desenvolva um programa que leia do teclado um inteiro de 4 dígitos e que exiba a soma dos dígitos do número. 
# Por exemple, se for digitado o inteiro 3141 então seu programa deverá exibir 3+1+4+1=9.

num = int(input('Qual o valor(de um numero com 4 digitos): '))
texto = str(num)

# Resolução do chat:

numero = input("Digite um número de 4 dígitos: ")

soma = int(numero[0]) + int(numero[1]) + int(numero[2]) + int(numero[3])

print(soma)
# Leia três números e imprima o maior deles.

num1 = int(input('Qual o Primeiro numero: '))
num2 = int(input("Qual o Segundo numero: "))
num3 = int(input("Qual o Terceiro numero: "))
listaDeNumeros = {num1, num2, num3}

print(max(listaDeNumeros))

# 31  -  Crie  um  programa  que  realiza  a  Progressão  Aritmética  de  20
# elementos, com primeiro termo e razão definidos pelo usuário:

num = int(input('Qual o numero: '))
raz = int(input('Qual o numero: '))
listaDeNumeros = [num]
num1 = num

for i in range(20):
    num1 += raz
    listaDeNumeros.append(num1)


print(listaDeNumeros)
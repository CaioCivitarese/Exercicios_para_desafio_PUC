# 32  -  Crie  um  programa  que  exibe  em  tela  a  tabuada  de  um
# determinado número fornecido pelo usuário:

num = int(input('Qual o numero: '))
num2 = num
num1 = 1
listaDaTabuada = []

for i in range(10):
    num *= num1
    num1 += 1
    print(num)
    num = num2

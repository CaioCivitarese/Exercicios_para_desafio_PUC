# N = int(input('Qual a linha inicial ocupada pelo aluno: '))
# M = int(input('Qual a colina inicial ocupada pelo aluno: '))
# P = int(input('Quantas dezes sera mudada a posição dos alunos: '))
# O = 0
# C = 0
# A = 0
# B = 0
# K = 0
# Y = 0

# ListaDeNumeros = []
# ListaDeDentro = []
# X = '/'
# formula1 = N * M

# while K != M:
#     for i in range(N):
#         C += 1 
#         ListaDeDentro.append(C)

#     ListaDeNumeros.append(ListaDeNumeros)
#     ListaDeDentro = []
#     K += 1
# for i in range(P):
#     O = input('Qual Vc vai alterar: ')
#     A = int(input('Qual o primeiro: '))
#     B = int(input('Qual o segundo: '))

#     if O == 'L':
#         ListaDeNumeros[A - 1], ListaDeNumeros[B - 1] = ListaDeNumeros[B - 1], ListaDeNumeros[A - 1]
#     elif O == 'C':
#         ListaDeDentro[A - 1], ListaDeDentro[B - 1] = ListaDeDentro[B - 1], ListaDeDentro[A - 1] 

# for i in range(M):
#     for i in range(N):
#         ListaDeNumeros.append(ListaDeDentro[Y])
#         Y += 1

#     Y = 0

# print(ListaDeNumeros)

N = int(input())
M = int(input())
P = int(input())

O = 0
C = 0
A = 0
B = 0
K = 0

ListaDeNumeros = []
ListaDeDentro = []

while K != N:

    for i in range(M):
        C += 1
        ListaDeDentro.append(C)

    ListaDeNumeros.append(ListaDeDentro)
    ListaDeDentro = []

    K += 1


for i in range(P):

    O = input()
    A = int(input())
    B = int(input())

    if O == 'L':

        ListaDeNumeros[A - 1], ListaDeNumeros[B - 1] = \
        ListaDeNumeros[B - 1], ListaDeNumeros[A - 1]

    elif O == 'C':

        for j in range(N):

            ListaDeNumeros[j][A - 1], ListaDeNumeros[j][B - 1] = \
            ListaDeNumeros[j][B - 1], ListaDeNumeros[j][A - 1]


for i in range(N):
    print(*ListaDeNumeros[i])
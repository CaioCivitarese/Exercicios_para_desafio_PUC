# K = int(input('Numero de caracteres da linguagem alienigena: '))
# N = int(input('Numero de caracteres digitados: '))
# numero = 0
# X = 0
# Y = 0
# T1 = input('Escreva o alfabeto estraterestre aqui: ')
# T2 = input('Escreva a frase aqui: ')

# lista1 = list(map(str, T1.split('')))
# lista2 = list(map(str, T2.split('')))

# media2 = len(lista2) / 2

# if len(lista1) == K  & len(lista2) == N:

#     for i in range(K):
#         while numero != Y:
#             if lista1[X] ==  lista2[Y]:
#                 numero += 1
#                 Y += 1
#             else:
#                 Y+= 1
#         X += 1

#     if numero > media2:
#         print('S')
#     else:
#         print('N')    


K, N = map(int, input().split())

T1 = input()
T2 = input()

lista1 = list(T1)
lista2 = list(T2)

resultado = True

for caractere in lista2:
    if caractere not in lista1:
        resultado = False
        break

if resultado:
    print("S")
else:
    print("N")
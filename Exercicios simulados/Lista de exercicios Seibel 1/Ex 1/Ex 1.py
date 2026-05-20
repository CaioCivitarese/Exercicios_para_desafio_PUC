# Jogar “par ou ímpar” com o computador, por 10 iterações, e indicar o que ocorreu mais vezes
# (você venceu, o computador venceu ou empatou). Deve ser questionada a sua escolha e deve
# ser gerada aleatoriamente a escolha do computador (números de 0 a 10). O computador escolhe
# sempre par, assim, se a soma dos números escolhidos for par, o computador venceu, se for
# ímpar, você venceu.

import random

par_ou_impar = input('Você quer Par ou Impar: ')
seu_numero = int(input('Escreva um numeros de 0 a 10: '))
numero_computador = random.randint(0, 10)
pi = 'par'

if seu_numero % 2 == 0:
    pi2 = 'Par'
    # print('par')
else:
    pi2 = 'Impar'
    # print('impar')


if numero_computador % 2 == 0:
    pi3 = 'Par'
    # print('par')
else:
    pi3 = 'Impar'
    # print('impar')

if par_ou_impar == 'par':
    pi = 'Par'
    # print('Par')
elif par_ou_impar == 'impar':
    pi = 'Impar'
    # print('Impar')
else:
    print('Invalido')

if pi2 == pi3:
    print(numero_computador)
    print('Deu Par')
else:
    print(numero_computador)
    print('Deu Impar') 
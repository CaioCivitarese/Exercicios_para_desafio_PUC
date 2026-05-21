# Elabore um programa para fazer 10 jogos da super-mega-sena, cada um com 6 números
# pertencentes ao intervalo [10,99]. Use a biblioteca de geração de números aleatórios para isso.
# DICA: Para evitar números repetidos em sua aposta, armazene os números em uma string
# separados por um espaço e verifique se o número pertence à string.
import random

nj = 0
nm = random.randint(10, 99)

while nj != 10:
    p1 = int(input('Digite seu numero: '))
    p2 = int(input('Digite seu numero: '))
    p3 = int(input('Digite seu numero: '))
    p4 = int(input('Digite seu numero: '))
    p5 = int(input('Digite seu numero: '))
    p6 = int(input('Digite seu numero: '))

    if nm == p1:
        print(p1)
        print('Participante 1 venceu!!!')

    elif nm == p2:
        print(p2)
        print('Participante 2 venceu!!!')

    elif nm == p3:
        print(p3)
        print('Participante 3 venceu!!!')

    elif nm == p4:
        print(p4)
        print('Participante 4 venceu!!!')

    elif nm == p5:
        print(p5)
        print('Participante 5 venceu!!!')
    elif nm == p6:
        print(p6)
        print('Participante 6 venceu!!!')
    else:
        print('Inguem venceu')
    
    nj = nj + 1
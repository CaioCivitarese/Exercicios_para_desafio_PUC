# Questão 1: Classificação de Triângulos (4 Pontos)

# Escreva um programa em Python que leia três números inteiros A, B e C (um por linha) representando os três lados de um
# triângulo. O programa deve verificar se os lados formam um triângulo válido (a soma de quaisquer dois lados deve ser estritamente
# maior que o terceiro lado).
# • Se for válido, imprima EQUILATERO (3 lados iguais), ISOSCELES (2 lados iguais) ou ESCALENO (3 diferentes).
# • Se não for válido, imprima INVALIDO

A = int(input())
B = int(input())
C = int(input())

if A + C > B and A + B > C and B + C > A:
    if A == C and A == B:
        print("EQUILATERO")
    elif A == C or A == B or C == B:
        print('ISOSCELES')
    else:
        print('ESCALENO')
else:
    print('INVALIDO')

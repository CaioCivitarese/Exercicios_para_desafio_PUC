# N = numero de Lances
# C = Nome da pessoa
# V = Valor do lance

N = int(input('Qual o nomero de lances: '))
C = 0
V = 0
valorAnterior = 0
nomeAnterior = 0
lances = []

for c in range(N):
    C = input('Qual seu nome: ')
    V = int(input('Qual o Valor de seu lance: '))

    if V > valorAnterior:
        nomeAnterior = C
        valorAnterior = V


print(nomeAnterior)
print(valorAnterior)


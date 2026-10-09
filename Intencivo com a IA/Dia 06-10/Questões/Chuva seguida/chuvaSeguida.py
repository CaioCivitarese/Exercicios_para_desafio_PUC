# N == numero de segundos
# 1 == choveu
# 0 == não choveu

N = int(input())
num = 0
numAnterior = 2

listaDeSequncias = []

for i in range(N):
    num = int(input())

    if num == numAnterior:
        num = numAnterior
        
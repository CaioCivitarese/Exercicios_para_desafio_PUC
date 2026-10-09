# D == numero de dias
# T == temperatura

D = int(input())
T = 0
listaDeTemperatura = []
N = 0

for i in range(D):
    T = int(input())
    listaDeTemperatura.append(T)

mediaListaTemperatura = sum(listaDeTemperatura) / D

for i in range(len(listaDeTemperatura)):
    if listaDeTemperatura[i] > mediaListaTemperatura:
        N += 1

print(N)

# K = Numeros de caditatos que podem ser aprovados
# C = maior nota que K canditatos sejam aprovados
# N = Numero de canditados

N = int(input()) 
K = int(input())
listaDeNotas = []

for i in range(N):
    A = int(input())
    listaDeNotas.append(A)

for i in range(N - K):
    listaDeNotas.remove(min(listaDeNotas))

print(listaDeNotas[0])
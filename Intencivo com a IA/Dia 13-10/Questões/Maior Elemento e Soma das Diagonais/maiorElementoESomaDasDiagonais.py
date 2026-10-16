N = int(input())
num = 0
I = 0
numLista = []
numsoma = N
somaLista = []
ListMax = []
listaMap1 = []
listaMap2 = []
for c in range(N):
    num = input()
    numLista = list(map(int, num))
    somaLista.append(numLista[numsoma])
    numsoma -= 1
    ListMax.append(max(numLista))

    for i in range(N):
        if max(numLista) == numLista[i]:
            listaMap1.append(i)
            listaMap2.append(c)
        
S = sum(somaLista)
V =  max(ListMax)

for d in range(N):
    if V == ListMax[d]:
        I = d

print('SOMA DIAGONAL', S)
print('MAIOR: {} EM ({}, {})'.format(V, listaMap1[I], listaMap2[I]))
        
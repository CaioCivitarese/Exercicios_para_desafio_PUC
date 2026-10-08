# M == altiara da maré (um inteiro, em centímetros, que pode ser negativo)
# N == quantidade de mediadas

N = int(input())
M = 0
ListadeM = []
Manterior = 0
maiorValor = 0
num = 0

for i in range(N):
    M = int(input())
    ListadeM.append(M)

for i in range(N):
    if maiorValor < ListadeM[i]:
        maiorValor = ListadeM[i]
        Manterior = ListadeM[i]
    elif ListadeM[i] > Manterior:
        maiorValor = ListadeM[i]
        Manterior = ListadeM[i]
    else:
        Manterior = ListadeM[i]

for i in range(N):
    if maiorValor == ListadeM[i]:
        num = i + 1
        break



print('MAIOR:', maiorValor)
print('POSICAO:', num)

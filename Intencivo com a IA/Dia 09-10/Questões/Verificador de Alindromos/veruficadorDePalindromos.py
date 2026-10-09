S = input()
Slista = list(map(str, S))
N = len(Slista)
lista1 = []

for i in range(N):
    if Slista[i].isupper() == True:
        Slista[i].lower()
    elif Slista[i] == ' ':
        Slista.pop(i)

for i in range(N):
    lista1.append(Slista[N - i])

if lista1 == Slista:
    print('SIM')
else:
    print('NAO')
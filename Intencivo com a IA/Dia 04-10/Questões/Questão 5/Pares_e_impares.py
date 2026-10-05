N1 = int(input())
N2 = int(input())
N3 = int(input())

Lista = [N1, N2, N3]
listaRespostas = []
contagemP = 0

for i in range(3):

    if Lista[i] % 2 == 0:
        listaRespostas.append("P")
        contagemP += 1
    else:
        listaRespostas.append('I')

ListaFinal = " ".join(listaRespostas)

print(contagemP)

if ListaFinal == "P P P":
    print("TODOS")
elif ListaFinal == "I I I":
    print('NENHUM')
else: 
    print('ALGUNS')
    
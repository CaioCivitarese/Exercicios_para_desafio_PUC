# M = Limeite de calorias
# N = Numero de refeições
# a cada 1 grama de proteina tem 4 calorias
# a cada 1 grama de gordura tem 9 calorias
# a cada 1 grama de carbidrato tem 4 calorias

M = int(input("Qual o limite de calorias: "))
N = int(input("Qual a quantidade de refeições já engeridas: "))
P = 0
G = 0
C = 0
listaDeCalorias = []

for c in range(N):
    P = int(input("Qual a quantidade de proteinas: "))
    G = int(input("Qual a quntidade de gordura: "))
    C = int(input("Qual a quantidade de carboidrato: "))

    P *= 4
    G *= 9
    C *= 4

    listaDeCalorias.append(P)
    listaDeCalorias.append(G)
    listaDeCalorias.append(C)

resut = M - sum(listaDeCalorias) 

print(resut)

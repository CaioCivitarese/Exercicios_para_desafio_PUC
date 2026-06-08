# N = Numero de chocolates escolidos
# P = Preço de cada chocolate 

N = int(input('Quantos chocolates você escolheu: '))
P = 0
listaDePreços = []

for c in range(N):
    P = int(input('Qual o preço do chocolate: '))
    listaDePreços.append(P)

listaDePreços.sort(reverse=True)

total = sum(listaDePreços)

desconto = 0

for i in range(2, len(listaDePreços), 3):
    desconto += listaDePreços[i]

print(total - desconto)

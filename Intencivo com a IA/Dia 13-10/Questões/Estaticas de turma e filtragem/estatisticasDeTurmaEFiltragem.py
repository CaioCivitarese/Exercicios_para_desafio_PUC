# N == quantidade de alunos 
# num = nota dos alunos

N = int(input())
num = 0
listaNotas = []
maiorMedia = 0
for i in range(N):
    num = float(input())
    listaNotas.append(num)

media = sum(listaNotas) / N
maiorNota = max(listaNotas)

for i in range(N):
    if listaNotas[i] > media:
        maiorMedia += 1

print('MEDIA:', media)
print('MAIOR:', maiorNota)
print('ACIMA:', maiorMedia)

# C = Nota de corte
# K = numero de candidatos a ser aprovados
# N = Numero de cadidatos

N = int(input('Qual o nomeros de participantes: '))
K = int(input('Qual o numero de aprovados: '))

Nota = 0
notaAterior = 0
listaDeNotas = []
for c in range(N):
    Nota = int(input('Qual a nota do candidato: '))
    listaDeNotas.append(Nota)

maiores = sorted(listaDeNotas, reverse=True)[:K]

C = min(maiores)

print(C)

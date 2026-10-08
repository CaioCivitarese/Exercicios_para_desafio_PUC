# N == Numero de alunos 
# calular a media da turma
# calcular a quanrtidade de aprovados 

N = int(input())

Nota = 0
listaDeNotas = [] 
Naprovados = 0

for i in range(N):
    Nota = float(input())

    if Nota >= 6:
        listaDeNotas.append(Nota)
        Naprovados += 1
    else:
        listaDeNotas.append(Nota)

mediaListaDeNotas = sum(listaDeNotas) / N

print('MEDIA:', round(mediaListaDeNotas, 1))
print('APROVADOS:', Naprovados)

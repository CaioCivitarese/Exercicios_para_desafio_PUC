# N = cadeira na frente do profeçor
# j = cadeira no meio
# i = Ultima cadeira da fileira
# I = numero da cadira do aluno
# A = temanho em centimetos do aluno

N = int(input('Quatos alunos tem na sala: '))
A = 0
anterior = 0
N1 = 0

for i in range(N):
    A = int(input('Altira do aluno: '))
    while A > anterior:
        N1 += 1

    if A > anterior:
        anterior = A
    else:
        break
    
resultado = A - N1
print(resultado)

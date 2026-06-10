# N = Quantidade de alunos
# A = lista das aulturas dos alunos

N = int(input('Quantidade de alunos em sala: '))
A = 0
Amod = 0
Amod1 = 0
result = 0

for c in range(N - 1):
    A = int(input('Qual a altura dos alunos: '))
    
    if Amod < A or A > Amod1:
        result += 1

    if A > Amod1:
        Amod1 = A
    
    Amod = A    
        
    
    
A = int(input('Qual a altura dos alunos: '))

print(result)

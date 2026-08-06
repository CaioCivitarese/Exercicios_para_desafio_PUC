# Volume minimo = A
# Volume maximo = B
# Capacidade = C
# dose de café = D




A = int(input('Volume minimo de leite: '))
B = int(input('Volume maximo de leite: '))
C = int(input('Capacidade da xícara: '))
D = int(input('Doses de café: '))
n1 = D + A
n2 = D + B

if n1 <= C:
    print('S') 
elif n2 <= C:
    print('S')
elif n1 > C & n2 > C:
    print('N')
            

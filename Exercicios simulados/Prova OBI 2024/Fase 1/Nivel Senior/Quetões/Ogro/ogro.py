# E = Valor da mão esquerda
# D = Valor da mão direita
# E > D == E + D
# E < D ==  2 * (D - E)

E = int(input('Numero de dedos da mão Esquerda: '))
D = int(input('Numero de dedos da mão Direita: '))

if E > D:
    resultado = E + D
else: 
    resultado = 2 * (D - E)

print(resultado)

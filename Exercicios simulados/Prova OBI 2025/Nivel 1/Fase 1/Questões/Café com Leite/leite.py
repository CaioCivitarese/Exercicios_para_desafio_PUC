# A = Volume minimo de Leite
# B = Volume maximo de Leite
# C = Capacidade de sua xícara
# D = volume de caé preparado pela máquina

A = int(input('Qual o volume minimo de leite: '))
B = int(input('Qual o volume maximo de leite: '))
C = int(input('Qual a capacidade de sua xícara: '))
D = int(input('Qual o volume de café feito em cada dose: '))

form = C - D
result = B >= form >= A

if result == True:
    print('S')
else: 
    print('N')

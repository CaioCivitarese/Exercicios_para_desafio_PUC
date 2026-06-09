# A = Volume minimo de Leite
# B = Volume maximo de Leite
# C = Capacidade de sua xicara
# D = quantidade de café em cada dose

A = int(input("Qual o volume minimo de leite: "))
B = int(input("Qual o volume maximo de leite: "))
C = int(input("Qual a capacidade de sua xicara: "))
D = int(input("Volume de cafe para cada dose feita pela máquina: "))
V = 0
intervalo = abs(A - C)
intervalo2 = abs(B - C)

while D % intervalo == 0 or D % intervalo2 == 0:
    V += D

    if V > C:
        print("N")
        break
    

if intervalo == True:
    print("S")

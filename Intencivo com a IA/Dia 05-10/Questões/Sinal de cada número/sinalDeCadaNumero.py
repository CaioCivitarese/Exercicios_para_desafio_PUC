# N = Numero de Interirios
# num = numero

N = int(input())
lintaNum = []

num = input()
L = num.split()
linhaNum = list(map(int, L)) 

for i in range(N):
    if linhaNum[i] > 0:
        print("POSITIVO")
    elif linhaNum[i] < 0:
        print("NEGATIVO")
    elif linhaNum[i] == 0:
        print("ZERO")
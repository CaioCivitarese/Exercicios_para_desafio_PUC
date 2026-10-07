N = int(input())
num = input()
O = 0

linhanum = num.split()
ListaNum = list(map(int, linhanum))

for i in range(N):
    if ListaNum[i] < 0:
        O = i + 1
        break

if O == 0:
    print("NENHUM")
else:
    print(O)

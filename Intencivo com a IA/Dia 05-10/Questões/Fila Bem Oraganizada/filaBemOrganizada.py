N = int(input())
Num = input()
listaNum = list(map(int, Num.split()))
num = 0
Anum = 0

for i in range(N):
    
    if listaNum[i] > num:
        num = listaNum[i]
    elif listaNum[i] <= num:
        print('NAO')
        Anum += 1
        break

if Anum == 0:
    print('SIM')

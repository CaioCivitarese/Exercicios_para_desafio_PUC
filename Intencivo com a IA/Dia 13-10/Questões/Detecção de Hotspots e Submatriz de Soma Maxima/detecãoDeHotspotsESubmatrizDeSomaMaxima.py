N, M, K = int(input())
H = 0
O = []
if K <= N and K <= M:
    listaM = []
    for i in range(N):
        H = input()
        Hlist = list(map(str, H))
        He = " ".split(Hlist)
        O.append(He)

    L = int(input())

    print(O)

    


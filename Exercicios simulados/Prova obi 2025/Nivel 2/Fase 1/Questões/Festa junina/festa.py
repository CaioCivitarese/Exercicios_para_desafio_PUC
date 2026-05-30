E = int(input('Qual a posição da escola: '))
S = int(input('Qual a posição do supermercado: '))
L = int(input('Qual a posição da loginha: '))

if E != S and S != L and L != E:
    if E < S and E < L:
        if S > L:
            d1 = L - E
            d2 = S - L
            d3 = L - E
        elif L > S:
            d1 = S - E
            d2 = L - S
            d3 = E - L
    elif E > S and E > L:
        if S > L:
            d1 = E - L
            d2 = S - L
            d3 = E - S
        elif L > S:
            d1 = E - S
            d2 = L - S
            d3 = E - L
    elif E > S and E < L:
        if S > L:
            d1 = E - L
            d2 = S - L
            d3 = E - S
        elif L > S:
            d1 = E - S
            d2 = L - S
            d3 = L - E
    elif E < S and E > L:
        if S > L:
            d1 = E - L
            d2 = S - L
            d3 = S - E
        elif L > S:
            d1 = S - E
            d2 = L - S
            d3 = E - L

    print(d1 + d2 + d3)
else:
    print('Os valores são equivalestes tente novamente')

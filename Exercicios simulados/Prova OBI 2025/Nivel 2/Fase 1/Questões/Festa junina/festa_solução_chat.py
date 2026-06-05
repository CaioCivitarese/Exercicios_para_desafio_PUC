E = int(input())
S = int(input())
L = int(input())

d1 = abs(E - S)
d2 = abs(S - L)
d3 = abs(L - E)

print(d1 + d2 + d3)
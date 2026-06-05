D = int(input())
A = int(input())
N = int(input())

diarias = 32 - N

if N <= 15:
    valor_diaria = D + (N - 1) * A
else:
    valor_diaria = D + 14 * A

total = diarias * valor_diaria

print(total)
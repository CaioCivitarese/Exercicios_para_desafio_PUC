M = int(input('Qual o valor máximo de calorias: '))
N = int(input('Quantas refeições: '))

cal_T = 0

for i in range(N):
    print(f'\nRefeição {i+1}')

    P = int(input('Proteínas: '))
    G = int(input('Gordura: '))
    C = int(input('Carboidrato: '))

    cal_T += (4 * P) + (9 * G) + (4 * C)

print(f'\nTotal de calorias: {cal_T}')
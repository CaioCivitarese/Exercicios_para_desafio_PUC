N = int(input())

num = 0
listanum = []
numPositivo = []
numNegativo = 0

for i in range(N):
    num = int(input())

    if num > 0:
        numPositivo.append(num)
    elif num < 0:
        numNegativo += 1

print('POSITIVOS:', sum(numPositivo))
print('NEGATIVOS:', numNegativo)
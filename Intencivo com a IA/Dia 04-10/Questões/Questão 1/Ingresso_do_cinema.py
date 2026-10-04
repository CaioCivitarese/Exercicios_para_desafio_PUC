# Meia == 10 (menos de 12 e maior ou igual a 60)
# inteira == 20
# quarta == 10 todos

I = int(input())
D = int(input())

if (I < 12 or I >= 60) or D == 4:
    print(10)
else:
    print(20)

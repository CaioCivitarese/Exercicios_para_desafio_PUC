# Q7:
#     resposta: b)
# Q8: 

num = int(input())

if num > 0 & num % 2 == 0:
    print('Positivo e par')
elif num > 0 & num % 2 != 0:
    print('positivo e impar')
elif num < 0 & num % 2 == 0:
    print('Negativo e par')
elif num < 0 & num % 2 != 0:
    print('Negativo e impar')
else: 
    print('Zero')

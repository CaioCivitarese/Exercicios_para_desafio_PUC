# 1. Ter comprimento de no mínimo 8 caracteres.
# 2. Conter pelo menos uma letra maiúscula ('A' a 'Z').
# 3. Conter pelo menos uma letra minúscula ('a' a 'z').
# 4. Conter pelo menos um dígito numérico ('0' a '9').

S = input()
Slista = list(map(str, S))
num = 0
num1 = 0
num2 = 0
num3 = 0

for i in range(len(Slista)):
    if len(Slista) >= 8:
        num += 1
    
    if Slista[i].isupper() == True:
        num1 += 1
    elif Slista[i].islower() == True:
        num2 += 1
    elif Slista[i].isdigit() == True:
        num3 += 1

if (num1 + num2 + num3) == len(Slista) and num >= 1 and num1 >= 1 and num2 >= 1 and num3 >= 1:
    print('SENHA VALIDA')
else:
    print('SENHA INVALIDA')
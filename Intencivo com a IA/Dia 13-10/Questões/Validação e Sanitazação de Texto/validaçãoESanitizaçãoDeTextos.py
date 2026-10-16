# Possuir **pelo menos 8 caracteres** (sem contar espaços nas pontas)
# Conter **pelo menos uma letra maiúscula** e **pelo menos uma letra minúscula**
# Conter **pelo menos um dígito numérico** (0 a 9)

S = input()
Slista = list(map(str, S))
Maiuscula = 0
Minuscula = 0
num = 0

if len(Slista) >= 8:
    for i in range(len(Slista)):
        if Slista[i].isupper() == True:
            Maiuscula += 1
        elif Slista[i].islower() == True:
            Minuscula += 1
        elif Slista[i].isnumeric() == True:
            num += 1

    if Maiuscula >= 1 and Minuscula >= 1 and num >= 1:
        print('FORTE')
    else:
        print('FRACA')
else:
    print('FRACA') 

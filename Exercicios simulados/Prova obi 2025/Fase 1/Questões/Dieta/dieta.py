M = int(input('Qual o valor maximo de calorias: '))
N = int(input('Qualtas refeições: '))
P = int(input('Qual a quantidade de proteinas: '))
G = int(input('Qual a quantidade de gordura: '))
C = int(input('Qual a quantidade de carboidrato: '))
cal_C = 1
cal_G = 1
cal_P = 1
cal_T = 1
nt = 1

while nt != N: 
    cal_P = 4 * P
    cal_G = 9 * G 
    cal_C = 4 * C
    cal_T = cal_C + cal_G + cal_P 

    nt = nt + 1


if M > cal_T:
    cal_rest = M - cal_T
    print(cal_rest)
elif M == cal_T:
    print('Suas calorias foram:  {}, e o seu valor maximo é: {}'.format(cal_T, M))
    print('Você atindiu o maximo de calorias.')
else:
    cal_ultra = cal_T - M
    print('Suas calorias foram:  {}, e o seu valor maximo é: {}'.format(cal_T, M))
    print('Você ultrapasou as calorisa determinadas. o valor ultrapasado foi: {}'.format(cal_ultra))

# 3) Escreva um programa que leia uma data (dia e mês) e indique a estação do ano correspondente de acordo com a tabela abaixo:
#     Estação		data de início
#     Primavera		22 setembro
#     Verão		    22 dezembro
#     Outono		21 março
#     Inverno		21 junho

mes = int(input('e de que mes (ponha em valor): '))

if mes == 1 or mes == 2 or mes == 4 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 11:
    if mes == 1 or mes == 2:
        print('Verão')
    elif mes == 4 or mes == 5:
        print('Outono')
    elif mes == 7 or mes == 8:
        print('Inverno')
    else:
        print('Primavera')
else:
    dia = int(input('Que dia você quer saber: '))

    if mes == 3 or dia <= 20:
        print('Verão')
    elif mes == 3 or dia > 20:
        print('Outono')
    elif mes == 6 or dia <= 20:
        print('Outono')
    elif mes == 6 or dia >= 21:
        print('Inverno')
    elif mes == 9 or dia <= 21:
        print('Inverno')
    elif mes == 9 or dia >= 22:
        print('Primavera')
    elif mes == 12 or dia <= 20:
        print('Primavera')
    elif mes == 12 or dia <= 21:
        print('Verão')
    else:
        print('Data invalida')

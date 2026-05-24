# Faça um programa que leia um valor a ser retirado em um caixa eletrônico e que retorne a menor quantidade de notas.
# Considere que o caixa contém notas de R$100,00, de R$50,00, de R$20,00, de R$10,00 e de R$5,00.
# Indique quantas notas de cada valor serão retiradas.

valor_pagar = int(input('Qual o valor que você que sacar: '))

nota100 = valor_pagar // 100
nota50 = valor_pagar // 50
nota20 = valor_pagar // 20
nota10 = valor_pagar // 10
nota5 = valor_pagar // 5

if valor_pagar == 5:
    print()

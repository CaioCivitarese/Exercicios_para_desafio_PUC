# Problema 1 — Cofrinho Inteligente
# João possui moedas de 1 real, 50 centavos e 25 centavos.
# Seu programa deve ler a quantidade de cada moeda e informar o valor total arrecadado.
# Entrada
# A entrada contém três números inteiros:
# quantidade de moedas de 1 real
# quantidade de moedas de 50 centavos
# quantidade de moedas de 25 centavos
# Saída
# Exiba o valor total em reais.

moedas_de_1_real = int(input('Quantas moedas de 1 real você possui: '))
moedas_de_50_centavos = int(input('Quantas moedas de 50 centavos você tem: '))
moedas_de_25_centavos = int(input('Quantas moedas de 25 centavos você tem: '))

formula = (1 * moedas_de_1_real) + (0.50 * moedas_de_50_centavos) + (0.25 * moedas_de_25_centavos)

print('O valor que você tem é R$',formula)

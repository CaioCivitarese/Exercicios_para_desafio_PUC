# 29 - Crie um programa que lê um valor de início e um valor de fim,
# exibindo em tela a contagem dos números dentro desse intervalo.

numInicio = int(input('Qual o numero de inicio: '))
numFim = int(input('Qual o numero do fim: '))

while numInicio != numFim:
    numInicio += 1
    print(numInicio)

# inicio = int ( input ( 'Digite o número onde começa a contagem: ' ))
# fim = int ( input ( 'Digite o número onde termina a contagem: ' ))
 
# for  i  in   range ( inicio ,  fim+ 1 ):
#    print ( i )
 
 
# Sempre  que  temos  um  intervalo  numérico  com  início  e  fim  pré-
# estabelecidos, podemos usar do método range( ) para ler todos elementos
# desse intervalo. Associando o operador lógico in, usando range( ) dentro
# de um laço for, é possível percorrer e iterar sobre cada elemento dentro do
# intervalo.
# Sendo  assim,  declaradas  as  variáveis  inicio  e  fim  que  recebem
# números  digitados  pelo  usuário,  em  nossa  estrutura  de  repetição
# parametrizamos nosso método range( ) com os dados de inicio e de fim
# incrementado de 1. É necessário fazer essa pequena codificação adicional
# pois em Python quando estamos lendo números dentro de um intervalo, o
# último número lido não é contabilizado, mas serve como gatilho para que o
# processo seja encerrado naquele ponto.
# Em  outras  palavras,  apenas  como  exemplo,  para  percorrer
# elementos dentro de um intervalo entre 0 a 10 temos de parametrizar nosso
# range( ) com números entre 0 e 11.
# Supondo que o usuário deu entrada dos números 20 e 30 o retorno será:
 
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# *Caso  não  houvéssemos  definido  fim+1  como  parâmetro  em  range(  )  a
# contagem encerraria em 29, não atendendo o enunciado da questão.

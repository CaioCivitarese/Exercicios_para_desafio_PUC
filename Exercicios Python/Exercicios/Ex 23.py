# 23 - Verifique se o valor de num1 consta nos elementos de lista1. Sendo
# num1 = 100 e lista1 = [10, 100, 1000, 10.000, 100.000].

num1 = 100
lista1 = [10, 100, 1000,10000, 100000]
N = 0
R = False

for i in range(len(lista1)):
    if num1 == lista1[N]:
        print('Existe no elemento: ', N);
        N += 1
        R = True
    else:
        N += 1

if R == False:
    print('Esse numero não existe nessa lista!!!')

# num1 =  100
 
# lista1 =  [ 10 ,   100 ,   1000 ,   10000 ,   100000 ]
 
# print ( num1  in  lista1 )
 
 
# Aqui temos uma expressão lógica fazendo o uso do operador in,
# que basicamente nos é útil para verificar se um determinado dado/valor
# consta dentro de uma variável/objeto.
# Nesse caso, se o valor atribuído para num1 constar como um dos
# elementos de lista1, o retorno será Tru e  .

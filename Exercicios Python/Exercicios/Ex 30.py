# 30  -  Crie  um  programa  que  realiza  a  contagem  de  0  a  20,  exibindo
# apenas os números pares:

num1 = 0
num2 = 20

while num1 != num2:
    if num1 % 2 == 0:
        print(num1)
        num1 += 1
    else:
        num1 += 1

# for  i  in   range ( 0 ,   21 ):
#    if  i %  2  ==  0 :
#      print ( i )
 
 
# Da  mesma  forma  como  no  exemplo  anterior,  usando  do  método
# range( ) parametrizado com o valor de início e de fim (acrescido em uma
# unidade),  podemos  definir  que  serão  exibidos  apenas  os  números  pares
# simplesmente  criando  uma  condição  onde  apenas  serão  exibidos  os
# números os quais o resto de sua divisão por 2 seja 0.
#  for  i  in   range ( 0 ,   21 ,   2 ):
#    print ( i )
  
 
# Uma forma alternativa que temos para resolver esse exercício é
# usando  do  terceiro  parâmetro  em  justaposição  do  método  range(  )  que
# justamente define de quantos em quantos elementos devem ser retornados
# na função.
# Como para nosso exemplo estamos exibindo números pares, que
# logicamente,  sequencialmente  são  contados  de  dois  em  dois,
# parametrizando o método range( ) em seu terceiro parâmetro justaposto
# com o número 2, indiretamente exibiremos apenas os números pares.
# O retorno será:
 
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
20

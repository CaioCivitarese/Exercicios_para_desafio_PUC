# 32  -  Crie  um  programa  que  exibe  em  tela  a  tabuada  de  um
# determinado número fornecido pelo usuário:

num = int(input('Qual o numero: '))
num2 = num
num1 = 1
listaDaTabuada = []

for i in range(10):
    num *= num1
    num1 += 1
    print(num)
    num = num2

# x = int ( input ( 'Digite um Número: ' ))
 
# for  num  in   range ( 1 ,   11 ):
#      print ( f ' { x }  X  { num }  =  { x * num } ' )
    
 
# Para gerar uma simples tabuada podemos fazer o uso do método
# range( ), nos poupando serviço de realizar cada multiplicação do número
# fornecido por outro número.
# Inicialmente  criamos  uma  variável  de  nome  x  que  recebe  do
# usuário um número por meio da função input( ), validando o mesmo como
# do tipo int pois em uma tabuada básica não temos números com casas
# decimais.
# Em seguida por meio de um laço for, usando do método range( )
# percorreremos um intervalo de 1 a 10, a cada execução retornando um
# valor para num. Indentado para esse laço for simplesmente exibimos em
# tela  que  o  determinado  número,  multiplicado  pelo  valor  atual  de  num,
# resulta em um dado valor, nesse caso, o próprio valor de x multiplicado
# pelo valor de num.
# Tendo o usuário digitado 7, o retorno será:
 
 
# 7 X 1 = 7
# 7 X 2 = 14
# 7 X 3 = 21
# 7 X 4 = 28
# 7 X 5 = 35
# 7 X 6 = 42
# 7 X 7 = 49
# 7 X 8 = 56
# 7 X 9 = 63
# 7 X 10 = 70

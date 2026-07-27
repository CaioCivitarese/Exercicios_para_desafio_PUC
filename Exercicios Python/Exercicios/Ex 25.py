# 25 - Peça para que o usuário digite um número, em seguida exiba em
# tela uma mensagem dizendo se tal número é PAR ou se é ÍMPAR:

num = int(input('Digite um Numero: '))

if num % 2 == 0:
    print('Par')
else:
    print('Inpar')

# num = int ( input ( 'Digite um número: ' ))
 
# if   ( num %  2 )  ==  0 :
#      print ( f ' { num }  é PAR' )
# else :
#      print ( f ' { num }  é ÍMPAR' )
 
 
# Após criar a linha de código responsável por pedir ao usuário que
# o mesmo digite um número, validando esse número como do tipo inteiro e
# atribuindo o número em si a uma variável, vamos a estrutura condicional.
# Para verificar se um determinado número é par, simplesmente o
# resto da divisão desse número por 2 deve ser igual a 0. Logo, criamos uma
# condição onde se o resto da divisão do valor de num por 2 for igual a 0, é
# exibida uma mensagem dizendo que o mesmo é PAR, caso essa condição
# não seja verdadeira, é exibida em tela uma outra mensagem, dessa vez
# dizendo que o número em questão é ÍMPAR.
# Supondo que o usuário tenha digitado o número 15, o retorno gerado é ’15 é
# ÍMPAR’.

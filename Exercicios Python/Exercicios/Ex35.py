# 35 - Crie um programa que pede ao usuário que o mesmo digite um
# número qualquer, em seguida retorne se esse número é primo ou não,
# caso não, retorne também quantas vezes esse número é divisível:

num = int(input('Digite o numero: '))



if (num == 5) | (num == 2) | :
    print('Seu numeros e primo')

# numero = int ( input ( 'Digite um número: ' ))
# divisoes =  0
 
# for  i  in   range ( 1 ,  numero +  1 ):
#    if  numero % i ==  0 :
#     divisoes +=  1
 
# if  divisoes ==  2 :
#    print ( f ' { numero }  é primo!!!' )
#    print ( f ' { numero }  é divisível por 1 ou por  { numero } ' )
# else :
#    print ( f ' { numero }  não é primo!!!' )
#    print ( f ' { numero }  é divisível  { divisoes }  vezes...' )
 
 
# Lembrando que um número primo é aquele que apenas é divisível
# por 1 ou por ele mesmo, temos de criar essa condição lógica para poder
# solucionar esse exercício.
# Inicialmente por meio da função input( ) pedimos que o usuário
# digite um número, guardando esse valor na variável numero. Também é
# criada uma variável divisões que inicialmente está zerada.
# Na  sequência  criamos  um  laço  for  que  percorrerá  de  1  até  o
# número  digitado  pelo  usuário  +  1  via  método  range(  )  retornando  os
# valores para i a cada laço de repetição. Dentro do bloco referente ao nosso
# laço for criamos uma estrutura condicional onde se o módulo da divisão de
# número por i for igual a 0, divisoes recebe um incremento.
# Por fim, podemos criar uma simples estrutura condicional onde se
# o  último  valor  atribuído  a  divisoes  for  igual  a  2,  exibimos  em  tela  a
# mensagem referente a um número primo, caso contrário, exibimos em tela a
# mensagem referente a um número não primo.
# Supondo que o usuário digitou 97, o retorno será:
# 97 é primo!!!
# 97 é divisível por 1 ou por 97.
 
# Supondo que o usuário tenha digitado 98, o retorno será:
 
# 98 não é primo!!!
# 98 é divisível 6 vezes..

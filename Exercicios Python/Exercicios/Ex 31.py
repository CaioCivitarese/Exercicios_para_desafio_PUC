# 31  -  Crie  um  programa  que  realiza  a  Progressão  Aritmética  de  20
# elementos, com primeiro termo e razão definidos pelo usuário:

num = int(input('Qual o numero: '))
raz = int(input('Qual o numero: '))
listaDeNumeros = [num]
num1 = num

for i in range(20):
    num1 += raz
    listaDeNumeros.append(num1)


print(listaDeNumeros)

# termo = int ( input ( 'Digite o primeiro termo: ' ))
# razao = int ( input ( 'Digite a razão: ' ))
# pa = termo +  ( 20   -1 )  * razao
 
# for  i  in   range ( termo ,  pa + razao ,  razao ):
#    print ( i )
 
 
# Lembrando que uma progressão aritmética é uma operação onde
# definimos um número inicial e uma constante, também chamados de termo
# e razão, respectivamente. A progressão em si nada mais é do que a soma do
# termo anterior com a constante.
# Para nosso exercício pedimos que o usuário dê entrada tanto no
# termo (valor inicial) quanto na razão (constante) por meio da função input(
# ) atribuindo esses valores a suas respectivas variáveis.
# Na  sequência  criamos  uma  variável  de  nome  pa  que
# contextualizando a fórmula de uma progressão aritmética, pega o valor de
# termo, somando com a constante multiplicada pela razão. Lembrando de 
# realizar a subtração da constante em 1 para que tenhamos o gatilho para
# encerrar a progressão dentro do valor definido.
# A partir daí, podemos simplesmente criar um laço for que usando
# do método range( ) define o valor de termo como valor inicial, pa + razão
# como valor final, exibindo no intervalo estipulado por razão. Sendo que a
# cada execução do laço é exibido em tela o valor da progressão por meio da
# função print( ).
# Supondo que para termo o usuário tenha digitado 10, e para razão tenha
# digitado 3, o retorno será:
 
# 10
# 13
# 16
# 19
# 22
# 25
# 28
# 31
# 34
# 37
# 40
# 43
# 46
# 49
# 52
# 55
# 58
# 61
# 64
# 67

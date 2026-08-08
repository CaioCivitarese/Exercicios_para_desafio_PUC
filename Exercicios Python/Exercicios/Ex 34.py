# 34 - Crie um programa que realiza a contagem de 1 até 100, usando
# apenas de números ímpares, ao final do processo exiba em tela quantos
# números  ímpares  foram  encontrados  nesse  intervalo,  assim  como  a
# soma dos mesmos:

num = 1
listaDeNumeros = []

for i in range(100):
    if num % 2 == 0:
        num += 1
    else:
        listaDeNumeros.append(num)
        num += 1

print(listaDeNumeros)

# contador =  0
# soma =  0
 
# for  i  in   range ( 1 ,   101 ):
#    if  i %  3  ==  0 :
#     soma += i
#     contador +=  1
 
# print ( f 'Foram encontrados  { contador }  números ímpares.' )
# print ( f 'A soma destes números é:  { soma } !!!' )
 
 
# Para esse caso, novamente temos um problema envolvendo muito
# mais lógica do que estrutura de dados em si. Raciocine que ao mesmo
# tempo em que identificamos cada número ímpar precisamos o guardar em
# uma variável para que seja possível o usar na soma do total.
# Para isso criamos duas variáveis, uma para controle (contador) e
# uma que fará a soma dos elementos (soma), ambas inicialmente zeradas
# pois serão incrementadas a cada laço de repetição.
# Para o laço em si criamos um laço for que realiza a contagem de 1
# até 100, retornando essa contagem para a variável temporária i. Dentro do
# bloco de código do laço for criamos uma estrutura condicional onde se o
# módulo da divisão de i por 3 deve ser igual a 0. Sempre que essa condição
# for verdadeira, a variável soma é atualizada somando para si o valor de i,
# da mesma forma, a variável contador recebe o incremento em uma unidade.
# Por fim simplesmente exibimos em tela via função print( ) o que o
# enunciado da questão nos pede.
# O retorno será:
 
# Foram encontrados 33 números ímpares.
# A soma destes números é: 1683!!!

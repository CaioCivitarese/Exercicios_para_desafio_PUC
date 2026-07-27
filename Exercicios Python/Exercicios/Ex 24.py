# 24 - Crie duas variáveis com dois valores numéricos inteiros digitados
# pelo  usuário,  caso  o  valor  do  primeiro  número  for  maior  que  o  do
# segundo, exiba em tela uma mensagem de acordo, caso contrário, exiba
# em tela uma mensagem dizendo que o primeiro valor digitado é menor
# que o segundo:

num1 = int(input('Qual o primeiro valor: '))
num2 = int(input('Qual o segundo valor: '))

if num1 > num2:
    print('Correto')
elif num1 < num2:
    print('O primeiro valor e menor que o segundo valor!!!')

# num1 = int ( input ( 'Digite o primeiro número: ' ))
# num2 = int ( input ( 'Digite o segundo número: ' ))
 
# if  num1 > num2 :
#    print ( 'O primeiro número digitado é o maior!' )
# else :
#    print ( 'O segundo número digitado é o maior!' )
 
 
# Lembrando que em uma estrutura condicional simples, criamos um
# objetivo a ser alcançado/atingido, indentando blocos de código de acordo
# com as condições importas.
# Nesse caso, como temos apenas dois possíveis desfechos de acordo
# com a condição, supondo que o usuário digitou 25 e 26, respectivamente, o
# resultado exibido em tela seria ‘O segundo número digitado é o maior’,
# uma vez que a primeira condição (se num1 for maior que num2) não é
# válida.

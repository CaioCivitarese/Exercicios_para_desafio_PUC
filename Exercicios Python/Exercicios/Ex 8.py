# 8 - Peça para que o usuário digite um número, em seguida o converta
# para float, exibindo em tala tanto o número em si quanto seu tipo de
# dado.

num = int(input("Escreva um numero:"))
numfloat = float(num)

print(num, numfloat)

# num =  input ( 'Digite um número: ' )
# num = float ( num )
 
# print ( num )
# print ( type ( num ))
 
 
# Uma vez criada nossa variável num, com seu conteúdo vindo da
# interação  com  o  usuário,  podemos  atualizar  o  conteúdo  dessa  variável,
# mudando inclusive seu tipo de dado. Para isso, nossa variável num recebe
# como atributo o método float( ) parametrizado com ela mesma.
# Dessa forma, o conteúdo atribuído a variável num é convertido de
# formato e salvo sobrescrevendo o conteúdo antigo dessa variável. Por meio
# da função print( ) podemos exibir em tela tanto o tipo quanto o conteúdo da
# variável num.
# Supondo que o usuário tenha digitado 52, o retorno será:
 
# 52
# float

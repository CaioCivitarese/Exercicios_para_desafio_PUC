# Num dia quente de verão, Pete e seu amigo Billy decidiram comprar uma melancia. Escolheram a maior e a mais madura, na opinião deles.
# Depois, pesaram a melancia e a balança marcou w quilos. Correram para casa, morrendo de sede, e decidiram dividir a fruta, mas enfrentaram um grande problema.

# Pete e Billy adoram números pares, por isso querem dividir a melancia de forma que cada uma das duas partes pese um número par de quilos,
# embora não seja obrigatório que as partes tenham o mesmo peso. Os meninos estão muito cansados ​​e querem começar a comer logo,
# então você deve ajudá-los e descobrir se eles conseguem dividir a melancia do jeito que querem. Com certeza, cada um deles deve ficar com uma parte de peso positivo.

# Entrada
# A primeira (e única) linha de entrada contém o número inteiro w ( 1 ≤  w  ≤ 100 ) — o peso da melancia comprada pelos meninos.

# Saída
# Escreva SIM se os meninos conseguirem dividir a melancia em duas partes, cada uma pesando um número par de quilos; e NÃO caso contrário.

W = int(input())

if W / 2 == 1:
    print('NO')
elif W % 2 == 0:
    print('YES')
else:
    print('NO')

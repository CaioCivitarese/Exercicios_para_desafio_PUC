#  Média 7 ou mais: aprovado.
#  Média maior ou igual a 4 e menor que 7: recuperacao.
#  Média menor que 4: reprovado
#  se qualquer das duas notas for menor que 2, o aluno é reprovado direto

N1 = float(input())
N2 = float(input())

media = (N1 + N2) / 2

if (N1 < 2) or (N2 < 2):
    print('reprovado')
elif media >= 7:
    print('aprovado')
elif (media < 7) and (media >= 4):
    print('recuperacao')
elif media < 4:
    print('reprovado')

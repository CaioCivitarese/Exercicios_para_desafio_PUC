aluno1 = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a nota desse aluno: '))
nota2 = float(input('Digite a outra nota desse aluno: '))
nota3 = float(input('Digite a ultima nota desse aluno: '))

media_notas = (nota1 + nota2 + nota3) / 3

if media_notas >= 5.0:
    print("Aprovado")
else: 
    print('Reprovado')
print(media_notas)

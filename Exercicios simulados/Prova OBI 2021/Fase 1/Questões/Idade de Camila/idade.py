# Cibele > Camila > Celeste

idade1 = int(input('Qual a idade: '))
idade2 = int(input('Qual a idade: '))
idade3 = int(input('Qual a idade: '))

if idade1 > idade2 and idade1 < idade3:
    print(idade1)
elif idade2 > idade1 and idade2 < idade3:
    print(idade2)
elif idade3 > idade1 and idade3 < idade2:
    print(idade3)
else:
    print(idade1)

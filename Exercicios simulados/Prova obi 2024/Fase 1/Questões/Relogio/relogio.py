H = int(input('Quantas Horas: '))
M = int(input('Quantos Minutos: '))
S = int(input('Quantos Segundos: '))
T = int(input('Qual o tempo de atraso: '))

seg = S + T
min = M
hora = H

for c in range(seg):
    if seg >= 60:
        seg = seg - 60
        min = min + 1


if min >= 60:
    for c in range(min):
        if min >= 60:
            min = min - 60
            hora = hora + 1
            

if hora >= 24:
    for c in range(hora):
        if hora >= 24:
            hora = hora - 24

print(hora)
print(min)
print(seg)

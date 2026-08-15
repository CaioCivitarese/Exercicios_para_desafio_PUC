H = int(input('Quantas Horas: '))
M = int(input('Quantos Minutos: '))
S = int(input('Quantos Segundos: '))
T = int(input('Qual o tempo de atraso: '))

segundos = 0
seg = S + T
minutos = 0
min = 0
horas = 0
hor = 0

segundos = segundos + seg

if seg >= 60:
    segundos = seg % 60
    min = seg // 60 


minutos = min + M
min = minutos

if min >= 60:
    minutos = min % 60
    hor = min // 60 

horas = hor + H
hor = horas

if hor >= 24:
    horas = hor % 24

print(horas)
print(minutos)
print(segundos)

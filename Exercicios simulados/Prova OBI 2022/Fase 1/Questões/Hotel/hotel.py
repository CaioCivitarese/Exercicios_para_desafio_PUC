# D = dia 1 
# 30 x D = Preço para que chega no dia 1
# A = aumendo diario da diaria
# D + X x A = função do almento da diaria
# D = 16: a diaria não almenta mais

D = int(input('Qual o valor da diaria no dia 1: '))
A = int(input('Qual o almento diario: '))
N = int(input('Dia de chegado no hotel: '))

dia = 31 - N
almentoDia = 0
form = 0
dia1 = 0

for c in range(N):
    if dia < 1  and dia > 16:
        almentoDia = dia * A
        form = dia * (D + almentoDia)
    elif N > 15:
        almentoDia = 15 * A
        form = dia * (D + almentoDia) 
    else:
        form = dia * D


print(form)

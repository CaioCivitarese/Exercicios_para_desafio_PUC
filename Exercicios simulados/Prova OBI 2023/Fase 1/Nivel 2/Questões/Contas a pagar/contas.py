# V = Valor que tem disponivel
# A = Valor da conta do Açogue
# F = Valor da conta da Farmacia
# P = Valor da conta da Padaria

V = int(input('Qual o valor disponivel: '))
A = int(input('Qual o valor da conta do Açogue: '))
F = int(input('Qual o valor da conta da Farmacia: '))
P = int(input('Qual o valor da conta da Padaria: '))

listaTotal = [A, F, P]
listaTotal.sort()
N = 0
numerosDeContas = 0

while N < len(listaTotal) and V >= listaTotal[N]:
    V -= listaTotal[N]
    N += 1
    numerosDeContas += 1

print(numerosDeContas)

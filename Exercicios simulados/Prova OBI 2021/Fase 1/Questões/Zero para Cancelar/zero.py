# soma das sequencias so numeros

N = int(input('Quandos numeros serão: '))
X = 0
listaDeNumeros = []
for c in range(N):
    X = int(input('Qual e o numero: '))
    if X != 0:
        listaDeNumeros.append(X)
    else:
        listaDeNumeros.pop()

soma = sum(listaDeNumeros)

print(soma)
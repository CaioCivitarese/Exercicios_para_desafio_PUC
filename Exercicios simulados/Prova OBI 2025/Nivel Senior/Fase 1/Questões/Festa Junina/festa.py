# Roupas = loja do bairro
# ingredientes = supermercado 
# distacia em metros do inicio da rua
# distacia = predio1 - predio2

E = int(input('Localização da escola: '))
S = int(input('Localização do supermercado: '))
L = int(input('Localização da lojinha: '))

form = abs(E - S) + abs(S - L) + abs(L - E)

print(form)

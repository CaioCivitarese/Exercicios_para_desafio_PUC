# E = posição da escola
# S = posição do supermercado
# L = posição da lojinha

E = int(input("Qual a posição da escola: "))
S = int(input("Qual a posição do supermecado: "))
L = int(input("Qual a posição da lojinha: "))

escolaSuper = abs(E - S)
superLoja = abs(S - L)
lojaEscola = abs(L - E)    

result = escolaSuper + superLoja + lojaEscola

print(result)

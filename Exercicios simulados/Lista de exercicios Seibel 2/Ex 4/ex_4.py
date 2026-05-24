# Gerar e imprimir os números entre 1 e 100 que são múltiplos de 3 e de 5.
n = 0

while n < 100:
    if n % 3 == 0 and n % 5 == 0:
        print(n)
    
    n = n + 1



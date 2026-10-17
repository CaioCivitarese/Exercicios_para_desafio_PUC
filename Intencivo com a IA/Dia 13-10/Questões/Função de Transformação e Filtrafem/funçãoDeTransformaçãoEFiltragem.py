def processa_lista(lista, limite):
    listaFull = []

    for num in lista:
        if num > limite:
            if num % 2 == 0:
                listaFull.append(num * 2)
            else:
                listaFull.append(num)

    return listaFull

# Leitura dos dados de entrada (fora da função)
lista = list(map(int, input().split()))
limite = int(input())

# Chamada da função e impressão do retorno
resultado = processa_lista(lista, limite)
print(resultado)

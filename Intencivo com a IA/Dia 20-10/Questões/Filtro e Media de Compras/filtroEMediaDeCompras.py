# Crie uma função processa_compras(precos, limite) que recebe uma lista de preços (floats) e um valor limite (float). A função deve
# retornar uma tupla contendo: (1) uma nova lista com os preços estritamente maiores que o limite e (2) a média desses preços
# filtrados.
# Fora da função, leia a lista de preços na primeira linha (valores separados por espaço) e o limite na segunda linha. Imprima a lista
# resultante e a média com 2 casas decimais no formato MEDIA: X.XX. Se nenhum item for maior que o limite, imprima [] e MEDIA:
# 0.00.

def processa_compras(precos, limite):
    listaDePrecos = list(map(float, precos.split()))
    listaDePrecosAcima= [] 
    for i in range(len(listaDePrecos)):
        if listaDePrecos[i] > limite:
            listaDePrecosAcima.append(listaDePrecos[i])

    if len(listaDePrecosAcima) > 0:
        media = sum(listaDePrecosAcima) / len(listaDePrecosAcima)
    else:
        media = 0.0

    return listaDePrecosAcima, media

listaDePrecosAcima, media = processa_compras(input(), float(input()))

listaDePrecosAcimaFull = ' '.join(map(str, listaDePrecosAcima))

print('ITENS:', listaDePrecosAcimaFull)
print('MEDIA:', media)

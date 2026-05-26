def histograma(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
dicionario=histograma('banana')
print(dicionario)
dicionario=histograma('brontosaurus')
print(dicionario)


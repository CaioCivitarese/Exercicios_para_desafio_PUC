# Python != python
# Ver a palavar que aparece e contar quantas veses ele se repete.
# alterer a palavra que mais aparece por ([MAIS_FREQUENTE])

S = input()
Slist = list(map(str, S.split(' ')))
Slist2 = list(map(str, S))
maisSeRepete = max(Slist)
lista = []
listaDeAgrupamentos = []

for i in range(len(Slist2)):
    if Slist2[i - 1] == ' ':
        while Slist2[i] == ' ':
            listaDeAgrupamentos.append(Slist2[i])

        "".join(listaDeAgrupamentos)

        lista.append(listaDeAgrupamentos)
    else:
        lista.append(Slist2)

for i in range(len(lista)):
    if lista[i] == maisSeRepete:
        lista[i] = maisSeRepete

print(lista)

print(SlistFull)
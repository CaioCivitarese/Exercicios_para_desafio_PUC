# calcular o total de vogais presentes e gerar uma versão censurada do texto onde todas as vogais são substituídas pelo caractere '*'.
# Consideram-se vogais as letras 'a', 'e', 'i', 'o', 'u' (tanto minúsculas quanto maiúsculas).
# Espaços, pontuações e consoantes devem permanecer inalterados.

S = input()
Slista = list(map(str, S))
ListaDeVogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
FraseFinal = ""
N = 0

for i in range(len(Slista)):
    if Slista[i] in ListaDeVogais:
        FraseFinal += '*'
        N += 1
    else:
        FraseFinal += Slista[i]

print(N)
print(FraseFinal)

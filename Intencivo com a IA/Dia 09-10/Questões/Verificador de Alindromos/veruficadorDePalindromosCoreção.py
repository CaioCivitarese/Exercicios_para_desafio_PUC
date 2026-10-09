S = input()
Slista = list(map(str, S))

# 1. Trata os caracteres (converte maiúsculas e remove espaços)
Slista_limpa = []
for i in range(len(Slista)):
    if Slista[i] != ' ':
        if Slista[i].isupper() == True:
            Slista_limpa.append(Slista[i].lower())
        else:
            Slista_limpa.append(Slista[i])

# Atualiza a lista e calcula o tamanho final N
Slista = Slista_limpa
N = len(Slista)

lista1 = []

# 2. Cria a lista invertida (usando N - 1 - i para pegar do último ao primeiro)
for i in range(N):
    lista1.append(Slista[N - 1 - i])

# 3. Compara a lista invertida com a lista tratada
if lista1 == Slista:
    print('SIM')
else:
    print('NAO')
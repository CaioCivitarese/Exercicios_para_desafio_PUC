#OBI2024 fase2 ex1 - solução:
# os cubos internos não tem face preta e tem tamanho N-2 então (N-2)**3
# os cubos de fora que não são os das bordas e nem os dos cantos tem 1
#    face preta e são 6 faces, então 6*(N-2)**2
# os cubos das bordas que não são os dos cantos tem 2 faces pretas, e são
#   2 por face, então 12*(N-2)
# os cubos dos cantos, que são 8, tem 3 faces pretas

# Lê a dimensão N do cubo
N = int(input())

# Calcula as quantidades pedidas de acordo com as fórmulas
zero_faces = (N - 2) ** 3
uma_face = 6 * ((N - 2) ** 2)
duas_faces = 12 * (N - 2)
tres_faces = 8

# Imprime os resultados conforme a saída esperada
print(zero_faces)
print(uma_face)
print(duas_faces)
print(tres_faces)
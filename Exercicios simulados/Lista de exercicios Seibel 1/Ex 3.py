# Elaborar um programa para jogar “zero ou um” entre 3 jogadores. Ganha a partida o jogador
# que discordar. Ganha o jogo aquele que ganhar 10 partidas. Os valores (0 ou 1) devem ser
# gerados aleatoriamente (por exemplo gerando um número aleatório entre 1 e 100 e calculando
# o resto da divisão do número por 2, resultando em 0 ou 1). A saída deve ter o seguinte formato:
# Saida
# Partida1: Jogador1: 0 Jogador2: 1 Jogador3: 0 Jogador2 venceu a partida1
# Partida2: Jogador1: 1 Jogador2: 1 Jogador3: 0 Jogador3 venceu a partida2
import random
nv = 0

while nv != 10: 
    j1 = random.randint(0, 1)
    j2 = random.randint(0, 1)
    j3 = random.randint(0, 1)

    if j1 == j2 != j3:
        v = "O vencedor foi o jogador 3"
    elif j3 == j2 != j1:
        v = 'O vencedor foi o jogador 1'
    elif j1 == j3 != j2:
        v = 'O vencedor foi o jogador 2'
    else:
        v = 'Impate'

    print("Partida: jogador1:", j1, " jogador2:", j2, " jogador3:", j3, v)
    nv = nv + 1

# Elaborar um programa para jogar “zero ou um” entre 3 jogadores. Ganha a partida o jogador
# que discordar. Ganha o jogo aquele que ganhar 10 partidas. Os valores (0 ou 1) devem ser
# gerados aleatoriamente (por exemplo gerando um número aleatório entre 1 e 100 e calculando
# o resto da divisão do número por 2, resultando em 0 ou 1). A saída deve ter o seguinte formato:
# Saida
# Partida1: Jogador1: 0 Jogador2: 1 Jogador3: 0 Jogador2 venceu a partida1
# Partida2: Jogador1: 1 Jogador2: 1 Jogador3: 0 Jogador3 venceu a partida2
import random
nv = 0
nv1 = 0
nv2 = 0
nv3 = 0
nv4 = 0

while nv < 10: 
    j1 = random.randint(0, 1)
    j2 = random.randint(0, 1)
    j3 = random.randint(0, 1)

    if j1 == j2 != j3:
        v = "O vencedor foi o jogador 3"
        nv3 = nv3 + 1
    elif j3 == j2 != j1:
        v = 'O vencedor foi o jogador 1'
        nv1 = nv1 + 1
    elif j1 == j3 != j2:
        v = 'O vencedor foi o jogador 2'
        nv2 = nv2 + 1
    else:
        v = 'Empate'
        nv4 = nv4 + 1

    print("Partida: jogador1:", j1, " jogador2:", j2, " jogador3:", j3, v)
    nv = nv + 1

if nv1 > nv2 and nv1 > nv3 and nv1 > nv4:
    print('Jogador 1 foi o ganhador!!!')
elif nv2 > nv1 and nv2 > nv3 and nv2 > nv4:
    print('Jogador 2 foi o ganhador!!!')
elif nv3 > nv1 and nv3 > nv2 and nv3 > nv4:
    print('Jogador 3 foi o ganhador!!!')
else:
    print('Empate ganhou!!!')
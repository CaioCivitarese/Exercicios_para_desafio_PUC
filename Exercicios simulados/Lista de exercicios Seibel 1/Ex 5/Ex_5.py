# Escreva um programa em Python que implemente o jogo conhecido como “pedra, papel,
# tesoura”. Neste jogo, o usuário e o computador escolhem entre pedra, papel ou tesoura.
# Sabendo que pedra ganha de tesoura, papel ganha de pedra e tesoura ganha de papel, exiba na
# tela o ganhador: usuário ou computador. Para esta implementação, assuma que o número 1
# representa pedra, 2 representa papel e 3 representa tesoura. O programa deve pedir para ousuário entrar com sua escolha, gerar aleatoriamente a escolha do computador, exibir a escolha
# do computador e indicar o vencedor.
# Não se esqueça de colocar mensagens na tela para instruir o usuário, e faça uma saída textual
# que indique a opção “PEDRA”, “PAPEL” ou “TESOURA” de cada participante (usuário e
# computador), revelando o ganhador.
# Um exemplo de execução de um código é ilustrado abaixo:
# Entre com sua escolha 1 (pedra), 2 (papel) ou 3 (tesoura): 2
# Escolha do computador: 1
# Usuário: PAPEL Computador: PEDRA
# Usuário ganhou!
import random

escolha_usuario = input('Você que pedra papel ou tesoura (escreva tudo em minusculo): ')
escolhas_computador = ['pedra', 'papel', 'tesoura']
escolha_aleatotia = random.choice(escolhas_computador)

if escolha_aleatotia == 'pedra' and escolha_usuario == 'tesoura':
    print('O coputador escolheu: ', escolha_aleatotia)
    print('O coputador venceu!!!')

elif escolha_aleatotia == 'papel' and escolha_usuario == 'pedra':
    print('O coputador escolheu: ', escolha_aleatotia)
    print('O coputador venceu!!!')

elif escolha_aleatotia == 'tesoura' and escolha_usuario == 'papel':
    print('O coputador escolheu: ', escolha_aleatotia)
    print('O coputador venceu!!!')
    
elif escolha_aleatotia == 'tesoura' and escolha_usuario == 'pedra':
    print('O coputador escolheu: ', escolha_aleatotia)
    print('Você venceu!!!')

elif escolha_aleatotia == 'papel' and escolha_usuario == 'pedra':
    print('O coputador escolheu: ', escolha_aleatotia)
    print('Você venceu!!!')

elif escolha_aleatotia == 'pedra' and escolha_usuario == 'papel':
    print('O coputador escolheu: ', escolha_aleatotia)
    print('Você venceu!!!')
else:
    print('O coputador escolheu: ', escolha_aleatotia)
    print('Deu empate!!!')

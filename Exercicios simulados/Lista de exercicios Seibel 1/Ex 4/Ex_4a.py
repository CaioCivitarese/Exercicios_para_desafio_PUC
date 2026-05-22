# Implemente um jogo de adivinhação. O computador “escolhe” (gera aleatoriamente) um
# número entre 1 e 1023, e o usuário tenta adivinhar o número escolhido. Para cada tentativa do
# usuário, o programa deve exibir na tela:
# • o número -1, se o número gerado for menor do que o número fornecido pelo usuário;
# • o número 1, se o número gerado for maior do que o número fornecido pelo usuário;
# • o número 0, se o número gerado for igual ao fornecido pelo usuário. Neste caso, o programa
# deve exibir o número de tentativas usadas pelo usuário para acertar a escolha do computador e
# finalizar a execução.
# Implemente e teste este jogo.
import random
def tentativas_usuario():
    sorte_num = random.randint(1, 1023)
    tentativa = 0
    tentativas = 0

    while tentativa != sorte_num:
        
        tentativa = int(input('Escolha um numero: '))
        tentativas = tentativas + 1
        if tentativa < sorte_num:
            print(-1)
        elif tentativa > sorte_num:
            print(1)
        else:
            print(0)
            print('Você acertou em {} tentativas'.format(tentativas))
    return        

tentativas_usuario()

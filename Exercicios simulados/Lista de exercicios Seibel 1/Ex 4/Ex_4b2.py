import random
def tentativas_computador():
    sorte_num = random.randint(1, 1023)
    tentativa = 1
    tentativas = 0

    while tentativa != sorte_num:

        tentativas = tentativas + 1

        if tentativa < sorte_num:
            print(-1)

        elif tentativa > sorte_num:
            print(1)
        else:
            print(0)
            print('Você acertou em {} tentativas'.format(tentativas))
            
print(tentativas_computador())
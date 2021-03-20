from random import randint
    print ('Bem vindo!')
    sorteado = randint(1, 100)
    chute = 0

    while chute != sorteado:
    chute = int(input ('Chute: '))
    if chute == sorteado:
        print ('Você venceu!')
    if chute > sorteado:
        print ('Menor')
    if chute < sorteado:
        print ('Maior')

print ('Fim do jogo!')

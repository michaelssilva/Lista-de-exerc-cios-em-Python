minutos = int(input('Digite o número de minutos: '))

if minutos > 200:
    preço =  0.20
    
else:
    if minutos <= 400:
        preço = 0.18
    else:
        preço = 0.15

print (f'R$ {preço*minutos:.2f}')

    

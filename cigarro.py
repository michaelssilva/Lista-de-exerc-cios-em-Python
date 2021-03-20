a = int(input('Quantos anos voce fuma: '))
c = int(input('Quantos cigarros fuma por dia: '))

mp = c * (365 * a)
dp =mp / 144

print (f'Você perdeu {dp: .2f} dias de vida')

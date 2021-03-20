v= int(input('digite a velociade do seu carro: '))
 
if v > 110:
    print ('Você foi multado!')
    multa = (v - 110) * 5
    print (f'Valor da multa: R$ {multa:.2f}')

else:
    print ('Você não foi multado! ')

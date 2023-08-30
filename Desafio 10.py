real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real / 4.86
euro = real / 5.32
print ('Com R${:.2f} voce pode comprar US${:.2f}'.format (real, dolar))
print ( 'Com R${:.2f} voce pode comprar EUR ${:.2f}'.format (real, euro))

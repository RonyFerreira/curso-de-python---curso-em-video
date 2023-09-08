#crie um programa que leia qquanto dinheiro
#uma pessoa tem na carteira e mostre quantos
#dolares ela pode comprar


real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.99
print('Com {} R$ você pode comprar {:.2f} US$'.format(real, dolar))

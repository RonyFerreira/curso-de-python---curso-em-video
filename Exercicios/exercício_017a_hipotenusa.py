from math import hypot
cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateto adjacente: '))
print('O valor da hipotenusa é {:.2f} '.format(hypot(cat_op, cat_adj)))


#ainda poderiamos ter criado uma variável "hi = hypot(cat_op, cat_adj)"
#e no print colocar apenas ".format(hi)"

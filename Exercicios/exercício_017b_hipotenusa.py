cat_op = float(input('Digite o commprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateto adjacente: '))
hip = (cat_op ** 2 + cat_adj ** 2) ** (1/2)
print('A hipotenusa vai medir {} '.format(hip))



#a soma dos quadrados dos catetos é = a porra da hipotenusa
#hipotenusa é a raiz quadrada da soma dos quadrados dos catetos
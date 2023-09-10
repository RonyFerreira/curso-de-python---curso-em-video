from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e seu valor inteiro é {} '.format(num, trunc(num))) 


#para números inteiros poderiamos usar a função int
#.format(num, int(num)) sem necessidade de importar nada
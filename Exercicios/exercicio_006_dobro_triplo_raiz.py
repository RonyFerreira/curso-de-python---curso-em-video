#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada


n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.'.format(n, t))
print('A raiz quadrada de {} vale {:.2f}.'.format(n, r))      #a formatação ':.2f' dentro das chaves serve para mostrar apenas dois números após a virgula


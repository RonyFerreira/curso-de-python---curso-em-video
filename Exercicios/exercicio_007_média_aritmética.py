#desenvolva um programa que leia as duas notas de um aluno e calcule e mostre sua média


n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1+n2) / 2
print('A média entre {} e {} é {}.'.format(n1, n2, m))

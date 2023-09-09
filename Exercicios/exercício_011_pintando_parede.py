#faça um programa que leia a largura e a altura de uma parede
#em metros, calcule a sua área e a quantidade necessária para
#pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadadros


larg = float(input('Qual é a largura da parede? '))
alt = float(input('Qual é a altura da parede? '))
área = larg * alt
print('A sua parede tem {} x {} e, a sua área é {:.2}m2 '.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede você vai precisar de {}l de tinta '.format(tinta))


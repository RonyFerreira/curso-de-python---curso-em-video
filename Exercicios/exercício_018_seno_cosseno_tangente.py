#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 
import math
ang = float(input('Qual é o ângulo desejado: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O valor do seno é {:.2f} '.format(sen))
print('O valor do cosseno é {:.2} '.format(cos))
print('O valor da tangente é {:.2f} '.format(tan))
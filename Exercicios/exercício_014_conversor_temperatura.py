#escreva um programa qque converta
#uma temperatura digitada em graus celsius
#e converta para graus Fahrenheit


c = float(input('Qual é a temperatura em °C?: '))
F = ((9 * c) / 5) + 32
print('A temperatura de {}°C corresponde a {}°F.'.format(c, F))

#Escreva um programa qque pergunte a quantidade de KM
#percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que, 
#o carro custa R$60 por dia e R%0,15 por KM rodado


km = float(input('Quantos kms o carro percorreu? '))
d = int(input('Quantos dias o carro foi alugado? '))
v = float(input(km * 0,15 + 60 * d))
print('O aluguel do carro que percorreu {}km com um total de {} dias, custará {} '.format(k, d, v))

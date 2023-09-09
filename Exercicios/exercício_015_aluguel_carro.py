#Escreva um programa qque pergunte a quantidade de KM
#percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que, 
#o carro custa R$60 por dia e R%0,15 por KM rodado


d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos kms o carro percorreu? '))
v_d = d * 60 + km * 0.15
print('O valor do aluguel é de R${:.2f}.'.format(v_d))


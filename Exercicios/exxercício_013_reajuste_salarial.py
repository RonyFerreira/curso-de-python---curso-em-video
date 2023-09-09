#Faça um algoritmo que leia o salário de um 
#funcionário e mostre seu novo salário,
#com 15% de aumento


salário = float(input('Qual é o seu salário? R$'))
novo_salário = salário + (salário * 15 / 100)
print('O seu salário de R${:.3f}, com o aumento de 15% passou a ser de R${:.3f}'.format(salário, novo_salário))

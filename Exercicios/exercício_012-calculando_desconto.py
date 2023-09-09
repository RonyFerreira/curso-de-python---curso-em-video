#faça um algoritmo qque leia o preço de um produto
#e mostre o seu novo preço com 5% de desconto


preço = float(input('Qual é o preço do produto? R$'))
novo_preço = preço - (preço * 5 / 100)
print('O produto que custava {}, com 5% de desconto passará a custar {:.2f} '.format(preço, novo_preço))

#Escreva um programa que leia um valor em metros e exiba
# convertido em centimetros e milimetros

medida = float(input('Digite uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}cm e {}mm. '.format(medida, cm, mm))


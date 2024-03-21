# Escreva um programa que calcule e escreva o valor total da compra
quantidades_macas = int(input('Quantas maçãs irá levar hoje ? '))
if quantidades_macas < 12:
    valor_maca = 0.3
else:
    valor_maca = 0.25
calculo = quantidades_macas * valor_maca
print(f'O total, por {quantidades_macas} maçãs, foi de: R${calculo}')

# Escreva um programa para informar qual é o polígono e sua área
poligono = input('Quantos lados tem seu polígono ? ')
medida_lado = float(input('Quanto mede, em cm, os lados do seu polígono ? '))
if poligono == '3':
    area = ((medida_lado ** 2) * (3 ** 1 / 2)) / 2
elif poligono == '4':
    area = medida_lado ** 2
elif poligono == '5':
    area = ((3 * (medida_lado ** 2)) * (3 ** 1 / 2)) / 2
print(f'A área do seu polígono é de: {area} cm')

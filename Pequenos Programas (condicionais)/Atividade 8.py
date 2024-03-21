# Complemento da "Atividade 7"
poligono = int(input('Quantos lados tem seu polígono ? '))
if poligono < 3:
    print('Não é um polígono')
elif poligono > 5:
    print('Polígono não identificado')
else:
    medida_lado = float(input('Quanto mede, em cm, os lados do seu polígono ? '))
    if poligono == 3:
        area = ((medida_lado ** 2) * (3 ** 1 / 2)) / 2
        poligono = 'triângulo'
    elif poligono == 4:
        area = medida_lado ** 2
        poligono = 'quadrado'
    elif poligono == 5:
        area = ((3 * (medida_lado ** 2)) * (3 ** 1 / 2)) / 2
        poligono = 'pentagono'
    print(f'A área do seu {poligono} é de: {area} cm²')

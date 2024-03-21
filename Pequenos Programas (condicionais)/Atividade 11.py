# Escreva um programa que diga o tipo de um triângulo (pela medida dos ângulos)
med1 = float(input('Diga, em graus ("˚"), a medida de um dos ângulos do triângulo: '))
med2 = float(input('Diga, em graus ("˚"), a medida de outro dos ângulos do triângulo: '))
med3 = float(input('Diga, em graus ("˚"), a medida do último dos ângulos do triângulo: '))
pos = (med1 + med2 + med3)
req = (med1 != 0 or med2 != 0 or med3 != 0)
if pos == 180 and req:
    if (med1 or med2 or med3) > 90:
        tri = 'Obtusângulo'
    elif (med1 or med2 or med3) == 90:
        tri = 'Retângulo'
    elif (med1 or med2 or med3) < 90:
        tri = 'Acutângulo'
else:
    tri = 'Impossível, suas medidas não satisfazem a lei de "formação triangular"'
print(f'O tipo do seu triângulo é: {tri}')

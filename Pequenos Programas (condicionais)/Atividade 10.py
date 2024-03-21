# Escreva um programa que diga o tipo de um triângulo (pela mediada dos lados)
med1 = float(input('Diga, em cm, a medida de um dos lados do triângulo: '))
med2 = float(input('Diga, em cm, a medida de outro dos lados do triângulo: '))
med3 = float(input('Diga, em cm, a medida do último dos lados do triângulo: '))
pos = ()
if (pos == med1 + med2 > med3 or pos == med2 + med3 > med1 or pos == med3 + med1 > med2 or
        pos == med1 <= 0 or pos == med2 <= 0 or pos == med3 <= 0):
    if med1 == med2 == med3:
        tri = 'Equilátero'
    elif med1 == med2 or med1 == med3 or med2 == med3:
        tri = 'Isósceles'
    else:
        tri = 'Escaleno'
else:
    tri = 'Impossível, suas medidas não satisfazem a lei de "desigualdade triangular"'
print(f'O tipo do seu triângulo é: {tri}')

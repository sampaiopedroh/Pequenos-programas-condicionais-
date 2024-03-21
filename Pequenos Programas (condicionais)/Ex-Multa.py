"""Limite = 100
faixa1 100-120 = 20%
faixa2 120-150 = 30%
faixa3 150-... = 40%
*Acumulativo*"""
v = int(input('Qual a velociade (em Km/h) ? '))
if v <= 100:
    mul = 0
elif v <= 120:
    mul = 0.2 * v
elif v <= 150:
    mul = 24 + v * 0.3
else:
    mul = 69 + v * 0.4
print(f'O valor da multa a ser pago é: R${mul}')

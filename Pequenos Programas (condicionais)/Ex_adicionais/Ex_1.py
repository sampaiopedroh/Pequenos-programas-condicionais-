# Verificar o maior de três n˚
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
if num1 > num2 and num1 > num3:
    num1 = num1
elif num2 > num3:
    num1 = num2
else:
    num1 = num3
print(f'O maior número é: {num1}')

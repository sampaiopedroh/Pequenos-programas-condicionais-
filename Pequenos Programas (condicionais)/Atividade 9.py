# Escreva um programa para escrever o maior entre 3 valore (sem valores iguais)
"""a = float(input('Digite um número: '))
b = float(input('Digite um número diferente: '))
c = float(input('Digite um número diferente dos outros dois: '))
if a > b and a > c:
    a = a
elif b > c:
    a = b
else:
    a = c
print(a)"""

# Melhorado
qnt = int(input('Quantos números serão comparados ? '))
vezes = 0
num = 0
maior = ''
while vezes < qnt:
    vezes += 1
    num = float(input(f'Digite o {vezes}° número: '))
    if num > num:
        maior = num
    else:
        maior = num
print(f'O maior número é: {maior}')

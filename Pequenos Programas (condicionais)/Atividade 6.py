# Construa um programa que calcule e imprima seu peso ideal
altura = (float(input('Qual a sua altura ? ')))
sexo = input('Qual o seu sexo, sendo'
             '\n"1" para sexo feminino'
             '\n"2" para sexo masculino'
             '\nResposta: ')
if sexo == '1':
    calculo = (altura * 62.1) - 44.7
    print(f'Seu peso ideal é: {calculo}')
elif sexo == '2':
    calculo = (altura * 72.7) - 58
    print(f'Seu peso ideal é: {calculo}')

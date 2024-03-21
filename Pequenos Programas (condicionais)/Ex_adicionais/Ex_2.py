# Calculadora de IMC
peso = float(input('Qual o seu peso (em "Kg") ? '))
altura = float(input('qual a sua altura (em "m") ? '))
cal = peso / (altura ** 2)
if cal <= 18.5:
    retorno = 'Abaixo do peso'
elif 18.5 < cal <= 24.9:
    retorno = 'Peso normal'
elif 24.9 < cal <= 29.9:
    retorno = 'Sobrepeso'
elif 29.9 < cal <= 34.9:
    retorno = 'Obesidade grau 1'
elif 34.9 < cal <= 39.9:
    retorno = 'Obesidade grau 2'
else:
    retorno = 'Obesidade grau 3'
print(f'A sua situação é: {retorno}.\n'
      f'O calculo do seu IMC é:', round(cal, 2))
# "round(var, 'qnt_casas_deci')" determina a qnt de casas decimais

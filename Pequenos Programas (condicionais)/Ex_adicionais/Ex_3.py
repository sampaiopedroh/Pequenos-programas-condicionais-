# Conversor de temperatura
uni_med = int(input('1 para ˚Fahrenheit\n'
                    '2 para ˚Celcius.\n'
                    'Qual será a unidade de medida ? '))
if uni_med == 1:
    uni_i = 'Fahrenheit'
    uni_f = 'Celcius'
    temp = int(input('Quantos graus ˚Fahrenheit deseja converter para ˚Celcius ? '))
    cal = (temp - 32) * (5/9)
elif uni_med == 2:
    uni_i = 'Celsius'
    uni_f = 'Fahrenheit'
    temp = int(input('Quantos graus ˚Celsius deseja converter para ˚Fahrenheit ? '))
    cal = (temp * 9/5) + 32
else:
    print('O valor selecionado não condiz com as opções ')
print(f'A conversão de {temp}˚ {uni_i} para ˚{uni_f} dá', round(cal, 2),f'˚{uni_f}')

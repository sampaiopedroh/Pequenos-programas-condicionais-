# Escreva um programa para ver se uma pessoa pode votar este ano e diga se pode ou não
ano_nascimento = int(input('E que ano você nasceu? '))
if 150 > (2024 - ano_nascimento) >= 16:
    print('Pode vota')
elif 150 < (2024 - ano_nascimento) or 0 > (2024 - ano_nascimento):
    per = input('Tem certeza que essa é sua idade (Y/N) ? ')
    if per == 'Y':
        print(f'Deixa de brincadeira, ninguém está vivo desde {ano_nascimento}')
    elif per == 'N':
        print('Reinicie o programa e coloque seu ano de nascimento real')

else:
    print('Não pode vota')

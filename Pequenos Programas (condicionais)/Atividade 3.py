# Escreva um programa que verifique a validade de uma senha fornecida pelo usuário
"""user = input('Usuário: ')
senha = input('Senha: ')
if senha == '1234':
    print('ACESSO PERMITIDO')
else:
    print('ACESSO NEGADO')"""

# Melhorado
"""user = input('Digite seu usuário: ')
senha = input('Sigite sua senha: ')
tentativas = 0
while senha != '1234' and tentativas < 2:
    senha = input('Senha incorreta, tente novamente: ')
    tentativas += 1

if senha == '1234':
    print(f'Acesso concedido.'
          f'\nBem vindo, {user} !')
else:
    print('Multiplas tentativas incorretas.'
          '\nAcesso bloqueado !')"""

# Melhor ainda
user = input('Digite seu usuário: ')
senha = input('Sigite sua senha: ')
tentativas = 0
while senha != '1234' and tentativas < 2:
    senha = input('Senha incorreta, tente novamente: ')
    tentativas += 1

if senha == '1234':
    import string
    import time

    texto = f'Acesso concedido.' \
            f'\nBem vindo, {user} !'
    temp = ''
    for ch in texto:
        for i in string.printable:
            if i == ch or ch == i:
                time.sleep(0.02)
                print(temp + i)
                temp += ch
                break
            else:
                time.sleep(0.02)
                print(temp + i)
else:
    print('Multiplas tentativas incorretas.'
          '\nAcesso bloqueado !')
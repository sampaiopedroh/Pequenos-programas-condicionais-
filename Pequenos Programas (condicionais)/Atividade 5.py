# ***Escreva um programa para ler 3 valores inteiros e escrevê-los em ordem crescente (sem valores iguais)***
a = float(input('Digite um número: '))
b = float(input('Digite um número diferente: '))
c = float(input('Digite um número diferente dos outros dois: '))
# tornar o maior númeno em "c"
# verifica se "a" é o maior de todos
if a > b and a > c:
    # "c" recebe o valor de "a"
    aux = a
    a = c
    c = aux
# se "a" não é o maior de todos, então ou "b" ou "c" é o maior
elif b > c:
    # "c" recebe o valor de "b"
    aux = b
    b = c
    c = aux
    # se não, "c" se mantém
# agora "c" (antigo "a" ou "b" ou o atual "c") é o maior, então temos que saber quem é o maior entre o "a" e "b" atuais
if a > b:
    # "b" recebe o valor de "a"
    aux = a
    a = b
    b = aux
    # se não, "a" se mantém
print(f'{a}, {b} e {c}')

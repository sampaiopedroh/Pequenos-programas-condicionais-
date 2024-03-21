# Jogo da adivinhação
num_certo = 89
num_per = int(input('Adivinhe o número: '))
if num_per > num_certo:
    print('Um pouco menos')
elif num_per < num_certo:
    print('Um pouco mais')
else:
    print('Acertou, parabéns !!!')

# Com while
# num_certo = 89
# num_per = int(input('Adivinhe o número: '))
# while num_per != num_certo:
#     if num_per > num_certo:
#         print('Um pouco menos')
#         num_per = int(input('Tente denovo: '))
#     else:
#         print('Um pouco mais')
#         num_per = int(input('Tente denovo: '))
# print('Acertou, parabéns !!!')

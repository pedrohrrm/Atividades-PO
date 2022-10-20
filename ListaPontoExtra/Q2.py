# Questão 2
from random import randint

preto = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
vermelho = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

numSelecionado = randint(1, 38)
print('O resultado da rodada é {0}'.format(numSelecionado))
if numSelecionado == 38:
    print('Pagar 00.')
elif numSelecionado == 37:
    print('Pagar 0.')
else:
    print('pagar {0}'.format(numSelecionado))
if numSelecionado in vermelho:
    print('Pagar vermelho.')
elif numSelecionado in preto:
    print('Pagar preto.')
if numSelecionado % 2 == 0:
    print('Pagar par.')
else:
    print('Pagar ímpar.')
if numSelecionado <= 18:
    print('Pagar 1 a 18')
elif numSelecionado > 18 and numSelecionado <= 36:
    print('Pagar 19 a 36.')

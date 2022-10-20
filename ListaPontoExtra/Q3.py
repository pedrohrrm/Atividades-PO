# Questão 3 
from random import randint

colecaoInt = randint(1, 100)
nVezes = 0
print('Número selecionado da coleção de inteiros: {0}'.format(colecaoInt))
for c in range(1, 100):
    nAtual = randint(1, 100)
    print(nAtual)
    if nAtual > colecaoInt:
        colecaoInt = nAtual
        print('{0} atualizado.'.format(colecaoInt))
        nVezes += 1
print('O valor máx encontrado foi: {0}'.format(colecaoInt))
print(
    'O número máx de vezes que o maior valor foi atulizado foi {0} vezes'.format(nVezes))

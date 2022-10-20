# Questão 8
pontos = {'a': 1, 'e': 1, 'i': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1,
          'd': 2, 'g': 2, 'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4, 'v': 4, 'w': 4,
          'y': 4, 'k': 5, 'j': 8, 'x': 8, 'q': 10, 'z': 10}

palavra = input('Escreva uma palavra para saber quantos pontos ela vale:').swapcase()
caracteres = list(palavra)
total = 0
for i in range(0, len(caracteres)):
    if caracteres[i] in pontos:
        total += pontos.get(caracteres[i])

print(f'O total é {total}')

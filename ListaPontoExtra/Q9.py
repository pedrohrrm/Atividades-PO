# Questão 9
def lerArquivo(name):

    c = 1
    has_function = False
    try:
        arquivo = open(name,'r')

    except FileNotFoundError:
        return (f'não existe arquivo com o nome {name}')

    else:
        for line in arquivo:
            values = list(line)
            if ''.join(values[:3]) == 'def':
                has_function = True
                function_name = ''.join(values[4:line.find('(')])
                return (f'no arquivo {name}, a linha {c} contém uma função e o nome dela é {function_name}')
            c += 1
        if has_function == False:
            return (f'o arquivo {name} possui nenhuma função')
        arquivo.close()


qtd = int(input('Quantos arquivos você gostaria de ler? '))
if qtd == 1:
    name = input('Escreva o nome do arquivo: ')
    print(lerArquivo(name))
else:
    name = list()
    for c in range(1, qtd+1):
        aux = input(f'insira o {c}º nome do arquivo: ')
        name.append(aux)
    for i in range(0, len(name)):
        print(lerArquivo(name[i]))

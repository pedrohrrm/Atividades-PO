# Questão 7
def crivoErastostenes():
    limite = int(input("Digite o limite do intervarlo  "))
    numeros = []
    for i in range(limite+1):
        numeros.append(True)

    for j in range(2, int(len(numeros)/2)):
        for c in range(2*j, len(numeros), j):
            if numeros[c] == True:
                numeros[c] = False

    for n in range(len(numeros)):
        if n >= 2:
            if numeros[n] == True:
                print(n)


print(crivoErastostenes())

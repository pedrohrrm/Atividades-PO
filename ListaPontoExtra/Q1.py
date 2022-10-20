# Questão 1
n1 = int(input('Digite quantos pães você está comprando:'))
dor = float(4.60*(60/100))
pao = 4.60
n2 = float(pao-dor)*n1
n3 = float(n1*dor)
print('O valor do pão do dia é: {0:.2f}. Comprando pão dormido, você terá um desconto total de {1:.2f} e pagará na sua compra o total de: {2:.2f}'.format(
    pao, n2, n3))

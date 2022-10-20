# Questão 5
from calendar import monthrange, isleap

anoEscolhido = int(input("digite o ano escolhido : "))
mesEscolhido = int(input("digite o mes escolhido : "))

def diasMes(year, month):
    if isleap(year):
        return (f'{year} é bissexto, {monthrange(year, month)}')
    else:
        return (f'{year} não é bissexto {monthrange(year, month)}')

print(diasMes(anoEscolhido, mesEscolhido))

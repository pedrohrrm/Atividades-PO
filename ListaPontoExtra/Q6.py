# Questão 6
from calendar import monthrange


def AnoMAGICO(dia, mes, ano):
    if dia*mes == int(ano[2:]):
        print(f' A data {dia}/{mes}/{ano} é mágica ')
    else:
        print(f'A data {dia}/{mes}/{ano} não é mágica ')
        ano_atual = 1900
    while ano_atual <= 1999:
        mes_atual = 1
        while mes_atual <= 12:
            dias_totais = monthrange(ano_atual, mes_atual)
            for i in range(1, dias_totais[1]):
                novo_ano_atual = str(ano_atual)
                if i * mes_atual == int(novo_ano_atual[2:]):
                    print(f'A data {i}/{mes_atual}/{novo_ano_atual} é mágica ')
            mes_atual += 1
        ano_atual += 1


dia = int(input('digite o dia  '))
mes = int(input('digite o mês  '))
ano = input('digite o ano  ')
print(AnoMAGICO(dia, mes, ano))

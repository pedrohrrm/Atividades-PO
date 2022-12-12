
from scipy.optimize import linprog

lucroSapatoOuCinto = [-5, -2] #Coloca negativo para o scipy conseguir maximizar.
#ele só trabalha com minimização;

quantidadeProduzirUmaUnidade = [[2, 1],  # Unidades de couro
                                [10, 12]]  # Tempo gasto para produção.

totalDeCadaItem = [6, 60]  # total de couro e minutos disponíveis.

opt = linprog(
    c=lucroSapatoOuCinto,
    A_ub=quantidadeProduzirUmaUnidade,
    b_ub=totalDeCadaItem,
    method="revised simplex"
)
print(opt)

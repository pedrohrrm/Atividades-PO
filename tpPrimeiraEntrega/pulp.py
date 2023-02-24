from pulp import *

prob = LpProblem("Exemplo de Problema de Otimização", LpMaximize)

x = LpVariable("x", 0, None, LpContinuous)
y = LpVariable("y", 0, None, LpContinuous)

prob += 2 * x + 3 * y

prob += x + y <= 4
prob += 2 * x + y <= 6

status = prob.solve()
print("Status da Otimização:", LpStatus[status])
print("Valor Ótimo:", value(prob.objective))
print("Valor de x:", x.varValue)
print("Valor de y:", y.varValue)

from pulp import *

# Cria o modelo
model = LpProblem("Minimizar as distâncias de transporte", LpMinimize)

# Define as variáveis de decisão
x1 = LpVariable("x1", 0, None, LpInteger) # número de viagens de P1 para L1
x2 = LpVariable("x2", 0, None, LpInteger) # número de viagens de P2 para L1
x3 = LpVariable("x3", 0, None, LpInteger) # número de viagens de P3 para L1
x4 = LpVariable("x4", 0, None, LpInteger) # número de viagens de P1 para L2
x5 = LpVariable("x5", 0, None, LpInteger) # número de viagens de P2 para L2
x6 = LpVariable("x6", 0, None, LpInteger) # número de viagens de P3 para L2
x7 = LpVariable("x7", 0, None, LpInteger) # número de viagens de P1 para L3
x8 = LpVariable("x8", 0, None, LpInteger) # número de viagens de P2 para L3
x9 = LpVariable("x9", 0, None, LpInteger) # número de viagens de P3 para L3
x10 = LpVariable("x10", 0, None, LpInteger) # número de viagens de P1 para L4
x11 = LpVariable("x11", 0, None, LpInteger) # número de viagens de P2 para L4
x12 = LpVariable("x12", 0, None, LpInteger) # número de viagens de P3 para L4

# Define a função objetivo
model += 30 * x1 + 12 * x2 + 8 * x3 + 30 * x4 + 36 * x5 + 15 * x6 + 24 * x7 + 30 * x8 + 25 * x9 + 18 * x10 + 24 * x11 + 20 * x12, "Minimize transport distances"

# Adiciona as restrições
model += x1 + x2 + x3 == 50 / 10, "L1 fornece"
model += x4 + x5 + x6 == 80 / 10, "L2 fornece"
model += x7 + x8 + x9 == 40 / 10, "L3 fornece"
model += x10 + x11 + x12 == 100 / 10, "L4 fornece"

# Resolve o modelo
model.solve()

# Imprime o resultado
print("--- Solucao ---")
print("x1 = ", x1.varValue)
print("x2 = ", x2.varValue)
print("x3 = ", x3.varValue)
print("x4 = ", x4.varValue)
print("x5 = ", x5.varValue)
print("x6 = ", x6.varValue)
print("x7 = ", x7.varValue)
print("x8 = ", x8.varValue)
print("x9 = ", x9.varValue)
print("x10 = ", x10.varValue)
print("x11 = ", x11.varValue)
print("x12 = ", x12.varValue)
print("Objetivo = ", value(model.objective))

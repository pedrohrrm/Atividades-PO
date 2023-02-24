from pulp import *
baterias = ["VTC5A", "HG2", "25R"]
fornecedores = [1, 2, 3]

# Variáveis de decisão
x = LpVariable.dicts("x", (baterias, fornecedores), lowBound=0)
prob = LpProblem("Minimizar_Custo_Total_Frete", LpMinimize)
# Parâmetros
di = {"VTC5A": 100, "HG2": 80, "25R": 120}
fi = {("VTC5A", 1): 10, ("VTC5A", 2): 8, ("VTC5A", 3): 12,
      ("HG2", 1): 9, ("HG2", 2): 7, ("HG2", 3): 11,
      ("25R", 1): 8, ("25R", 2): 6, ("25R", 3): 10}
cij = {("VTC5A", 1): 150, ("VTC5A", 2): 140, ("VTC5A", 3): 130,
       ("HG2", 1): 160, ("HG2", 2): 150, ("HG2", 3): 140,
       ("25R", 1): 170, ("25R", 2): 160, ("25R", 3): 150}

# Função objetivo
prob += lpSum([fi[bateria, j] * x[bateria][j] for bateria in baterias for j in fornecedores])
# Restrição 1: Para cada bateria, a quantidade comprada pelos fornecedores deve atender à demanda
for bateria in baterias:
    prob += lpSum([x[bateria][j] for j in fornecedores]) == di[bateria]

# Restrição 2: Para cada bateria e fornecedor, a quantidade comprada não pode ultrapassar a quantidade disponível para compra
for bateria in baterias:
    for j in fornecedores:
        prob += x[bateria][j] <= cij[bateria, j]

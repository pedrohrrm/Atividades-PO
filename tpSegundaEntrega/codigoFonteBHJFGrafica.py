import tkinter as tk
import pulp

def run_optimization():
    # Inicializa o modelo
    model = pulp.LpProblem("Minimização de gastos com frete", pulp.LpMinimize)

    # Variáveis de decisão
    x = pulp.LpVariable.dicts("x", [(i, j) for i in range(1, 7) for j in range(1, 4)],
                               lowBound=0,
                               cat="Integer")

    # Pega os valores dos campos de entrada
    demandas = {i: int(demanda_entry[i].get()) for i in range(1, 4)}
    demandas_jf = {i: int(demand_jf_entry[i].get()) for i in range(1, 4)}
    ofertas = {i: int(supply_entry[i].get()) for i in range(1, 4)}
    ofertas_jf = {i: int(supply_jf_entry[i].get()) for i in range(1, 4)}
    fretes = {(i, j): float(shipping_cost_entry[i][j].get())
                for i in range(1, 4) for j in range(1, 4)}
    fretes_jf = {(i, j): float(shipping_cost_jf_entry[i-3][j].get())
                for i in range(4, 7) for j in range(1, 4)}

    # Função objetivo
    model += sum(x[i, j] * (fretes[(i, j)] if i <= 3 else fretes_jf[(i, j)])
                 for i in range(1, 7) for j in range(1, 4))

    # Restrições
    for i in range(1, 7):
        model += sum(x[i, j] for j in range(1, 4)) == (demandas[i] if i <= 3 else demandas_jf[i-3])
    for j in range(1, 4):
        model += sum(x[i, j] for i in range(1, 7)) <= (ofertas[j] if j <= 3 else ofertas_jf[j-3])

#Demanda dos clientes
    for i in range(1, 7):
        model += sum(x[i, j] for j in range(1, 4)) >= demandas[i]

#Otimizacao do modelo
    model.optimize()

#Verificacao do estado de otimizacao
    if model.status == GRB.OPTIMAL:
        solution = model.getAttr('x', x)
        total_cost = model.objVal
        print("A solução ótima encontrou um resultado de:", total_cost)
        for i in range(1, 7):
            for j in range(1, 4):
                if solution[(i, j)] > 0:
                    print("Se enviaron", solution[(i, j)], "unidades da fábrica", j, "cliente", i)
    else:
        print("O modelo não funciona devido a:", model.status)

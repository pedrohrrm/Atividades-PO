import pulp

# Inicializa o modelo
model = pulp.LpProblem("Minimização de gastos com frete", pulp.LpMinimize)
# Parâmetros

ofertas = {1: 50, 2: 30, 3: 20}
ofertas_jf = {1: 40, 2: 40, 3: 15}
fretes = {(1, 1): 1.10, (1, 2): 0.80, (1, 3): 3.50,
          (2, 1): 0.60, (2, 2): 0.70, (2, 3): 2.80,
          (3, 1): 2.00, (3, 2): 1.80, (3, 3): 3.00}
fretes_jf = {(4, 1): 1.30, (4, 2): 1.50, (4, 3): 1.80,
            (5, 1): 1.10, (5, 2): 0.90, (5, 3): 1.40,
            (6, 1): 2.10, (6, 2): 1.30, (6, 3): 3.50}
# Variáveis de decisão
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(1, 7) for j in range(1, 4)],
                           lowBound=0,
                           cat="Integer")

# Pede os parâmetros para o usuário
demandas = {i: int(input(f"Entre com a demanda para a bateria {i} (BH): ")) for i in range(1, 4)}
demandas_jf = {i: int(input(f"Entre com a demanda para a bateria {i} (JF): ")) for i in range(1, 4)}

# Função objetivo
model += sum(x[i, j] * (fretes[(i, j)] if i <= 3 else fretes_jf[(i, j)])
             for i in range(1, 7) for j in range(1, 4))

# Restrições
for i in range(1, 4):
    model += sum(x[i, j] for j in range(1, 4)) == demandas[i]
    model += sum(x[i + 3, j] for j in range(1, 4)) == demandas_jf[i]
    for j in range(1, 4):
        model += x[i, j] <= ofertas[j]
        model += x[i + 3, j] <= ofertas_jf[j]
for j in range(1, 4):
    model += x[1, j] <= ofertas[1]
    model += x[2, j] <= ofertas[2]
    model += x[3, j] <= ofertas[3]
    model += x[4, j] <= ofertas_jf[1]
    model += x[5, j] <= ofertas_jf[2]
    model += x[6, j] <= ofertas_jf[3]

#Resolve o modelo
model.solve()

#Imprime o resultado
print("Valor ótimo da função objetivo: R$ {:.2f}".format(pulp.value(model.objective)))
for i in range(1, 7):
    for j in range(1, 4):
        if x[i, j].value() > 0:
            local = "BH" if i <=3 else "JF"
            if j == 1:
                bateria = "Sony VTC5A"
            elif j == 2:
                bateria = "LG HG2"
            elif j == 3:
                bateria = "Samsung 25R"
            else:
                bateria = "Bateria {}".format(i-3)
            print("Comprar {:.0f} unid bateria {} do fornecedor {}, enviar para:{}".format(x[i, j].value(), bateria, j, local))
from scipy.optimize import linprog
obj = [-2000, -3000]
lado_esq = [[1 ,1] #totalacres
[3,2] #totaltrabalhador
[2,4] #totalfertilizante
]
lado_dir = [450, 1000, 1200]
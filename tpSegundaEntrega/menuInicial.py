import tkinter as tk
from tkinter import *

# Criar a janela principal
root = tk.Tk()
root.title("Menu")

# Adicionar um título
title_label = tk.Label(root, text="MENU", font=("Helvetica", 16))
title_label.pack(pady=20)

#Definindo abrr processadores ao cliclar
def abrir_processadores():
    janela_processadores = Tk()
    janela_processadores.title("Processadores")
    # código para adicionar os botões e outros elementos na janela de processadores
    janela_processadores.mainloop()
# código da janela principal (menu inicial)
janela = Tk()
janela.title("Menu")

def clique_estoque(self):
    root.destroy()
    telaEstoque(Tk())


# criando o botão "Processadores"
botao_processadores = Button(janela, text="Processadores", command=abrir_processadores)
botao_processadores.pack()

janela.mainloop()


# Função de callback para o botão Processadores
def processadores_callback():
    print("Processadores")

# Função de callback para o botão Alterar preço
def alterar_preco_callback():
    print("Alterar preço")

# Função de callback para o botão Estoque
def estoque_callback():
    print("Estoque")

# Botão Processadores
processadores_button = tk.Button(root, text="Processadores", command=processadores_callback)
processadores_button.pack(pady=10)

# Botão Alterar preço
alterar_preco_button = tk.Button(root, text="Alterar preço", command=alterar_preco_callback)
alterar_preco_button.pack(pady=10)

# Botão Estoque
estoque_button = tk.Button(root, text="Estoque", command=estoque_callback)
estoque_button.pack(pady=10)

# Rodar a aplicação
root.mainloop()

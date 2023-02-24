class TelaEstoque:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        
        self.titulo = Label(self.container1, text="Estoque")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()
        
        self.atualizar = Button(self.container2)
        self.atualizar["text"] = "Atualizar"
        self.atualizar["font"] = self.fonte
        self.atualizar["width"] = 12
        self.atualizar.pack(side=LEFT)
        
        self.conferir = Button(self.container2)
        self.conferir["text"] = "Conferir"
        self.conferir["font"] = self.fonte
        self.conferir["width"] = 12
        self.conferir.pack(side=LEFT)
        
        self.organizar = Button(self.container2)
        self.organizar["text"] = "Organizar"
        self.organizar["font"] = self.fonte
        self.organizar["width"] = 12
        self.organizar.pack(side=LEFT)
        
        self.voltar = Button(self.container2)
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = self.fonte
        self.voltar["width"] = 12
        self.voltar["command"] = self.voltar_tela
        self.voltar.pack(side=LEFT)
        
    def voltar_tela(self):
        root.destroy()
        MainWindow()


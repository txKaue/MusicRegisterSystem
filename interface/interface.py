import tkinter as tk
from tkinter import ttk, messagebox
from dataBase.data import Data
from utils.convert import Conversor

class Interface:

    def __init__(self, dataBase):
        self.root = tk.Tk()
        self.db = dataBase #Transformando o banco em algo do objeto tela
        self.cvt = Conversor()
        self.nomeInput = ""
        self.artistaInput = ""
        self.generoInput = ""
        self.root.title("Cadastro de músicas") #Mudando o nome da janela
        self.width = 720
        self.height = 560
        centerPosition = self.getCentroDaTela()
        self.root.geometry(f'{self.width}x{self.height}+{centerPosition[0]}+{centerPosition[1]}') #Definindo as medidas da janela
        self.root.resizable(False, False) #Impede o user de mudar o tamanho da tela
        self.root.iconbitmap('./assets/images/logoApp.ico') #Mudando o icone da janela
        self.mudar = False
        self.MontarAdicionar()


    def Abrir(self):
        self.root.mainloop() #Isso aqui é o que mantém a tela funcionando

    def getCentroDaTela(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - self.width / 2)
        center_y = int(screen_height/2 - self.height / 2)
        return [center_x, center_y]
    
    def MontarAdicionar(self):

        #Primeiro vou dividir as áreas da tela
        lFrame = ttk.Frame(self.root, height=self.height, width=self.width/2)
        lFrame.pack(side="left", fill="both", expand=True)

        rFrame = ttk.Frame(self.root, height=self.height, width=self.width/2)
        rFrame.pack(side="right", fill="both", expand=True)

        #Adicionando um descritivo em cada lado
        ttk.Label(lFrame, text='Adicionar música', font=("Arial", 12)).pack(pady=20)
        ttk.Label(rFrame, text='Pesquisar música', font=("Arial", 12)).pack(pady=20)

        #Montando o lado de adicionar novas músicas
        ttk.Label(lFrame, text='Nome', font=("Arial", 10)).pack(pady=10, padx=10, anchor='nw')
        self.nomeInput = ttk.Entry(lFrame, width=30)
        self.nomeInput.pack(pady=0, padx=10, anchor='nw')
        
        ttk.Label(lFrame, text='Artista', font=("Arial", 10)).pack(pady=10, padx=10, anchor='nw')
        self.artistaInput = ttk.Entry(lFrame, width=30)
        self.artistaInput.pack(pady=0, padx=10, anchor='nw')

        ttk.Label(lFrame, text='Gênero', font=("Arial", 10)).pack(pady=10, padx=10, anchor='nw')
        self.generoInput = ttk.Entry(lFrame, width=30)
        self.generoInput.pack(pady=0, padx=10, anchor='nw')

        self.botaoAdicionarMudar = ttk.Button(lFrame, text="Adicionar", command=self.Enviar)
        self.botaoAdicionarMudar.pack() 

        #Montando o lado de busca no banco de dados
        ttk.Label(rFrame, text='Pesquisar por nome', font=("Arial", 10)).pack(pady=10, padx=10, anchor='nw')
        self.buscaInput = ttk.Entry(rFrame, width=45)
        self.buscaInput.pack(pady=10, padx=10, anchor='nw')

        ttk.Button(rFrame, text="Buscar", command=self.Buscar).pack(pady=20)

        #Montando a visualização de alguns dados:
        self.listbox = tk.Listbox(rFrame, width=55, height=5, font=("Arial", 8))  # Definindo a altura para 5 itens visíveis
        self.listbox.pack(pady=10, padx= 10, anchor="nw")
        self.AtualizarLista()

        ttk.Button(lFrame, text="Exportar Dados", command=self.Exportar).pack(pady=20)

    def SerializarInput(self, nome, artista, genero):
        data = {}
        data["Nome"] = nome
        data["Artista"] = artista
        data["Genero"] = genero
        return data
    
    def LimparCampos(self):
        self.nomeInput.delete(0, 'end')
        self.artistaInput.delete(0, 'end')
        self.generoInput.delete(0, 'end')

    def Enviar(self):
        nome = self.nomeInput.get()
        artista = self.artistaInput.get()
        genero = self.generoInput.get()
        data = self.SerializarInput(nome, artista, genero)
        colection = "Músicas"
        self.db.AdicionarDados(colection, data)
        self.LimparCampos()
        self.AtualizarLista()

    def PreencherDados(self, data):
        self.nomeInput.insert(0, data["Nome"])
        self.artistaInput.insert(0, data["Artista"])
        self.generoInput.insert(0, data["Genero"])

    def Buscar(self):
        busca = self.buscaInput.get()
        data = self.db.getItemById("Músicas", self.db.getIdByName("Músicas", busca))
        if data != None:
            self.botaoAdicionarMudar.config(text="Alterar", command=self.Alterar)
            self.PreencherDados(data)
        else:
            messagebox.showerror("Erro", "Item não encontrado no banco.")

    def Alterar(self):
        nome = self.nomeInput.get()
        artista = self.artistaInput.get()
        genero = str(self.generoInput.get())

        if nome == None or artista == None or genero == None:
            messagebox.showerror("Erro", "Campos vazios operação cancelada.")
            self.botaoAdicionarMudar.config(text="Adicionar", command=self.Enviar)
            self.LimparCampos()
        else:
            id = self.db.getIdByName("Músicas", nome)
            data = self.SerializarInput(nome, artista, genero)
            print(data)
            sucesso = self.db.AlterarDados("Músicas", id, data)
            if sucesso:
                self.botaoAdicionarMudar.config(text="Adicionar", command=self.Enviar)
                self.LimparCampos()
                self.AtualizarLista()
            else:
                messagebox.showerror("Erro", "Inserção de dados inválida.")
                self.botaoAdicionarMudar.config(text="Adicionar", command=self.Enviar)
                self.LimparCampos()

    def AtualizarLista(self):
        self.listbox.delete(0, tk.END)

        data = self.db.GetDados("Músicas")
        for i in range(len(data)):
            if i == 5:
                break
            else:
                self.listbox.insert(tk.END, data[i])

    def Exportar(self):
        data = self.db.GetDados("Músicas")
        self.cvt.ConverterExcel(data)
        messagebox.showinfo("Documento Gerado", "Dados exportados para .xlsx")
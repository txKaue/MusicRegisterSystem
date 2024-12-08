import tkinter as tk
from tkinter import ttk
from dataBase.data import Data

class Interface:

    def __init__(self, dataBase):
        self.root = tk.Tk()
        self.db = dataBase #Transformando o banco em algo do objeto tela
        self.nomeInput = ""
        self.artistaInput = ""
        self.generoInput = ""
        self.root.title("Cadastro de músicas") #Mudando o nome da janela
        self.width = 600
        self.height = 400
        centerPosition = self.getCentroDaTela()
        self.root.geometry(f'600x400+{centerPosition[0]}+{centerPosition[1]}') #Definindo as medidas da janela
        self.root.resizable(False, False) #Impede o user de mudar o tamanho da tela
        self.root.iconbitmap('./assets/images/logoApp.ico') #Mudando o icone da janela
        self.MontarTela()


    def Abrir(self):
        self.root.mainloop() #Isso aqui é o que mantém a tela funcionando

    def getCentroDaTela(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - self.width / 2)
        center_y = int(screen_height/2 - self.height / 2)
        return [center_x, center_y]
    
    def MontarTela(self):

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

        ttk.Button(lFrame, text="Adicionar", command=self.Enviar).pack()

    def SerializarInput(self, nome, artista, genero):
        data = {}
        data["Nome"] = nome
        data["Artista"] = artista
        data["Gênero"] = genero
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
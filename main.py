from dataBase.data import Data
from interface.interface import Interface

#Criando a conexão com o banco de dados
db = Data()

#Criando a nossa interface
tl = Interface(db)
tl.Abrir()



import firebase_admin
from firebase_admin import credentials, firestore
import os

class Data:
    def __init__(self):
        cred_path = os.path.join(os.getcwd(), './dataBase/pycadastro-f3ded-firebase-adminsdk-ihzwp-f8749221f8.json')
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def AdicionarDados(self, colection, data):
        try:
            self.db.collection(colection).add(data)
            print("Dados adicionados com sucesso.")
        except:
            print("Erro ao adicionar ao banco de dados.")

    def GetDados(self, colection):
        data = self.collection(colection).get()
        return data
    
    def MostrarDados(self, colection):
        data = self.db.collection(colection).get()
        for item in data:
            print(f"{item.id} -> {item.to_dict()}")

    def AlterarDados(self, colection, id, data):
        try:
            original = self.db.collection(colection).document(id)
            original.update(data)
            print(f"Item alterado com sucesso.")
        except:
            print(f"Não foi possível editar o item {id}")

    def getIdByName(self, colection, nome):
        items = self.db.collection(colection).where(field_path="Nome", op_string="==", value=nome).get()

        if items:
            return items[0].id
        else:
            print("Item não encontrado")
            return None
            
    def DeleteDados(self, colection, id):
        try:
            self.db.collection(colection).document(id).delete()
            print(f"Item {id} deletado com sucesso.")
        except:
            print(f"Não foi possível deleter {id}.")


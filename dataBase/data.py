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
        data = self.db.collection(colection).get()
        result = []

        for doc in data:
            doc_dict = doc.to_dict()
            reordered_dict = {
                "Nome": doc_dict["Nome"],
                "Artista": doc_dict["Artista"],
                "Genero": doc_dict["Genero"],
            }
            
            result.append(reordered_dict)
        
        return result
    
    def MostrarDados(self, colection):
        data = self.db.collection(colection).get()
        for item in data:
            print(f"{item.id} -> {item.to_dict()}")

    def AlterarDados(self, colection, id, data):
        try:
            original = self.db.collection(colection).document(id)
            original.update(data)
            print(f"Item alterado com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao editar o item {id}: {e}")
            return

    def getIdByName(self, colection, nome):
        items = self.db.collection(colection).where(field_path="Nome", op_string="==", value=nome).get()

        if items:
            return items[0].id
        else:
            print("Item não encontrado")
            return None
        
    def getItemById(self, colection, item_id):
        try:
            document = self.db.collection(colection).document(item_id).get()
            if document.exists:
                return document.to_dict()
            else:
                print("Documento não encontrado")
                return None
            
        except Exception as e:
            print(f"Erro ao buscar o documento: {e}")
            return None
            
    def DeleteDados(self, colection, id):
        try:
            self.db.collection(colection).document(id).delete()
            print(f"Item {id} deletado com sucesso.")
        except:
            print(f"Não foi possível deleter {id}.")


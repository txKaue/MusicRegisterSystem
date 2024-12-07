from dataBase.data import Data

db = Data()
print("Conexão criada")

data = [
    {
        "Nome":"Espanca Joaninha",
        "Cidade": "Taubaté",
        "Tipo":"Cover"
    },
    {
        "Nome":"Alucinados",
        "Cidade": "Taubaté",
        "Tipo":"Cover"
    },
    {
        "Nome":"DMT",
        "Cidade": "Taubaté",
        "Tipo":"Autoral"
    }
]

for item in data:
    db.AdicionarDados("Bandas", item)

db.MostrarDados("Bandas")

db.AlterarDados("Bandas", db.getIdByName("Bandas", "Espanca Joaninha"), {"Nome":"Spank LadyBug"})

db.MostrarDados("Bandas")

db.DeleteDados("Bandas", db.getIdByName("Bandas", "DMT"))

db.MostrarDados("Bandas")


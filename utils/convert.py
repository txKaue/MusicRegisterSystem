import pandas as pd

class Conversor:
    def __init__(self):
        self.data = None

    def ConverterExcel(self, data):
        # {'Nome': 'Around the Fur', 'Artista': 'Deftones', 'Genero': 'NuMetal'}
        nomes = []
        artistas = []
        generos = []

        for i in data:
            nomes.append(i["Nome"])
            artistas.append(i["Artista"])
            generos.append(i["Genero"])

        table = {
            "Nome": nomes,
            "Artista": artistas,
            "Gênero": generos
        }

        df = pd.DataFrame.from_dict(table)
        df.to_excel("./Musicas.xlsx", index=False)
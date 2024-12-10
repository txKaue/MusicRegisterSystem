# Music register system

## Description
This application is a music management system. You can register, list and update musics information to a FireStore DataBase.
You also can export the data to a excel file.

## Technologies
    - Python 3
    - Google Firebase

## Instalation
1. Clone the repository:
    ´´´bash
    git clone https://github.com/txKaue/MusicRegisterSystem.git
    ```

2. Install dependencies:
    ´´´bash
    pip install -r requirements.txt
    ´´´

3. Run "main.py" file:
    ´´´bash
    python main.py
    ´´´

## How to use

After you execute the application, you'll see a simple UI if two sides: "Adicionar Músicas" and "Buscar Músicas"
If you dont the translation of these words, in the end of README you can find the translations.

You can add musics to database filling the entryies with "Nome", "Artista" and "Genero". Then you just have to click on "Adicionar" button.

You can search musics filling the "Buscar" entry and pressing the respective button. After, if musics exists on database, the informations will be appear on the left fields.
When the musics infomations appear, you also can update them.

You can export database to a excel file (.xlsx) to work on your data.

## License
This projects was made by Kauê Teixeira and you can use this to training your programming skills and learn more about the technologies

## Translations
Portuguese to English:
- Adicionar = Add
- Busacr = Find
- Adicionar Música = Add music
- Buscar Música = Find music
- Alterar Música = Update music
- Exportar = Export
- Nome = Name
- Artista = Artist
- Genero = Genre

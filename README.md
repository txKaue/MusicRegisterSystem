# Music register system

## Description
This application is a music management system. You can register, list and update musics information to a FireStore DataBase.
You also can export the data to a excel file.

## Technologies
    - Python 3
    - Google Firebase

## Instalation
1. Clone the repository:
    ```bash
    git clone https://github.com/txKaue/MusicRegisterSystem.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run "main.py" file:
    ```bash
    python main.py
    ```

## How to use

After you execute the application, you'll see a simple UI if two sides: "Adicionar Músicas" and "Buscar Músicas"
If you dont the translation of these words, in the end of README you can find the translations.

You can add musics to database filling the entryies with "Nome", "Artista" and "Genero". Then you just have to click on "Adicionar" button.

You can search musics filling the "Buscar" entry and pressing the respective button. After, if musics exists on database, the informations will be appear on the left fields.
When the musics infomations appear, you also can update them.

You can export database to a excel file (.xlsx) to work on your data.

## Project structure:

At root you will find 4 folders ("assets", "dataBase", "interface" and "utils") and 1 file (main.py). See the description bellow:
- Assets: This folders is for images or other stetic items.
- DataBase: This folder contains the dataBase class and here you will place your key to connect with FireBase (a json file, normally).
- Interface: This folder contains the interface class.
- Utils: This folder contains the converter class.
- Main.py: This is the main file project. You must run this file to use the application.

## Files and Functions:
Next you'll see the application UML.

## License
This projects was made by Kauê Teixeira and you can use this to training your programming skills and learn more about the technologies

## Translations
Portuguese to English:
- Adicionar = Add
- Buscar = Find
- Adicionar Música = Add music
- Buscar Música = Find music
- Alterar Música = Update music
- Exportar = Export
- Nome = Name
- Artista = Artist
- Genero = Genre

## Future Updates:

You cant delete musics from database, so the next feature i'll add will be a deletion system.

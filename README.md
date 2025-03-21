# sge_theBear_grupE

## FAST API PRIMERES PASSES

### Arxius
El primer pas per crear un projecte de FastAPI es crear una estructura de carpetes com diferents fitxers i utilitzar un fitxer buit "\_\_init__" a cada subcarpeta per poder accedir a l'altre desde altres carpetes.

![alttext](img/estructura.png "Estructura")

A continuació s'escriuran els fitxers corresponents, començant per "connect.py". El codi d'aquest serà el mateix utilitzat a l'activitat anterior.

![alttext](img/connect.png "connect.py")

El següent fitxer a complir serà "read_sch.py" que s'encarregarà de transformar les dades de users en format List a un format de disccionari.

![alttext](img/schema.png "read_sch.py")

Seguidament s'escriurà el fitxer "read.py" amb tota aquella lògica que permetrà treballar amb les consultes del client.

![alttext](img/read.png "read.py")

L'últim fitxer a omplir és el "main.py" que decidira que farà el programa segons la consulta del client.

![alttext](img/main.png "main.py")

### Comprovació

Un cop tots els fitxers tenen el seu codi corresponent, s'executa la comanda "uvicorn main:app --reload" desde el directori principal del projecte, si uvicorn no està instal·lat cal fer-ho amb la comanda "pip install uvicorn".

![alttext](img/uvicorn.png "uvicorn main:app --reload")


Finalment, a la següent captura es pot veure com tot funciona correctament utilitzant la nostra adreça a un navegador i es pot executar per veure la resposta.

![alttext](img/imatge_comprovacio.png "Comprovació")

## FASTAPI + BD
Per començar amb el projecte, s'ha creat un fitxer amb el nom "requirements.txt" amb els noms del requeriments que s'instal·laran a continuació amb la comanda "pip install -r requirements.txt".

![alttext](img/Requirements.png "Requirements")

Tot seguit es crea un fitxer .env amb la configuració del projecte per a la connexió amb la Base de Dades.

![alttext](img/env.png ".env")

Un cop fet això, s'ha afegit codi a main.py per carregar algunes variables i crear automàticament les taules a la Base de dades.

![alttext](img/main_modificat.png "main modificat")

Seguidament s'afegeix una carpeta de nom "models" i un fitxer de nom "User.py" amb codi per definir el model d'un usuari.

![alttext](img/User.png "User.py")

A continuació s'ha fet la modificació de l'endpoint read a l'arxiu main.py.

![alttext](img/endpoint_read.png "endpoint read")

A l'arxiu user.py s'ha afegit el mètode "get_all_users" que s'ecarrega de fer la consulta a la BD.

![alt text](img/get_all_users.png "metode get all users")

Seguint a aquest arxiu, s'ha creat un nou mètode "add_new_user" per crear usuaris amb un endpoint al main.

![alttext](img/add_new_user.png "metode add new user")

![alttext](img/endpoint_add_new_user.png "endpoint add new user")

Finalment es crea l'arxiu users_sch amb 2 funcions per consultar a la BD en un format json.

![alttext](img/users_sch.png "users_sch")

Un cop acabat, es fa la comprovació novament amb la comanda "uvicorn main:app --reload"

![alttext](img/uvicornBD.png "uvicorn BD")
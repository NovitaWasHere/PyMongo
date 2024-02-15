from pymongo import MongoClient
import pprint

MONGO_URI=['mongodb+srv://<username>:<password>@cluster.aoqznyg.mongodb.net/?retryWrites=true&w=majority']

client = MongoClient(MONGO_URI)
db = client['Ejemplo']
collection = db['Users']

#Consiguiendo todos los documentos de la base de datos
for post in collection.find():
    pprint.pprint(post)

#Conseguir un dolo documento de la base de datos

#Se le pasa la clave por la que va a preguntar
clave = input("Ingrese la clave que se buscara del usuario")
cl = clave.lstrip().rstrip().lower()

#Se le pasa el valor por el que va a preguntar
valor = input("Ingrese el valor que se buscara de usuario (Importan realmente las mayusculas)")
vl = valor.lstrip().rstrip()

pprint.pprint(collection.find_one({cl:vl}))

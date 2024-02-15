from pymongo import MongoClient
import pprint

MONGO_URI=['mongodb+srv://<username>:<password>@cluster.aoqznyg.mongodb.net/?retryWrites=true&w=majority']

client = MongoClient(MONGO_URI)
db = client['Ejemplo']
collection = db['Users']

# Updating fan quantity from 10 to 25.

clave = input("Ingrese la clave por la que se actualizará el usuario")
cl = clave.lstrip().rstrip().lower()

valor = input("Ingrese el valor de f{cl} de su usuario (Importan realmente las mayusculas)")
vl = valor.lstrip().rstrip()

das = {cl: vl}

act = input("Nuevo dato")
actU = act.lstrip().rstrip()

# Values to be updated.
values = {"$set": {cl: actU}}

pprint.pprint(collection.update_one(das, values))

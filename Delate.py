from pymongo import MongoClient
import pprint

MONGO_URI=['mongodb+srv://novita:1234567890aBc@cluster.aoqznyg.mongodb.net/?retryWrites=true&w=majority']

client = MongoClient(MONGO_URI)
db = client['Ejemplo']
collection = db['Users']

# Updating fan quantity from 10 to 25.

usuario = input("Ingrese el usuario que eliminaras")
cl = usuario.lstrip().rstrip()


pprint.pprint(collection.delete_one({'username':usuario}))

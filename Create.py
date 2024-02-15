from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import datetime

MONGO_URI=['mongodb+srv://novita:1234567890aBc@cluster.aoqznyg.mongodb.net/?retryWrites=true&w=majority']

client = MongoClient(MONGO_URI)
db = client['Ejemplo']
collection = db['Users']

#Insertando un documento a la base de datos

username = input("Ingrese el nombre de usuario")
password = input("Ingrese la constraseña de usuario")
hashed = generate_password_hash(password)
genres = []

for i in range(3):
    texto = input(f"Ingrese el texto #{i + 1}: ")
    genres.append(texto)

Users = {
    "username": username,
    "password": hashed,
    "genres": genres,
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

post_id = collection.insert_one(Users).inserted_id
print(post_id)
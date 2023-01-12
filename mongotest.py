import pymongo
client = pymongo.MongoClient("mongodb+srv://naveensai1188:Emomari123@cluster0.2uuqig4.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "naveensai1188",
    "email": "naveensai.ayila1188@gmail.com",
    "surname": "kumar"

}


d = {
    "name": "naveensai1188",
    "email": "naveensai.ayila1188@gmail.com",
    "surname": "kumar"

}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
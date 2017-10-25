from pymongo import MongoClient
import json


client = MongoClient("mongodb://moishernandez:Clavefacil_2@cluster0-shard-00-00-lm9as.mongodb.net:27017,cluster0-shard-00-01-lm9as.mongodb.net:27017,cluster0-shard-00-02-lm9as.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
camps_data = client.camps_data
camps_collection = camps_data.camps_collection


with open('campamentos.json') as data_file:
    camps = json.load(data_file)

camps_collection.delete_many({})
camps_collection.insert_many(camps)













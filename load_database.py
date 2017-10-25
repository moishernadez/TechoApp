from pymongo import MongoClient
import json

client = MongoClient ()
camps_data = client.camps_data
camps_collection = camps_data.camps_collection


with open('campamentos.json') as data_file:
    camps = json.load(data_file)

camps_collection.delete_many({})
camps_collection.insert_many(camps)













from pymongo import MongoClient
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import math

app = Flask(__name__)
CORS(app)

@app.route('/camps/<float:ratio>&<float:abs_value_latitud>&<float:abs_value_longitud>', methods=['GET'])
def get_camps(ratio, abs_value_latitud, abs_value_longitud):
    client = MongoClient(
        "mongodb://moishernandez:Clavefacil_2@cluster0-shard-00-00-lm9as.mongodb.net:27017,cluster0-shard-00-01-lm9as.mongodb.net:27017,cluster0-shard-00-02-lm9as.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
    camps_data = client.camps_data
    camps_collection = camps_data.camps_collection

    cursor = camps_collection.find({})
    matching_camps = []
    for document in cursor:
        if math.sqrt((-abs_value_latitud - document["LATITUD"]) ** 2 + (-abs_value_longitud - document["LONGITUD"]) ** 2) < ratio:
            matching_camps.append(document)
    return jsonify(matching_camps)

if __name__ == '__main__':
    app.run(port=9000)

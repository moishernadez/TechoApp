from pymongo import MongoClient
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import math

app = Flask(__name__)
CORS(app)

@app.route('/camps/<float:ratio>&<float:abs_value_latitud>&<float:abs_value_longitud>', methods=['GET'])
def get_camps(ratio, abs_value_latitud, abs_value_longitud):
    client = MongoClient()
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

import json

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/V1.0/get_building_info/<string:building>')
def building_info(building):
    with open('buildings.json') as file:
        building_json = json.load(file)
        print(building_json[0])
        for building_object in building_json:
            print(building)
            if building_object['name'] == building:
                return building_object
    return "Building not found"


if __name__ == '__main__':
    app.run()

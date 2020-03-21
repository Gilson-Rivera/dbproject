from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

# import handlers
from Handlers.Fuel import FuelHandler

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/')
def greeting():
    return 'DB 2020 Project Phase 1' \
           'By Jonathan, Angel and Gilson'

@app.route('/Phase1/fuel', methods=['GET', 'POST'])
def getAllFuel():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FuelHandler().insertFuelJson(request.json)
    else:
        if not request.args:
            return FuelHandler().getAllFuel()
        else:
            #change to searchFuel() once implemented in handlers
            return FuelHandler().getAllFuel()


if __name__ == '__main__':
    app.run()


from flask import Flask, jsonify, request
from handler.consumers import ConsumerHandler
from handler.supplier import SupplierHandler
from handler.fuel import FuelHandler

# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/')
def greeting():
    return 'Hello, this is the DB project App!'

@app.route('/DBApp1/consumers', methods=['GET', 'POST'])
def getAllConsumers():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ConsumerHandler().insertConsumerJson(request.json)
    else:
        if not request.args:
            return ConsumerHandler().getAllConsumers()
        else:
            return ConsumerHandler().searchConsumers(request.args)

@app.route('/DBApp1/consumers/<int:cid>', methods=['GET', 'PUT', 'DELETE'])
def getConsumerById(cid):
    if request.method == 'GET':
        return ConsumerHandler().getConsumerById(cid)
    elif request.method == 'PUT':
        return ConsumerHandler().updateConsumer(cid, request.form)
    elif request.method == 'DELETE':
        return ConsumerHandler().deleteConsumer(cid)
    else:
        return jsonify(Error="Method not allowed."), 405

# @app.route('/PartApp/parts/<int:pid>/suppliers')
# def getSuppliersByPartId(pid):
#     return ConsumerHandler().getSuppliersByPartId(pid)

@app.route('/DBApp1/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else :
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)

@app.route('/DBApp1/suppliers/<int:sid>',
           methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/DBApp1/fuel', methods=['GET', 'POST'])
def getAllFuel():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FuelHandler().insertFuelJson(request.json)
    else:
        if not request.args:
            return FuelHandler().getAllFuel()
        else:
            #change to searchFuel() once implemented in handlers
            return FuelHandler().searchFuel(request.args)

@app.route('/DBApp1/fuel/<int:fuid>', methods=['GET', 'PUT', 'DELETE'])
def getFuelById(fuid):
    if request.method == 'GET':
        return FuelHandler().getFuelByID(fuid)
    elif request.method == 'PUT':
        return FuelHandler().updateFuel(fuid, request.form)
    elif request.method == 'DELETE':
        return FuelHandler().deleteFuel(fuid)
    else:
        return jsonify(Error="Method not allowed."), 405


# @app.route('/PartApp/suppliers/<int:sid>/parts')
# def getPartsBySuplierId(sid):
#     return SupplierHandler().getPartsBySupplierId(sid)

# @app.route('/PartApp/parts/countbypartid')
# def getCountByPartId():
#     return ConsumerHandler().getCountByPartId()

if __name__ == '__main__':
    app.run()
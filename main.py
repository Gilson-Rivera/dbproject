from flask import Flask, jsonify, request
from Handlers.Consumer import ConsumerHandler
from Handlers.Supplier import SupplierHandler
from Handlers.Fuel import FuelHandler
from Handlers.Fuel_Supplies import FuelSuppliesHandler
from Handlers.Medication import MedHandler
from Handlers.Medication_Supplies import MedSuppliesHandler

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
        return SupplierHandler().insertSupplierJson(request.json)
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

@app.route('/DBApp1/fuel_supplies', methods=['GET', 'POST'])
def getAllFuelSupplies():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FuelSuppliesHandler().insertFuelSuppliesJson(request.json)
    else:
        if not request.args:
            return FuelSuppliesHandler().getAllFuelSupplies()
        else:
            return FuelSuppliesHandler().searchFuelSupplies(request.args)

@app.route('/DBApp1/med', methods=['GET', 'POST'])
def getAllMed():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return MedHandler().insertMedJson(request.json)
    else:
        if not request.args:
            return MedHandler().getAllMed()
        else:
            #change to searchMed() once implemented in handlers
            return MedHandler().searchMed(request.args)

@app.route('/DBApp1/med/<int:mid>', methods=['GET', 'PUT', 'DELETE'])
def getMedById(mid):
    if request.method == 'GET':
        return MedHandler().getMedByID(mid)
    elif request.method == 'PUT':
        return MedHandler().updateMed(mid, request.form)
    elif request.method == 'DELETE':
        return MedHandler().deleteMed(mid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DBApp1/med_supplies', methods=['GET', 'POST'])
def getAllMedSupplies():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return MedSuppliesHandler().insertMedSuppliesJson(request.json)
    else:
        if not request.args:
            return MedSuppliesHandler().getAllMedSupplies()
        else:
            return MedSuppliesHandler().searchMedSupplies(request.args)


# @app.route('/PartApp/suppliers/<int:sid>/parts')
# def getPartsBySuplierId(sid):
#     return SupplierHandler().getPartsBySupplierId(sid)

# @app.route('/PartApp/parts/countbypartid')
# def getCountByPartId():
#     return ConsumerHandler().getCountByPartId()

if __name__ == '__main__':
    app.run()
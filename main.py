from flask import Flask, jsonify, request
from handler.food import FoodHandler
from handler.request_supplies import RequestedSuppliesHandler
from handler.consumers import ConsumerHandler
from handler.administrators import AdministratorHandler
from handler.supplier import SupplierHandler
from handler.fuel import FuelHandler
from handler.resources import ResourcesHandler
from handler.equipment import EquipHandler
from handler.medical_devices import MedDevHandler
from handler.fuel_supplies import FuelSuppliesHandler
from handler.food_supplies import FoodSuppliesHandler
from handler.esupplies import ESuppliesHandler
from handler.mdsupplies import MDSuppliesHandler
from handler.medication import MedHandler
from handler.med_supplies import MedSuppliesHandler

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


@app.route('/DBApp1/administrators', methods=['GET', 'POST'])
def getAllAdministrators():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return AdministratorHandler().insertAdministratorJson(request.json)
    else:
        if not request.args:
            return AdministratorHandler().getAllAdministrators()
        else:
            return AdministratorHandler().searchAdministrators(request.args)


@app.route('/DBApp1/administrators/<int:aid>', methods=['GET', 'PUT', 'DELETE'])
def getAdministratorById(aid):
    if request.method == 'GET':
        return AdministratorHandler().getAdministratorById(aid)
    elif request.method == 'PUT':
        return AdministratorHandler().updateAdministrator(aid, request.form)
    elif request.method == 'DELETE':
        return AdministratorHandler().deleteAdministrator(aid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DBApp1/resources', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ResourcesHandler().insertResourceJson(request.json)
    else:
        if not request.args:
            return ResourcesHandler().getAllResources()
        else:
            return ResourcesHandler().searchResources(request.args)

@app.route('/DBApp1/resources/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def getResourcesById(rid):
    if request.method == 'GET':
        return ResourcesHandler().getResourcesById(rid)
    elif request.method == 'PUT':
        return ResourcesHandler().updateResources(rid, request.form)
    elif request.method == 'DELETE':
        return ResourcesHandler().deleteResources(rid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DBApp1/resources_consumed/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def getResourcesConsumedById(rid):
    if request.method == 'GET':
        return ResourcesHandler().getResourcesConsumedById(rid)
    elif request.method == 'PUT':
            return ResourcesHandler().updateResources(rid, request.form)
    elif request.method == 'DELETE':
        return ResourcesHandler().deleteResources(rid)
    else:
        return jsonify(Error="Method not allowed."), 405


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

@app.route('/DBApp1/medication_supplies', methods=['GET', 'POST'])
def getAllMedSupplies():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return MedSuppliesHandler().insertMedSuppliesJson(request.json)
    else:
        if not request.args:
            return MedSuppliesHandler().getAllMedSupplies()
        else:
            return MedSuppliesHandler().searchMedSupplies(request.args)

@app.route('/DBApp1/food_supplies', methods=['GET', 'POST'])
def getAllFoodSupplies():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FoodSuppliesHandler().insertFoodSuppliesJson(request.json)
    else:
        if not request.args:
            return FoodSuppliesHandler().getAllFoodSupplies()
        else:
            return FoodSuppliesHandler().searchFoodSupplies(request.args)

@app.route('/DBApp1/requested_supplies', methods=['GET', 'POST'])
def getAllRequestedSupplies():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return RequestedSuppliesHandler().insertRequestedSuppliesJson(request.json)
    else:
        if not request.args:
            return RequestedSuppliesHandler().getAllRequestedSupplies()
        # else:
        #     return RequestedSuppliesHandler().searchRequestedSupplies(request.args)

@app.route('/DBApp1/medications', methods=['GET', 'POST'])
def getAllMedications():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return MedHandler().insertMedicationJson(request.json)
    else:
        if not request.args:
            return MedHandler().getAllMedications()
        else:
            return MedHandler().searchMedications(request.args)

@app.route('/DBApp1/food', methods=['GET', 'POST'])
def getAllFood():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FoodHandler().insertFoodJson(request.json)
    else:
        if not request.args:
            return FoodHandler().getAllFood()
        else:
            # change to searchFood() once implemented in handlers
            return FoodHandler().searchFood(request.args)


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

@app.route('/DBApp1/medications/<int:mid>', methods=['GET', 'PUT', 'DELETE'])
def getMedicationById(mid):
    if request.method == 'GET':
        return MedHandler().getMedicationByID(mid)
    elif request.method == 'PUT':
        return MedHandler().updateMed(mid, request.form)
    elif request.method == 'DELETE':
        return MedHandler().deleteMed(mid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/DBApp1/food/<int:fid>', methods=['GET', 'PUT', 'DELETE'])
def getFoodById(fid):
    if request.method == 'GET':
        return FoodHandler().getFoodByID(fid)
    elif request.method == 'PUT':
        return FoodHandler().updateFood(fid, request.form)
    elif request.method == 'DELETE':
        return FoodHandler().deleteFood(fid)
    else:
        return jsonify(Error="Method not allowed."), 405


# @app.route('/PartApp/parts/<int:pid>/suppliers')
# def getSuppliersByPartId(pid):
#     return ConsumerHandler().getSuppliersByPartId(pid)

@app.route('/DBApp1/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return SupplierHandler().insertSupplierJson(request.json)
    else:
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
        return jsonify(Error="Method not allowed"), 405


@app.route('/DBApp1/fuel', methods=['GET', 'POST'])
def getAllFuel():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FuelHandler().insertFuelJson(request.json)
    else:
        if not request.args:
            return FuelHandler().getAllFuel()
        else:
            # change to searchFuel() once implemented in handlers
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


@app.route('/DBApp1/equipment_supplies', methods=['GET', 'POST'])
def getAllESupplies():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ESuppliesHandler().insertESuppliesJson(request.json)
    else:
        if not request.args:
            return ESuppliesHandler().getAllESupplies()
        else:
            return ESuppliesHandler().searchESupplies(request.args)


@app.route('/DBApp1/mdsupplies', methods=['GET', 'POST'])
def getAllMDSupplies():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return MDSuppliesHandler().insertMDSuppliesJson(request.json)
    else:
        if not request.args:
            return MDSuppliesHandler().getAllMDSupplies()
        else:
            return MDSuppliesHandler().searchMDSupplies(request.args)


@app.route('/DBApp1/equipment', methods=['GET', 'POST'])
def getAllEquipment():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return EquipHandler().insertEquipmentJson(request.json)
    else:
        if not request.args:
            return EquipHandler().getAllEquipment()
        else:
            # change to searchEquipment() once implemented in handlers
            return EquipHandler().searchEquipment(request.args)


@app.route('/DBApp1/equipment/<int:eid>', methods=['GET', 'PUT', 'DELETE'])
def getEquipmentById(eid):
    if request.method == 'GET':
        return EquipHandler().getEquipmentByID(eid)
    elif request.method == 'PUT':
        return EquipHandler().updateEquipment(eid, request.form)
    elif request.method == 'DELETE':
        return EquipHandler().deleteEquipment(eid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/DBApp1/medical_devices', methods=['GET', 'POST'])
def getAllMedDev():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return MedDevHandler().insertMedDevJson(request.json)
    else:
        if not request.args:
            return MedDevHandler().getAllMedDev()
        else:
            # change to searchMedDev() once implemented in handlers
            return MedDevHandler().searchMedDev(request.args)


@app.route('/DBApp1/medical_devices/<int:mdid>', methods=['GET', 'PUT', 'DELETE'])
def getMedDevById(mdid):
    if request.method == 'GET':
        return MedDevHandler().getMedDevByID(mdid)
    elif request.method == 'PUT':
        return MedDevHandler().updateMedDev(mdid, request.form)
    elif request.method == 'DELETE':
        return MedDevHandler().deleteMedDev(mdid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/DBApp1/med', methods=['GET', 'POST'])
def getAllMed():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return MedHandler().insertMedJson(request.json)
    else:
        if not request.args:
            return MedHandler().getAllMed()
        else:
            return MedHandler().searchMed(request.args)



if __name__ == '__main__':
    app.run()

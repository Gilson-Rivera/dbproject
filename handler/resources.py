# resources handler

from flask import jsonify
from dao.resources import ResourcesDAO, MedicationDAO
from dao.resources import FoodDAO
from dao.resources import EquipmentDAO
from dao.resources import MedDevDAO
from dao.resources import MedicationDAO
from dao.resources import FuelDAO
from dao.resources import ClothingDAO
from dao.resources import WaterDAO


class ResourcesHandler:
    def build_resources_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rbrand'] = row[2]
        result['rnumavailable'] = row[3]
        result['rprice'] = row[4]
        result['rsupplier'] = row[5]
        result['rlocation'] = row[6]
        return result

    def build_resources_consumed_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['rid'] = row[1]
        result['cfirstname'] = row[2]
        result['clastname'] = row[3]
        result['rtype'] = row[4]
        result['rbrand'] = row[5]
        result['rconsume_price'] = row[6]
        result['rconsume_quantity'] = row[7]
        result['rconsume_date'] = row[8]
        result['rconsume_payment_method'] = row[9]
        return result

    def build_resources_attributes(self, rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation):
        result = {}
        result['rid'] = rid
        result['rtype'] = rtype
        result['rbrand'] = rbrand
        result['rnumavailable'] = rnumavailable
        result['rprice'] = rprice
        result['rsupplier'] = rsupplier
        result['rlocation'] = rlocation
        return result

    def build_rconsumes_attributes(self, cid, rid, rconsume_price, rconsume_quantity, rconsume_date, rconsume_payment_method):
        result = {}
        result['cid'] = cid
        result['rid'] = rid
        result['rconsume_price'] = rconsume_price
        result['rconsume_quantity'] = rconsume_quantity
        result['rconsume_date'] = rconsume_date
        result['rconsume_payment_method'] = rconsume_payment_method
        return result

    def build_rsupplies_attributes(self, sid, rid, rsupply_price, rsupply_quantity, rsupply_date):
        result = {}
        result['sid'] = sid
        result['rid'] = rid
        result['rsupply_price'] = rsupply_price
        result['rsupply_quantity'] = rsupply_quantity
        result['rsupply_date'] = rsupply_date
        return result

    def getAllResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResources()
        result_list = []
        for row in resources_list:
            result = self.build_resources_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def searchResources(self, args):
        type = args.get("type")
        status = args.get("status")  # reserved or purchased
        location = args.get("location")
        dao = ResourcesDAO()
        resources_list = []
        result_list = []
        if (len(args) == 1) and type:
            resources_list = dao.getResourcesByType(type)
            for row in resources_list:
                result = self.build_resources_dict(row)
                result_list.append(result)
        elif (len(args) == 1) and status:
            resources_list = dao.getResourcesByStatus(status)
            for row in resources_list:
                result = self.build_resources_consumed_dict(row)  # also need to add consumer's information
                result_list.append(result)
        elif (len(args) == 1) and location:
            resources_list = dao.getResourcesByLocation(location)
            for row in resources_list:
                result = self.build_resources_dict(row)
                result_list.append(result)
        else:
            return jsonify(Error="Malformed query string"), 400

        return jsonify(Resources=result_list)

    def getResourcesById(self, rid):
        dao = ResourcesDAO()
        row = dao.getResourcesById(rid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            resource = self.build_resources_dict(row)
            return jsonify(Resource=resource)

    def getResourcesConsumedByConsumerId(self, cid):
        dao = ResourcesDAO()
        resources_list = dao.getResourcesConsumedByConsumerId(cid)
        result_list = []
        for row in resources_list:
            result = self.build_resources_consumed_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourcesConsumedById(self, cid, rid):
        dao = ResourcesDAO()
        row = dao.getResourcesConsumedById(cid, rid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            requested_supply = self.build_resources_consumed_dict(row)
            return jsonify(MedicalDevices=requested_supply)

    def getResourcesByType(self, rtype):
        dao = ResourcesDAO()
        resources_list = dao.getResourcesByType(rtype)
        return jsonify(Resources=resources_list)

    def getResourcesByBrand(self, rbrand):
        dao = ResourcesDAO()
        resources_list = dao.getResourcesByBrand(rbrand)
        return jsonify(Resources=resources_list)

    def getResourcesByNumAvailable(self, rnumavailable):
        dao = ResourcesDAO()
        resources_list = dao.getResourcesByNumAvailable(rnumavailable)
        return jsonify(Resources=resources_list)

    def getResourcesByPrice(self, rprice):
        dao = ResourcesDAO()
        resources_list = dao.getResourcesByPrice(rprice)
        return jsonify(Resources=resources_list)

    def getResourcesBySupplier(self, rsupplier):
        dao = ResourcesDAO()
        resources_list = dao.getResourcesBySupplier(rsupplier)
        return jsonify(Resources=resources_list)

    def getResourcesByLocation(self, rlocation):
        dao = ResourcesDAO()
        resources_list = dao.getResourcesByLocation(rlocation)
        return jsonify(Resources=resources_list)

    def insertResourceJson(self, json):
        rtype = json['rtype']
        rbrand = json['rbrand']
        rnumavailable = json['rnumavailable']
        rprice = json['rprice']
        rsupplier = json['rsupplier']
        rlocation = json['rlocation']
        if rtype and rbrand and rnumavailable and rprice and rsupplier and rlocation:
            dao = ResourcesDAO()
            rid = dao.insert(rtype, rbrand, rnumavailable, rprice)
            rsupplier_id = dao.insertSupplier(rid, rsupplier)
            rlocation_id = dao.insertLocation(rid, rlocation)
            result = self.build_resources_attributes(rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation)
            return jsonify(Resources=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


    def insertConsumptionJson(self, json):
        cid = json['cid']
        rid = json['rid']
        rconsume_price = json['rconsume_price']
        rconsume_quantity = json['rconsume_quantity']
        rconsume_date = json['rconsume_date']
        rconsume_payment_method = json['rconsume_payment_method']
        if cid and rid and rconsume_price and rconsume_quantity and rconsume_date and rconsume_payment_method:
            dao = ResourcesDAO()
            consume_id = dao.insertConsumption(cid, rid, rconsume_price, rconsume_quantity, rconsume_date, rconsume_payment_method)
            result = self.build_rconsumes_attributes(cid, rid, rconsume_price, rconsume_quantity, rconsume_date, rconsume_payment_method)
            return jsonify(RConsumes=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def insertRSuppliesJson(self, json):
        sid = json['sid']
        rid = json['rid']
        rsupply_price = json['rsupply_price']
        rsupply_quantity = json['rsupply_quantity']
        rsupply_date = json['rsupply_date']
        if sid and rid and rsupply_price and rsupply_quantity and rsupply_date:
            dao = ResourcesDAO()
            supply_id = dao.insertRSupplies(sid, rid, rsupply_price, rsupply_quantity, rsupply_date)
            result = self.build_rsupplies_attributes(sid, rid, rsupply_price, rsupply_quantity, rsupply_date)
            return jsonify(RSupplies=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


class FoodHandler(ResourcesHandler):
    def build_food_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rbrand'] = row[2]
        result['rnumavailable'] = row[3]
        result['rprice'] = row[4]
        result['rsupplier'] = row[5]
        result['rlocation'] = row[6]
        result['fid'] = row[7]
        result['fname'] = row[8]
        result['fexpdate'] = row[9]
        return result

    def build_food_attributes(self, rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, fid, fname, fexpdate):
        result = {}
        result['rid'] = rid
        result['rtype'] = rtype
        result['rbrand'] = rbrand
        result['rnumavailable'] = rnumavailable
        result['rprice'] = rprice
        result['rsupplier'] = rsupplier
        result['rlocation'] = rlocation
        result['fid'] = fid
        result['fname'] = fname
        result['fexpdate'] = fexpdate
        return result

    def getAllFood(self):
        dao = FoodDAO()
        food_list = dao.getAllFood()
        result_list = []
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food=result_list)

    def getFoodByID(self, fid):
        dao = FoodDAO()
        row = dao.getFoodById(fid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            food = self.build_food_dict(row)
            return jsonify(Food=food)

    def searchFood(self, args):
        #        type = args.get("type")
        location = args.get("location")
        dao = FoodDAO()
        food_list = []
        result_list = []
        if (len(args) == 1) and type:
            food_list = dao.getFoodByName(type)
            for row in food_list:
                result = self.build_food_dict(row)
                result_list.append(result)
        else:
            return jsonify(Error="Malformed query string"), 400

        return jsonify(Food=result_list)

    def insertFood(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            fname = form['fname']
            fbrand = form['fbrand']
            fexpdate = form['fexpdate']
            fsupplier = form['fsupplier']
            fquantity = form['fquantity']
            flocation = form['flocation']
            if fname and fsupplier and fquantity and flocation:
                dao = FoodDAO()
                fid = dao.insert(fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                result = self.build_Food_attr(fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                return jsonify(Food=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertFoodJson(self, json):
        rtype = json['rtype']
        rbrand = json['rbrand']
        rnumavailable = json['rnumavailable']
        rprice = json['rprice']
        rsupplier = json['rsupplier']
        rlocation = json['rlocation']
        fname = json['fname']
        fexpdate = json['fexpdate']
        if rtype and rbrand and rnumavailable and rprice and rsupplier and rlocation and fname and fexpdate:
            dao = ResourcesDAO()
            rid = dao.insert(rtype, rbrand, rnumavailable, rprice)
            rsupplier_id = dao.insertSupplier(rid, rsupplier)
            rlocation_id = dao.insertLocation(rid, rlocation)
            fid = dao.insertFood(rid, fname, fexpdate)
            result = self.build_food_attributes(rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, fid, fname, fexpdate)
            return jsonify(Food=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteFood(self, fid):
        dao = FoodDAO()
        # if not dao.getFoodByID(fid):
        #     return jsonify(Error = "Food not found."), 404
        # else:
        result = dao.delete(fid)
        return jsonify(DeleteStatus=result), 200

    def updateFood(self, fid, form):
        dao = FoodDAO()
        if not dao.getFoodByID(fid):
            return jsonify(Error="Consumer not found."), 404
        else:
            return jsonify(dao.getFoodByID(fid)), 201

    def insertSupplierJson(self, json):
        rtype = json['rtype']
        rbrand = json['rbrand']
        rnumavailable = json['rnumavailable']
        rprice = json['rprice']
        rsupplier = json['rsupplier']
        rlocation = json['rlocation']
        if rtype and rbrand and rnumavailable and rprice and rsupplier and rlocation:
            dao = ResourcesDAO()
            result = dao.insert(rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation)
            return jsonify(Resources=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


class FuelHandler(ResourcesHandler):
    def build_fuel_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rbrand'] = row[2]
        result['rnumavailable'] = row[3]
        result['rprice'] = row[4]
        result['rsupplier'] = row[5]
        result['rlocation'] = row[6]
        result['fuid'] = row[7]
        return result

    def build_fuel_attributes(self, rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, fuelid):
        result = {}
        result['rid'] = rid
        result['rtype'] = rtype
        result['rbrand'] = rbrand
        result['rnumavailable'] = rnumavailable
        result['rprice'] = rprice
        result['rsupplier'] = rsupplier
        result['rlocation'] = rlocation
        result['fuelid'] = fuelid
        return result

    def getAllFuel(self):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

    def getFuelByID(self, fuid):
        dao = FuelDAO()
        row = dao.getFuelByID(fuid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            fuel = self.build_fuel_dict(row)
            return jsonify(Fuel=fuel)

    def searchFuel(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = FuelDAO()
                fuel_list = dao.getFuelByLocation()
                # result_list = []
                # for row in fuel_list:
                #     result = self.build_fuel_dict(row)
                #     result_list.append(row)
                return jsonify(Fuel=fuel_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertFuel(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            # remove fuid later
            # fuid = form['fuid']
            ftype = form['ftype']
            fsupplier = form['fsupplier']
            fquantity = form['fquantity']
            flocation = form['flocation']
            if ftype and fsupplier and fquantity and flocation:
                dao = FuelDAO
                fuid = dao.insert(ftype, fsupplier, fquantity, flocation)
                result = self.build_fuel_attr(fuid, ftype, fsupplier, fquantity, flocation)
                return jsonify(Fuel=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertFuelJson(self, json):
        rtype = json['rtype']
        rbrand = json['rbrand']
        rnumavailable = json['rnumavailable']
        rprice = json['rprice']
        rsupplier = json['rsupplier']
        rlocation = json['rlocation']
        if rtype and rbrand and rnumavailable and rprice and rsupplier and rlocation:
            dao = ResourcesDAO()
            rid = dao.insert(rtype, rbrand, rnumavailable, rprice)
            rsupplier_id = dao.insertSupplier(rid, rsupplier)
            rlocation_id = dao.insertLocation(rid, rlocation)
            fuelid = dao.insertFuel(rid,)
            result = self.build_fuel_attributes(rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, fuelid)
            return jsonify(Fuel=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteFuel(self, fuid):
        dao = FuelDAO()
        if not dao.getFuelByID(fuid):
            return jsonify(Error="Fuel not found."), 404
        else:
            dao.delete(fuid)
            return jsonify(DeleteStatus="OK"), 200

    def updateFuel(self, fuid, form):
        dao = FuelDAO()
        if not dao.getFuelByID(fuid):
            return jsonify(Error="Fuel not found."), 404
        else:
            return jsonify(dao.getFuelByID(fuid)), 201


class EquipmentHandler(ResourcesHandler):
    def build_equipment_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rbrand'] = row[2]
        result['rnumavailable'] = row[3]
        result['rprice'] = row[4]
        result['rsupplier'] = row[5]
        result['rlocation'] = row[6]
        result['eid'] = row[7]
        return result

    def build_equipment_attributes(self, rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, eid):
        result = {}
        result['rid'] = rid
        result['rtype'] = rtype
        result['rbrand'] = rbrand
        result['rnumavailable'] = rnumavailable
        result['rprice'] = rprice
        result['rsupplier'] = rsupplier
        result['rlocation'] = rlocation
        result['eid'] = eid
        return result

    def getAllEquipment(self):
        dao = EquipmentDAO()
        Equipment_list = dao.getAllEquipment()
        result_list = []
        for row in Equipment_list:
            result = self.build_equipment_dict(row)
            result_list.append(result)
        return jsonify(Equipment=result_list)

    def getEquipmentByID(self, eid):
        dao = EquipmentDAO()
        row = dao.getEquipmentByID(eid)
        if not row:
            return jsonify(Error="Equipment Not Found"), 404
        else:
            equipment = self.build_equipment_dict(row)
            return jsonify(Equipment=equipment)

    def searchEquipment(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = EquipmentDAO()
                equipment_list = dao.getEquipByLocation(location)
                # result_list = []
                # for row in equipment_list:
                #     result = self.build_Equipment_dict(row)
                #     result_list.append(row)
                return jsonify(Equipment=equipment_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertEquipment(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            # remove eid later
            eid = form['eid']
            etype = form['etype']
            ebrand = form['ebrand']
            esupplier = form['esupplier']
            equantity = form['equantity']
            elocation = form['elocation']
            if etype and esupplier and equantity and elocation:
                dao = EquipmentDAO
                eid = dao.insert(eid, etype, esupplier, ebrand, equantity, elocation)
                result = self.build_Equipment_attr(eid, etype, esupplier, ebrand, equantity, elocation)
                return jsonify(Equipment=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertEquipmentJson(self, json):
        rtype = json['rtype']
        rbrand = json['rbrand']
        rnumavailable = json['rnumavailable']
        rprice = json['rprice']
        rsupplier = json['rsupplier']
        rlocation = json['rlocation']
        if rtype and rbrand and rnumavailable and rprice and rsupplier and rlocation:
            dao = ResourcesDAO()
            rid = dao.insert(rtype, rbrand, rnumavailable, rprice)
            rsupplier_id = dao.insertSupplier(rid, rsupplier)
            rlocation_id = dao.insertLocation(rid, rlocation)
            eid = dao.insertEquipment(rid,)
            result = self.build_equipment_attributes(rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, eid)
            return jsonify(Equipment=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteEquipment(self, eid):
        dao = EquipmentDAO()
        result = dao.delete(eid)
        # if not dao.getEquipByID(eid):
        #     return jsonify(Error = "Equipment not found."), 404
        # else:
        #     dao.delete(eid)
        return jsonify(DeleteStatus=result), 200

    def updateEquipment(self, eid, form):
        dao = EquipmentDAO()
        if not dao.getEquipByID(eid):
            return jsonify(Error="Equiment not found."), 404
        else:
            return jsonify(dao.getEquipByID(eid)), 201


class MedDevHandler(ResourcesHandler):
    def build_MedDev_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rbrand'] = row[2]
        result['rnumavailable'] = row[3]
        result['rprice'] = row[4]
        result['rsupplier'] = row[5]
        result['rlocation'] = row[6]
        result['mdid'] = row[7]
        return result

    def build_MedDev_attr(self, rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, mdid):
        result = {}
        result['rid'] = rid
        result['rtype'] = rtype
        result['rbrand'] = rbrand
        result['rnumavailable'] = rnumavailable
        result['rprice'] = rprice
        result['rsupplier'] = rsupplier
        result['rlocation'] = rlocation
        result['mdid'] = mdid
        return result

    def getAllMedDev(self):
        dao = MedDevDAO()
        medDev_list = dao.getAllMedicalDevices()
        result_list = []
        for row in medDev_list:
            result = self.build_MedDev_dict(row)
            result_list.append(result)
        return jsonify(MedicalDevices=result_list)

    def getMedDevByID(self, mdid):
        dao = MedDevDAO()
        row = dao.getMedicalDevicesByID(mdid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            medDev = self.build_MedDev_dict(row)
            return jsonify(MedicalDevices=medDev)

    def searchMedDev(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = MedDevDAO()
                MedDev_list = dao.getMedDevByLocation(location)
                # result_list = []
                # for row in MedDev_list:
                #     result = self.build_MedDev_dict(row)
                #     result_list.append(row)
                return jsonify(MedDev=MedDev_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertMedDev(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            # remove mdid later
            # mdid = form['mdid']
            mdtype = form['mdtype']
            mdbrand = form['mdbrand']
            mdsupplier = form['mdsupplier']
            mdquantity = form['mdquantity']
            mdlocation = form['mdlocation']
            if mdtype and mdsupplier and mdquantity and mdlocation and mdlocation:
                dao = MedDevDAO()
                mdid = dao.insert(mdtype, mdsupplier, mdbrand, mdquantity, mdlocation)
                result = self.build_MedDev_attr(mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation)
                return jsonify(MedDev=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertMedDevJson(self, json):
        rtype = json['rtype']
        rbrand = json['rbrand']
        rnumavailable = json['rnumavailable']
        rprice = json['rprice']
        rsupplier = json['rsupplier']
        rlocation = json['rlocation']
        if rtype and rbrand and rnumavailable and rprice and rsupplier and rlocation:
            dao = ResourcesDAO()
            rid = dao.insert(rtype, rbrand, rnumavailable, rprice)
            rsupplier_id = dao.insertSupplier(rid, rsupplier)
            rlocation_id = dao.insertLocation(rid, rlocation)
            mdid = dao.insertMedicalDevices(rid, )
            result = self.build_MedDev_attr(rid, rtype, rbrand, rnumavailable, rprice, rsupplier,
                                            rlocation, mdid)
            return jsonify(Medical_Devices=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteMedDev(self, mdid):
        dao = MedDevDAO()
        # if not dao.getMedDevByID(mdid):
        #     return jsonify(Error = "MedDev not found."), 404
        # else:
        result = dao.delete(mdid)
        return jsonify(DeleteStatus=result), 200

    def updateMedDev(self, mdid, form):
        dao = MedDevDAO()
        if not dao.getMedDevByID(mdid):
            return jsonify(Error="Consumer not found."), 404
        else:
            return jsonify(dao.getMedDevByID(mdid)), 201


class MedicationHandler(ResourcesHandler):
    def build_Med_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rbrand'] = row[2]
        result['rnumavailable'] = row[3]
        result['rprice'] = row[4]
        result['rsupplier'] = row[5]
        result['rlocation'] = row[6]
        result['mid'] = row[7]
        result['mexpdate'] = row[8]
        result['mclass'] = row[9]
        return result

    def build_medication_attributes(self, rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, mid, mexpdate, mclass):
        result = {}
        result['rid'] = rid
        result['rtype'] = rtype
        result['rbrand'] = rbrand
        result['rnumavailable'] = rnumavailable
        result['rprice'] = rprice
        result['rsupplier'] = rsupplier
        result['rlocation'] = rlocation
        result['mid'] = mid
        result['mexpdate'] = mexpdate
        result['mclass'] = mclass
        return result

    def getAllMedication(self):
        dao = MedicationDAO()
        medication_list = dao.getAllMedication()
        result_list = []
        for row in medication_list:
            result = self.build_Med_dict(row)
            result_list.append(result)
        return jsonify(Medication=medication_list)

    def getMedByID(self, mid):
        dao = MedicationDAO()
        result = dao.getMedicationByID(mid)
        # if not row:
        #     return jsonify(Error = "Med Not Found"), 404
        # else:
        #     Med = self.build_Med_dict(row)
        return jsonify(Med=result)

    def searchMed(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = MedicationDAO()
                Med_list = dao.getMedByLocation(location)
                # result_list = []
                # for row in Med_list:
                #     result = self.build_Med_dict(row)
                #     result_list.append(row)
                return jsonify(Med=Med_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertMed(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            # remove mid later
            mname = form['mname']
            mbrand = form['mbrand']
            mexpdate = form['mexpdate']
            msupplier = form['msupplier']
            mquantity = form['mquantity']
            mlocation = form['mlocation']
            if mname and mexpdate and msupplier and mbrand and mquantity and mlocation:
                dao = MedicationDAO()
                result = dao.insert(mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
                return jsonify(Med=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertMedicationJson(self, json):
        rtype = json['rtype']
        rbrand = json['rbrand']
        rnumavailable = json['rnumavailable']
        rprice = json['rprice']
        rsupplier = json['rsupplier']
        rlocation = json['rlocation']
        mexpdate = json['mexpdate']
        mclass = json['mclass']
        if rtype and rbrand and rnumavailable and rprice and rsupplier and rlocation and mexpdate and mclass:
            dao = ResourcesDAO()
            rid = dao.insert(rtype, rbrand, rnumavailable, rprice)
            rsupplier_id = dao.insertSupplier(rid, rsupplier)
            rlocation_id = dao.insertLocation(rid, rlocation)
            mid = dao.insertMedication(rid, mexpdate, mclass)
            result = self.build_medication_attributes(rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, mid,
                                                mexpdate, mclass)
            return jsonify(Medication=result), 201
        else:
            return jsonify(Medication="Unexpected attributes in post request"), 400

    def deleteMed(self, mid):
        dao = MedicationDAO()
        result = dao.delete(mid)
        return jsonify(DeleteStatus=result), 200

    def updateMed(self, mid, form):
        dao = MedicationDAO()
        if not dao.getMedByID(mid):
            return jsonify(Error="Medication not found."), 404
        else:
            return jsonify(dao.getMedByID(mid)), 201


class WaterHandler(ResourcesHandler):
    def build_water_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rbrand'] = row[2]
        result['rnumavailable'] = row[3]
        result['rprice'] = row[4]
        result['rsupplier'] = row[5]
        result['rlocation'] = row[6]
        result['wid'] = row[7]
        result['wvolume'] = row[8]
        result['wexpdate'] = row[9]
        return result

    def build_water_attributes(self, rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, wid, wvolume, wexpdate):
        result = {}
        result['rid'] = rid
        result['rtype'] = rtype
        result['rbrand'] = rbrand
        result['rnumavailable'] = rnumavailable
        result['rprice'] = rprice
        result['rsupplier'] = rsupplier
        result['rlocation'] = rlocation
        result['wid'] = wid
        result['wvolume'] = wvolume
        result['wexpdate'] = wexpdate
        return result

    def getAllWater(self):
        dao = WaterDAO()
        water_list = dao.getAllWater()
        result_list = []
        for row in water_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return jsonify(Water=result_list)

    def getWaterByID(self, wid):
        dao = WaterDAO()
        row = dao.getWaterByID(wid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            water = self.build_water_dict(row)
            return jsonify(Water=water)


    def searchWater(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = FoodDAO()
                Water_list = dao.getWaterByLocation(location)
                # result_list = []
                # for row in Food_list:
                #     result = self.build_Water_dict(row)
                #     result_list.append(row)
                return jsonify(Water=Water_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertWater(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            fname = form['fname']
            fbrand = form['fbrand']
            fexpdate = form['fexpdate']
            fsupplier = form['fsupplier']
            fquantity = form['fquantity']
            flocation = form['flocation']
            if fname and fsupplier and fquantity and flocation:
                dao = WaterDAO()
                wid = dao.insert(fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                result = self.build_Water_attr(wid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                return jsonify(Water=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertWaterJson(self, json):
        rtype = json['rtype']
        rbrand = json['rbrand']
        rnumavailable = json['rnumavailable']
        rprice = json['rprice']
        rsupplier = json['rsupplier']
        rlocation = json['rlocation']
        wvolume = json['wvolume']
        wexpdate = json['wexpdate']
        if rtype and rbrand and rnumavailable and rprice and rsupplier and rlocation and wvolume and wexpdate:
            dao = ResourcesDAO()
            rid = dao.insert(rtype, rbrand, rnumavailable, rprice)
            rsupplier_id = dao.insertSupplier(rid, rsupplier)
            rlocation_id = dao.insertLocation(rid, rlocation)
            wid = dao.insertWater(rid, wvolume, wexpdate)
            result = self.build_water_attributes(rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, wid,
                                                wvolume, wexpdate)
            return jsonify(Water=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteWater(self, fid):
        dao = WaterDAO()
        # if not dao.getWaterByID(fid):
        #     return jsonify(Error = "Water not found."), 404
        # else:
        result = dao.delete(fid)
        return jsonify(DeleteStatus=result), 200

    def updateWater(self, fid, form):
        dao = WaterDAO()
        if not dao.getWaterByID(fid):
            return jsonify(Error="Consumer not found."), 404
        else:
            return jsonify(dao.getWaterByID(fid)), 201


class ClothingHandler(ResourcesHandler):
    def build_clothing_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rbrand'] = row[2]
        result['rnumavailable'] = row[3]
        result['rprice'] = row[4]
        result['rsupplier'] = row[5]
        result['rlocation'] = row[6]
        result['clothes_id'] = row[7]
        result['cpiece'] = row[8]
        result['csex'] = row[9]
        result['csize'] = row[10]
        return result

    def build_clothing_attributes(self, rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, cid, cpiece, csex,
                            csize):
        result = {}
        result['rid'] = rid
        result['rtype'] = rtype
        result['rbrand'] = rbrand
        result['rnumavailable'] = rnumavailable
        result['rprice'] = rprice
        result['rsupplier'] = rsupplier
        result['rlocation'] = rlocation
        result['clothes_id'] = cid
        result['cpiece'] = cpiece
        result['csex'] = csex
        result['csize'] = csize
        return result

    def getAllClothing(self):
        dao = ClothingDAO()
        clothing_list = dao.getAllClothing()
        result_list = []
        for row in clothing_list:
            result = self.build_clothing_dict(row)
            result_list.append(result)
        return jsonify(Clothing=result_list)

    def getClothingByID(self, cl_id):
        dao = ClothingDAO()
        row = dao.getClothingByID(cl_id)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            clothing = self.build_clothing_dict(row)
            return jsonify(Clothing=clothing)

    def searchClothing(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = ClothingDAO()
                Clothing_list = dao.getClothingByLocation(location)
                # result_list = []
                # for row in Clothing_list:
                #     result = self.build_Clothing_dict(row)
                #     result_list.append(row)
                return jsonify(Clothing=Clothing_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertClothing(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            fname = form['fname']
            fbrand = form['fbrand']
            fexpdate = form['fexpdate']
            fsupplier = form['fsupplier']
            fquantity = form['fquantity']
            flocation = form['flocation']
            if fname and fsupplier and fquantity and flocation:
                dao = ClothingDAO()
                fid = dao.insert(fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                result = self.build_Clothing_attr(fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                return jsonify(Clothing=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertClothingJson(self, json):
        rtype = json['rtype']
        rbrand = json['rbrand']
        rnumavailable = json['rnumavailable']
        rprice = json['rprice']
        rsupplier = json['rsupplier']
        rlocation = json['rlocation']
        cpiece = json['cpiece']
        csex = json['csex']
        csize = json['csize']
        if rtype and rbrand and rnumavailable and rprice and rsupplier and rlocation and cpiece and csex and csize:
            dao = ResourcesDAO()
            rid = dao.insert(rtype, rbrand, rnumavailable, rprice)
            rsupplier_id = dao.insertSupplier(rid, rsupplier)
            rlocation_id = dao.insertLocation(rid, rlocation)
            clothes_id = dao.insertClothing(rid, cpiece, csex, csize)
            result = self.build_clothing_attributes(rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation,
                                                      clothes_id, cpiece, csex, csize)
            return jsonify(Clothing=result), 201
        else:
            return jsonify(Clothing="Unexpected attributes in post request"), 400

    def deleteClothing(self, fid):
        dao = ClothingDAO()
        # if not dao.getClothingByID(fid):
        #     return jsonify(Error = "Clothing not found."), 404
        # else:
        result = dao.delete(fid)
        return jsonify(DeleteStatus=result), 200

    def updateClothing(self, fid, form):
        dao = ClothingDAO()
        if not dao.getClothingByID(fid):
            return jsonify(Error="Consumer not found."), 404
        else:
            return jsonify(dao.getClothingByID(fid)), 201

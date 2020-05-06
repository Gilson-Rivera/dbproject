from flask import jsonify
from dao.resources import FuelDAO


class FuelHandler:
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

    def build_fuel_attr(self, rid, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation, fuid):
        result = {}
        result['rid'] = rid
        result['rtype'] = rtype
        result['rbrand'] = rbrand
        result['rnumavailable'] = rnumavailable
        result['rprice'] = rprice
        result['rsupplier'] = rsupplier
        result['rlocation'] = rlocation
        result['fuid'] = fuid
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
            fuel_list = dao.getFuelByLocation(location)
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
    ftype = json['ftype']
    fsupplier = json['fsupplier']
    fquantity = json['fquantity']
    flocation = json['flocation']
    if ftype and fsupplier and fquantity and flocation:
        dao = FuelDAO()
        result = dao.insert(ftype, fsupplier, fquantity, flocation)
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

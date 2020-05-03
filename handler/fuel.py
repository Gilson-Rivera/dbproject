from flask import jsonify
from dao.fuel import FuelDAO

class FuelHandler:
    def build_fuel_dict(self, row):
        result = {}
        result['fuid'] = row[0]
        result['ftype'] = row[1]
        result['fsupplier'] = row[2]
        result['fnumavailable'] = row[3]
        result['flocation'] = row[4]

    def build_fuel_attr(self, fuid, ftype, fsupplier, fquantity, flocation):
        result = {}
        result['fuid'] = fuid
        result['ftype'] = ftype
        result['fsupplier'] = fsupplier
        result['fquantity'] = fquantity
        result['flocation'] = flocation
        return result

    def getAllFuel(self):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        return jsonify(Fuel=fuel_list)

    def getFuelByID(self, fuid):
        dao = FuelDAO()
        result = dao.getFuelByID()
        return jsonify(Fuel=result)

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
            return jsonify(Error = "Malformed post request"), 400
        else:
            #remove fuid later
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
            return jsonify(Error = "Fuel not found."), 404
        else:
            dao.delete(fuid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateFuel(self, fuid, form):
        dao = FuelDAO()
        if not dao.getFuelByID(fuid):
            return jsonify(Error="Fuel not found."), 404
        else:
            return jsonify(dao.getFuelByID(fuid)), 201

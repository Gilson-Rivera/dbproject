from flask import jsonify
from dao.resources import WaterDAO

class WaterHandler:
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

    def build_water_consumed_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['wid'] = row[1]
        result['cfirstname'] = row[2]
	result['clastname'] = row[3]
        result['wname'] = row[4]
        result['wbrand'] = row[5]
        result['wconsume_price'] = row[6]
        result['wconsume_quantity'] = row[7]
        result['wconsume_date'] = row[8]
        return result

    def build_Water_attr(self, wid, wname, wexpdate, wsupplier, wbrand, wquantit$
         result = {}
	return result

    def getAllWaters(self):
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

#    def searchWater(self, args):
#        type = args.get("type")
#        status = args.get("status")  #reserved or purchased
#        location = args.get("location")
#        dao = MedDAO()
#        medications_list = []
#        result_list = []
#        if (len(args) == 1) and type:
#            medications_list = dao.getMedicationByType(type)
#            for row in medications_list:
#                result = self.build_medication_dict(row)
#                result_list.append(result)
#	else:
#            return jsonify(Error="Malformed query string"), 400
#
#        return jsonify(Medications=result_list)

     def insertWater(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            #remove wid later
            wname = form['wname']
            wbrand = form['wbrand']
            wexpdate = form['wexpdate']
            wsupplier = form['wsupplier']
            wquantity = form['wquantity']
            wlocation = form['wlocation']
            if wname and wexpdate and wsupplier and wbrand and wquantity and wlocation:
                dao = WaterDAO()
                result = dao.insert(wname, wexpdate, wsupplier, wbrand, wquant$
                return jsonify(Water=result), 201
            else:
		return jsonify(Error="Unexpected attributes in post request"),$

    def insertWaterJson(self, json):
        wname = json['wname']
        wexpdate = json['wexpdate']
        wsupplier = json['wsupplier']
        wbrand = json['wbrand']
        wquantity = json['wquantity']
        wlocation = json['wlocation']
        if wname and wexpdate and wsupplier and wbrand and wquantity and wlocation:
            dao = WaterDAO()

     result = dao.insert(wname, wexpdate, wsupplier, wbrand, wquantity, wlocation)
            return jsonify(Water=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteWater(self, wid):
        dao = WaterDAO()
        result = dao.delete(wid)
        return jsonify(DeleteStatus = result), 200

    def updateWater(self, wid, form):
        dao = WaterDAO()
	if not dao.getWaterByID(wid):
            return jsonify(Error="Medication not found."), 404
        else:
            return jsonify(dao.getWaterByID(wid)), 201


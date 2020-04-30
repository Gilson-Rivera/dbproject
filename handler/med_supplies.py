from flask import jsonify
from dao.med_supplies import MedSuppliesDAO

class MedSuppliesHandler:
    def build_med_supplies_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sorganization'] = row[1]
        result['mid'] = row[2]
        result['mname'] = row[3]
        result['msupply_price'] = row[4]
        result['msupply_quantity'] = row[5]
        result['msupply_date'] = row[6]
        return result

    def build_Med_attr(self, fuid, stype, Medsupply_price, Medsupply_date, Medsupply_quantity):
        result = {}
        result['Medid'] = fuid
        result['stype'] = stype
        result['Medsupply_price'] = Medsupply_price
        result['Medsupply_date'] = Medsupply_date
        result['Medsupply_quantity'] = Medsupply_quantity
        return result

    def getAllMedSupplies(self):
        dao = MedSuppliesDAO()
        food_list = dao.getAllMedSupplies()
        result_list = []
        for row in food_list:
            result = self.build_med_supplies_dict(row)
            result_list.append(result)
        return jsonify(Medication_Supplies=result_list)

    def getMedById(self, mid):
        dao = MedSuppliesDAO()
        result = dao.getMedDevById(mid)
        return jsonify(MedSupplies=result)

    def searchMedSupplies(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            date = args.get("date")
            price = args.get("price")
            if date:
                dao = MedSuppliesDAO()
                result_list = dao.getMedSupplyByDate(date)
                return jsonify(MedSupplies=result_list)

            elif price:
                dao = MedSuppliesDAO()
                result_list = dao.getMedSupplyByPrice(price)
                return jsonify(MedSupplies=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400


    def insertMedSuppliesJson(self, json):
        Medsupply_price = json['Medsupply_price']
        Medsupply_date = json['Medsupply_date']
        Medsupply_quantity = json['Medsupply_quantity']
        if Medsupply_price and Medsupply_quantity and Medsupply_date:
            dao = MedSuppliesDAO()
            result = dao.insert(Medsupply_price, Medsupply_quantity, Medsupply_date)
            return jsonify(Med_Supply=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
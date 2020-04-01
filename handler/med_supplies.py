from flask import jsonify
from dao.med_supplies import MedSuppliesDAO

class MedSuppliesHandler:
    def build_Med_supplies_dict(self, row):
        result = {}
        result['Medid'] = row[0]
        result['sid'] = row[1]
        result['Medsupply_price'] = row[2]
        result['Medsupply_date'] = row[3]
        result['Medsupply_quantity'] = row[4]

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
        result_list = dao.getAllMedSupplies()
        return jsonify(MedSupplies=result_list)

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
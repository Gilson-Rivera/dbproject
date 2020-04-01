from flask import jsonify
from dao.esupplies import EquipmentSuppliesDAO

class ESuppliesHandler:
    def build_e_supplies_dict(self, row):
        result = {}
        result['eid'] = row[0]
        result['sid'] = row[1]
        result['esupply_price'] = row[2]
        result['esupply_date'] = row[3]
        result['esupply_quantity'] = row[4]

    def build_e_attr(self, fuid, stype, esupply_price, esupply_date, esupply_quantity):
        result = {}
        result['eid'] = fuid
        result['stype'] = stype
        result['esupply_price'] = esupply_price
        result['esupply_date'] = esupply_date
        result['esupply_quantity'] = esupply_quantity
        return result

    def getAllESupplies(self):
        dao = EquipmentSuppliesDAO()
        result_list = dao.getAllESupplies()
        return jsonify(EquipmentSupplies=result_list)

    def searchESupplies(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            date = args.get("date")
            price = args.get("price")
            if date:
                dao = EquipmentSuppliesDAO()
                result_list = dao.getESupplyByDate(date)
                return jsonify(EquipmentSupplies=result_list)

            elif price:
                dao = EquipmentSuppliesDAO()
                result_list = dao.getESupplyByPrice(price)
                return jsonify(EquipmentSupplies=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertESuppliesJson(self, json):
        esupply_price = json['esupply_price']
        esupply_date = json['esupply_date']
        esupply_quantity = json['esupply_quantity']
        if esupply_price and esupply_quantity and esupply_date:
            dao = EquipmentSuppliesDAO()
            result = dao.insert(esupply_price, esupply_quantity, esupply_date)
            return jsonify(E_Supply=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

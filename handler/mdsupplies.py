from flask import jsonify
from dao.mdsupplies import MDSuppliesDAO

class MDSuppliesHandler:
    def build_md_supplies_dict(self, row):
        result = {}
        result['mdid'] = row[0]
        result['sid'] = row[1]
        result['mdsupply_price'] = row[2]
        result['mdsupply_date'] = row[3]
        result['mdsupply_quantity'] = row[4]

    def build_md_attr(self, mdid, stype, mdsupply_price, mdsupply_date, mdsupply_quantity):
        result = {}
        result['mdid'] = mdid
        result['stype'] = stype
        result['mdsupply_price'] = mdsupply_price
        result['mdsupply_date'] = mdsupply_date
        result['mdsupply_quantity'] = mdsupply_quantity
        return result

    def getAllMDSupplies(self):
        dao = MDSuppliesDAO()
        result_list = dao.getAllMDSupplies()
        return jsonify(MDSupplies=result_list)

    def searchMDSupplies(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            date = args.get("date")
            price = args.get("price")
            if date:
                dao = MDSuppliesDAO()
                result_list = dao.getMDSupplyByDate(date)
                return jsonify(MDSupplies=result_list)

            elif price:
                dao = MDSuppliesDAO()
                result_list = dao.getMDSupplyByPrice(price)
                return jsonify(MDSupplies=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400
    def insertMDSuppliesJson(self, json):
        mdsupply_price = json['mdsupply_price']
        mdsupply_date = json['mdsupply_date']
        mdsupply_quantity = json['mdsupply_quantity']
        if mdsupply_price and mdsupply_quantity and mdsupply_date:
            dao = MDSuppliesDAO()
            result = dao.insert(mdsupply_price, mdsupply_quantity, mdsupply_date)
            return jsonify(MD_Supply=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

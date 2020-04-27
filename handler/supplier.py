from flask import jsonify
from dao.supplier import SupplierDAO


class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sfirstname'] = row[1]
        result['slastname'] = row[2]
        result['sorganization'] = row[3]
        result['slocation'] = row[4]
        result['sphone'] = row[5]
        return result

    def getAllSuppliers(self):
        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, sid):
        dao = SupplierDAO()
        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            supplier = self.build_supplier_dict(row)
            return jsonify(Supplier=supplier)


    def searchSuppliers(self, args):
        location = args.get("location")
        dao = SupplierDAO()
        suppliers_list = []
        if (len(args) == 1) and location:
            suppliers_list = dao.getSuppliersByLocation(location)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def insertSupplierJson(self, json):
        sfirstname = json['sfirstname']
        slastname = json['slastname']
        sorganization = json['sorganization']
        sphone = json['sphone']
        slocation = json['slocation']
        if sfirstname and slastname and sorganization and sphone and slocation:
            dao = SupplierDAO()
            result = dao.insert(sfirstname, slastname, sorganization, sphone, slocation)
            return jsonify(Supplier=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400



from flask import jsonify
from dao.supplier import SupplierDAO


class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['scity'] = row[2]
        result['sphone'] = row[3]
        return result

    def build_part_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pname'] = row[1]
        result['pmaterial'] = row[2]
        result['pcolor'] = row[3]
        result['pprice'] = row[4]
        result['quantity'] = row[5]
        return result

    def getAllSuppliers(self):
        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        return jsonify(Suppliers=suppliers_list)

    def getSupplierById(self, sid):
        dao = SupplierDAO()
        result = dao.getSupplierById(sid)
        return jsonify(Supplier=result)

    def getPartsBySupplierId(self, sid):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier Not Found"), 404
        parts_list = dao.getPartsBySupplierId(sid)
        result_list = []
        for row in parts_list:
            result = self.build_part_dict(row)
            result_list.append(result)
        return jsonify(PartsSupply=result_list)

    def searchSuppliers(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            organization = args.get("organization")
            if organization:
                dao = SupplierDAO()
                supplier_list = dao.getSuppliersByOrganization(organization)
                result_list = []
                return jsonify(Suppliers=supplier_list)
            else:
                return jsonify(Error="Malformed search string."), 400

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

from flask import jsonify
from dao.resources import EquipmentDAO

class EquipHandler:
    def build_Equipment_dict(self, row):
        result = {}
        result['eid'] = row[0]
        result['etype'] = row[1]
        result['esupplier'] = row[2]
        result['ebrand'] = row[3]
        result['equantity'] = row[4]
        result['elocation'] = row[5]

    def build_Equipment_attr(self, eid, etype, esupplier, ebrand, equantity, elocation):
        result = {}
        result['eid'] = eid
        result['etype'] = etype
        result['esupplier'] = esupplier
        result['ebrand'] = ebrand
        result['equantity'] = equantity
        result['elocation'] = elocation
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
            return jsonify(Error = "Equipment Not Found"), 404
        else:
            equipment = self.build_equipment_dict(row)
        return jsonify(Equipment = equipment)


    def searchEquipment(self, args):
        type = args.get("type")
        location = args.get("location")
        dao = EquipmentDAO()
        equipment_list = []
        result_list = []
        if (len(args) == 1) and type:
#            equipment_list = dao.getEquipmentByType(type)
            for row in equipment_list:
                result = self.build_equipment_dict(row)
                result_list.append(result)
        else:
            return jsonify(Error="Malformed query string"), 400

        return jsonify(Equipment=result_list)


    def insertEquipment(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            #remove eid later
            eid = form['eid']
            etype = form['etype']
            ebrand = form['ebrand']
            esupplier = form['esupplier']
            equantity = form['equantity']
            elocation = form['elocation']
            if etype and esupplier and equantity and elocation:
                dao = EquipmentDAO()
                result = dao.insert(eid, etype, esupplier, ebrand, equantity, elocation)
                return jsonify(Equipment=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def insertEquipmentJson(self, json):
        eid = json['eid']
        etype = json['etype']
        esupplier = json['esupplier']
        ebrand = json['ebrand']
        equantity = json['equantity']
        elocation = json['elocation']
        if eid and etype and esupplier and equantity and elocation:
            dao = EquipmentDAO()
            result = dao.insert(eid, etype, esupplier, ebrand, equantity, elocation)
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
        return jsonify(DeleteStatus = result), 200

    def updateEquipment(self, eid, form):
        dao = EquipmentDAO()
        if not dao.getEquipByID(eid):
            return jsonify(Error="Equiment not found."), 404
        else:
            return jsonify(dao.getEquipByID(eid)), 201

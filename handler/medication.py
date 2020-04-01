from flask import jsonify
from dao.medication import MedDAO

class MedHandler:
    def build_Med_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['mname'] = row[1]
        result['mexpdate'] = row[2]
        result['msupplier'] = row[3]
        result['mbrand'] = row[4]
        result['mquantity'] = row[5]
        result['mlocation'] = row[6]

    def build_Med_attr(self, mid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation):
        result = {}
        result['mid'] = mid
        result['mname'] = mname
        result['mexpdate'] = mexpdate
        result['msupplier'] = msupplier
        result['mbrand'] = mbrand
        result['mquantity'] = mquantity
        result['mlocation'] = mlocation
        return result

    def getAllMed(self):
        dao = MedDAO()
        Med_list = dao.getAllMed()
        result_list = []
        for row in Med_list:
            result = self.build_Med_dict(row)
            result_list.append(result)
        return jsonify(Med=Med_list)

    def getMedByID(self, mid):
        dao = MedDAO()
        result = dao.getMedByID(mid)
        # if not row:
        #     return jsonify(Error = "Med Not Found"), 404
        # else:
        #     Med = self.build_Med_dict(row)
        return jsonify(Med = result)


    def searchMed(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = MedDAO()
                Med_list = dao.getMedByLocation(location)
                # result_list = []
                # for row in Med_list:
                #     result = self.build_Med_dict(row)
                #     result_list.append(row)
                return jsonify(Med=Med_list)
            else:
                return jsonify(Error="Malformed search string."), 400


    def insertMed(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            #remove mid later
            mname = form['mname']
            mbrand = form['mbrand']
            mexpdate = form['mexpdate']
            msupplier = form['msupplier']
            mquantity = form['mquantity']
            mlocation = form['mlocation']
            if mname and mexpdate and msupplier and mbrand and mquantity and mlocation:
                dao = MedDAO()
                result = dao.insert(mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
                return jsonify(Med=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def insertMedJson(self, json):
        mname = json['mname']
        mexpdate = json['mexpdate']
        msupplier = json['msupplier']
        mbrand = json['mbrand']
        mquantity = json['mquantity']
        mlocation = json['mlocation']
        if mname and mexpdate and msupplier and mbrand and mquantity and mlocation:
            dao = MedDAO()
            result = dao.insert(mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
            return jsonify(Med=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteMed(self, mid):
        dao = MedDAO()
        result = dao.delete(mid)
        return jsonify(DeleteStatus = result), 200

    def updateMed(self, mid, form):
        dao = MedDAO()
        if not dao.getMedByID(mid):
            return jsonify(Error="Consumer not found."), 404
        else:
            return jsonify(dao.getMedByID(mid)), 201
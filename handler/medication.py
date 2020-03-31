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
        return jsonify(Med=Med_list)

    def getMedByID(self, mid):
        dao = MedDAO()
        row = dao.getMedByID()
        if not row:
            return jsonify(Error = "Med Not Found"), 404
        else:
            Med = self.build_Med_dict(row)
            return jsonify(Med = Med)


    def searchMed(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = MedDAO()
                Med_list = dao.getMedByLocation()
                result_list = []
                for row in Med_list:
                    result = self.build_Med_dict(row)
                    result_list.append(row)
                return jsonify(Med=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400


    def insertMed(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            #remove mid later
            mid = form['mid']
            mname = form['mname']
            mbrand = form['mbrand']
            mexpdate = form['mexpdate']
            msupplier = form['msupplier']
            mquantity = form['mquantity']
            mlocation = form['mlocation']
            if mname and msupplier and mquantity and mlocation:
                dao = MedDAO
                mid = dao.insert(mid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
                result = self.build_Med_attr(mid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
                return jsonify(Med=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def insertMedJson(self, json):
        mid = json['mid']
        mname = json['mname']
        mexpdate = json['mexpdate']
        msupplier = json['msupplier']
        mbrand = json['mbrand']
        mquantity = json['mquantity']
        mlocation = json['mlocation']
        if mid and mname and mexpdate and msupplier and mquantity and mlocation:
            dao = MedDAO
            mid = dao.insert(mid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
            result = self.build_Med_attr(mid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
            return jsonify(Med=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteMed(self, mid):
        dao = MedDAO()
        if not dao.getMedByID(mid):
            return jsonify(Error = "Med not found."), 404
        else:
            dao.delete(mid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateMed(self, mid, form):
        dao = MedDAO()
        if not dao.getMedByID(mid):
            return jsonify(Error = "Med not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                mid = form['mid']
                mname = form['mname']
                mexpdate = form['mexpdate']
                mbrand = form['mbrand']
                msupplier = form['msupplier']
                mquantity = form['mquantity']
                mlocation = form['mlocation']
                if mname and mexpdate and mbrand and msupplier and mquantity and mlocation:
                    dao.update(mid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
                    result = self.build_Med_attr(mid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
                    return jsonify(Med=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
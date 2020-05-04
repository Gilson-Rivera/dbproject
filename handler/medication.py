from flask import jsonify
from dao.medication import MedDAO

class MedHandler:
    def build_medication_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rbrand'] = row[2]
        result['rnumavailable'] = row[3]
        result['rprice'] = row[4]
        result['rsupplier'] = row[5]
        result['rlocation'] = row[6]
        result['mid'] = row[7]
        result['mexpdate'] = row[8]
        result['mclass'] = row[9]
        return result

    def build_medication_consumed_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['mid'] = row[1]
        result['cfirstname'] = row[2]
        result['clastname'] = row[3]
        result['mname'] = row[4]
        result['mbrand'] = row[5]
        result['mconsume_price'] = row[6]
        result['mconsume_quantity'] = row[7]
        result['mconsume_date'] = row[8]
        return result

    def build_Med_attr(self, mid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation):
         result = {}
        # result['mid'] = mid
        # result['mname'] = mname
        # result['mexpdate'] = mexpdate
        # result['mnumavailable'] = mexpdate
        # result['msupplier'] = msupplier
        # result['mbrand'] = mbrand
        # result['mquantity'] = mquantity
        # result['mlocation'] = mlocation
         return result

    def getAllMedications(self):
        dao = MedDAO()
        medications_list = dao.getAllMedications()
        result_list = []
        for row in medications_list:
            result = self.build_medication_dict(row)
            result_list.append(result)
        return jsonify(Medications=result_list)

    def getMedicationByID(self, mid):
        dao = MedDAO()
        row = dao.getMedicationByID(mid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            medication = self.build_medication_dict(row)
            return jsonify(Medication=medication)


    def searchMedications(self, args):
        type = args.get("type")
        status = args.get("status")  #reserved or purchased
        location = args.get("location")
        dao = MedDAO()
        medications_list = []
        result_list = []
        if (len(args) == 1) and type:
            medications_list = dao.getMedicationByType(type)
            for row in medications_list:
                result = self.build_medication_dict(row)
                result_list.append(result)
        # elif (len(args) == 1) and status:
        #     medications_list = dao.getMedicationByStatus(status)
        #     for row in medications_list:
        #         result = self.build_medication_consumed_dict(row) #also need to add consumer's information
        #         result_list.append(result)
        elif (len(args) == 1) and location:
            medications_list = dao.getMedicationByLocation(location)
            for row in medications_list:
                result = self.build_medication_dict(row)
                result_list.append(result)
        else:
            return jsonify(Error="Malformed query string"), 400

        return jsonify(Medications=result_list)


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


    def insertMedicationJson(self, json):
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
            return jsonify(Error="Medication not found."), 404
        else:
            return jsonify(dao.getMedByID(mid)), 201
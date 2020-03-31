from flask import jsonify
from dao.medical_devices import MedDevDAO

class MedDevHandler:
    def build_MedDev_dict(self, row):
        result = {}
        result['mdid'] = row[0]
        result['mdtype'] = row[1]
        result['mdsupplier'] = row[2]
        result['mdbrand'] = row[3]
        result['mdquantity'] = row[4]
        result['mdlocation'] = row[5]

    def build_MedDev_attr(self, mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation):
        result = {}
        result['mdid'] = mdid
        result['mdtype'] = mdtype
        result['mdsupplier'] = mdsupplier
        result['mdbrand'] = mdbrand
        result['mdquantity'] = mdquantity
        result['mdlocation'] = mdlocation
        return result

    def getAllMedDev(self):
        dao = MedDevDAO()
        MedDev_list = dao.getAllMedDev()
        return jsonify(MedDev=MedDev_list)

    def getMedDevByID(self, mdid):
        dao = MedDevDAO()
        row = dao.getMedDevByID()
        if not row:
            return jsonify(Error = "MedDev Not Found"), 404
        else:
            MedDev = self.build_MedDev_dict(row)
            return jsonify(MedDev = MedDev)


    def searchMedDev(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = MedDevDAO()
                MedDev_list = dao.getMedDevByLocation()
                result_list = []
                for row in MedDev_list:
                    result = self.build_MedDev_dict(row)
                    result_list.append(row)
                return jsonify(MedDev=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400


    def insertMedDev(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            #remove mdid later
            mdid = form['mdid']
            mdtype = form['mdtype']
            mdbrand = form['mdbrand']
            mdsupplier = form['mdsupplier']
            mdquantity = form['mdquantity']
            mdlocation = form['mdlocation']
            if mdtype and mdsupplier and mdquantity and mdlocation:
                dao = MedDevDAO
                mdid = dao.insert(mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation)
                result = self.build_MedDev_attr(mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation)
                return jsonify(MedDev=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def insertMedDevJson(self, json):
        mdid = json['mdid']
        mdtype = json['mdtype']
        mdsupplier = json['mdsupplier']
        mdbrand = json['mdbrand']
        mdquantity = json['mdquantity']
        mdlocation = json['mdlocation']
        if mdid and mdtype and mdsupplier and mdquantity and mdlocation:
            dao = MedDevDAO
            mdid = dao.insert(mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation)
            result = self.build_MedDev_attr(mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation)
            return jsonify(MedDev=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteMedDev(self, mdid):
        dao = MedDevDAO()
        if not dao.getMedDevByID(mdid):
            return jsonify(Error = "MedDev not found."), 404
        else:
            dao.delete(mdid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateMedDev(self, mdid, form):
        dao = MedDevDAO()
        if not dao.getMedDevByID(mdid):
            return jsonify(Error = "MedDev not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                mdid = form['mdid']
                mdtype = form['mdtype']
                mdbrand = form['mdbrand']
                mdsupplier = form['mdsupplier']
                mdquantity = form['mdquantity']
                mdlocation = form['mdlocation']
                if mdtype and mdbrand and mdsupplier and mdquantity and mdlocation:
                    dao.update(mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation)
                    result = self.build_MedDev_attr(mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation)
                    return jsonify(MedDev=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
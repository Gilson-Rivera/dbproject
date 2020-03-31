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

    def getMedById(self, cid):
        dao = MedSuppliesDAO()
        result = dao.getMedById(cid)
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
    #
    # def insertMed(self, form):
    #     print("form: ", form)
    #     if len(form) != 5:
    #         return jsonify(Error = "Malformed post request"), 400
    #     else:
    #         #remove fuid later
    #         fuid = form['fuid']
    #         ftype = form['ftype']
    #         fsupplier = form['fsupplier']
    #         fquantity = form['fquantity']
    #         flocation = form['flocation']
    #         if ftype and fsupplier and fquantity and flocation:
    #             dao = MedDAO
    #             fuid = dao.insert(fuid, ftype, fsupplier, fquantity, flocation)
    #             result = self.build_Med_attr(fuid, ftype, fsupplier, fquantity, flocation)
    #             return jsonify(Med=result), 201
    #         else:
    #             return jsonify(Error="Unexpected attributes in post request"), 400
    #

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

    # def deleteMed(self, fuid):
    #     dao = MedDAO()
    #     if not dao.getMedByID(fuid):
    #         return jsonify(Error = "Med not found."), 404
    #     else:
    #         dao.delete(fuid)
    #         return jsonify(DeleteStatus = "OK"), 200

    # def updateMed(self, fuid, form):
    #     dao = MedDAO()
    #     if not dao.getMedByID(fuid):
    #         return jsonify(Error = "Med not found."), 404
    #     else:
    #         if len(form) != 4:
    #             return jsonify(Error="Malformed update request"), 400
    #         else:
    #             fuid = form['fuid']
    #             ftype = form['ftype']
    #             fsupplier = form['fsupplier']
    #             fquantity = form['fquantity']
    #             flocation = form['flocation']
    #             if ftype and fsupplier and fquantity and flocation:
    #                 dao.update(fuid, ftype, fsupplier, fquantity, flocation)
    #                 result = self.build_Med_attr(fuid, ftype, fsupplier, fquantity, flocation)
    #                 return jsonify(Med=result), 200
    #             else:
    #                 return jsonify(Error="Unexpected attributes in update request"), 400
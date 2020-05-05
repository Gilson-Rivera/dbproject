from flask import jsonify
from dao.resources import ClothingDAO

class ClothingHandler:
    def build_clothing_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rbrand'] = row[2]
        result['rnumavailable'] = row[3]
        result['rprice'] = row[4]
        result['rsupplier'] = row[5]
        result['rlocation'] = row[6]
        result['clothes_id'] = row[7]
        result['cpiece'] = row[8]
        result['csex'] = row[9]
	result['csize'] = row[10]
        return result

    def build_clothing_consumed_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['clothes_id'] = row[1]
        result['cfirstname'] = row[2]
	result['clastname'] = row[3]
        result['cpiece'] = row[4]
        result['csex'] = row[5]
        result['csize'] = row[6]
        return result

    def build_Clothing_attr(self, clothes_id, mname, mexpdate, msupplier, mbrand, mquantit$
         result = {}
	return result

    def getAllClothing(self):
        dao = ClothingDAO()
        clothing_list = dao.getAllClothing()
        result_list = []
        for row in clothing_list:
            result = self.build_clothing_dict(row)
            result_list.append(result)
        return jsonify(Clothing=result_list)

    def getClothingByID(self, clothing_id):
        dao = ClothingDAO()
        row = dao.getClothingByID(clothing_id)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            clothing = self.build_clothing_dict(row)
	return jsonify(Clothing=clothing)

    def searchClothing(self, args):
	result_list = []
	return jsonify(Clothing=result_list)

    def insertClothing(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            
            cname = form['cname']
            cbrand = form['cbrand']
	    cnumavailable = form['cnumavailable']
	    cprice = form['cprice']
            csupplier = form['csupplier']
            cquantity = form['cquantity']
            clocation = form['clocation']
	    cpiece = form['cpiece']
	    csex = form['csex']
	    csize = form['csize']
            if cname and cbrand and cnumavailable and cprice and csupplier and cquantity and clocation and cpiece and csex and csize:
                dao = ClothingDAO()
                result = dao.insert(cname, cbrand, cnumavailable, cprice, csupplier, cquantity, clocation, cpiece, csex, csize)
                return jsonify(Clothing=result), 201
            else:
		return jsonify(Error="Unexpected attributes in post request"),$

    def insertClothingJson(self, json):
        cname = json['cname']
        cbrand = json['cbrand']
	cnumavailable = json['cnumavailable']
	cprice = json['cprice']
        csupplier = json['csupplier']
        cquantity = json['cquantity']
        clocation = json['clocation']
	cpiece = json['cpiece']
	csex = json['csex']
	csize = json['csize']
        if cname and cbrand and cnumavailable and cprice and csupplier and cquantity and clocation and cpiece and csex and csize:
            dao = ClothingDAO()
	    result = dao.insert(cname, cbrand, cnumavailable, cprice, csupplier, cquantity, clocation, cpiece, csex, csize)
            return jsonify(Clothing=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteClothing(self, clothing_id):
        dao = ClothingDAO()
        result = dao.delete(clothing_id)
        return jsonify(DeleteStatus = result), 200

    def updateMed(self, clothing_id, form):
        dao = ClothingDAO()
	if not dao.getClothingByID(clothing_id):
            return jsonify(Error="Medication not found."), 404
        else:
            return jsonify(dao.getClothingByID(mid)), 201


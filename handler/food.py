from flask import jsonify
from dao.food import FoodDAO

class FoodHandler:
    def build_Food_dict(self, row):
        result = {}
        result['fid'] = row[0]
        result['fname'] = row[1]
        result['fexpdate'] = row[2]
        result['fsupplier'] = row[3]
        result['fbrand'] = row[4]
        result['fquantity'] = row[5]
        result['flocation'] = row[6]

    def build_Food_attr(self, fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation):
        result = {}
        result['fid'] = fid
        result['fname'] = fname
        result['fexpdate'] = fexpdate
        result['fsupplier'] = fsupplier
        result['fbrand'] = fbrand
        result['fquantity'] = fquantity
        result['flocation'] = flocation
        return result

    def getAllFood(self):
        dao = FoodDAO()
        Food_list = dao.getAllFood()
        return jsonify(Food=Food_list)

    def getFoodByID(self, fid):
        dao = FoodDAO()
        result = dao.getFoodByID(fid)
        # if not row:
        #     return jsonify(Error = "Food Not Found"), 404
        # else:
        #     Food = self.build_Food_dict(row)
        return jsonify(Food = result)


    def searchFood(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = FoodDAO()
                Food_list = dao.getFoodByLocation(location)
                # result_list = []
                # for row in Food_list:
                #     result = self.build_Food_dict(row)
                #     result_list.append(row)
                return jsonify(Food=Food_list)
            else:
                return jsonify(Error="Malformed search string."), 400


    def insertFood(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            fname = form['fname']
            fbrand = form['fbrand']
            fexpdate = form['fexpdate']
            fsupplier = form['fsupplier']
            fquantity = form['fquantity']
            flocation = form['flocation']
            if fname and fsupplier and fquantity and flocation:
                dao = FoodDAO()
                fid = dao.insert(fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                result = self.build_Food_attr(fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                return jsonify(Food=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def insertFoodJson(self, json):
        fname = json['fname']
        fexpdate = json['fexpdate']
        fsupplier = json['fsupplier']
        fbrand = json['fbrand']
        fquantity = json['fquantity']
        flocation = json['flocation']
        if fname and fexpdate and fsupplier and fquantity and flocation:
            dao = FoodDAO()
            result = dao.insert(fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
            return jsonify(Food=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteFood(self, fid):
        dao = FoodDAO()
        # if not dao.getFoodByID(fid):
        #     return jsonify(Error = "Food not found."), 404
        # else:
        result =  dao.delete(fid)
        return jsonify(DeleteStatus = result), 200

    def updateFood(self, fid, form):
        dao = FoodDAO()
        if not dao.getFoodByID(fid):
            return jsonify(Error="Consumer not found."), 404
        else:
            return jsonify(dao.getFoodByID(fid)), 201
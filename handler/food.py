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
        row = dao.getFoodByID()
        if not row:
            return jsonify(Error = "Food Not Found"), 404
        else:
            Food = self.build_Food_dict(row)
            return jsonify(Food = Food)


    def searchFood(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            location = args.get("location")
            if location:
                dao = FoodDAO()
                Food_list = dao.getFoodByLocation()
                result_list = []
                for row in Food_list:
                    result = self.build_Food_dict(row)
                    result_list.append(row)
                return jsonify(Food=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400


    def insertFood(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            #remove fid later
            fid = form['fid']
            fname = form['fname']
            fbrand = form['fbrand']
            fexpdate = form['fexpdate']
            fsupplier = form['fsupplier']
            fquantity = form['fquantity']
            flocation = form['flocation']
            if fname and fsupplier and fquantity and flocation:
                dao = FoodDAO
                fid = dao.insert(fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                result = self.build_Food_attr(fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                return jsonify(Food=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def insertFoodJson(self, json):
        fid = json['fid']
        fname = json['fname']
        fexpdate = json['fexpdate']
        fsupplier = json['fsupplier']
        fbrand = json['fbrand']
        fquantity = json['fquantity']
        flocation = json['flocation']
        if fid and fname and fexpdate and fsupplier and fquantity and flocation:
            dao = FoodDAO
            fid = dao.insert(fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
            result = self.build_Food_attr(fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
            return jsonify(Food=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteFood(self, fid):
        dao = FoodDAO()
        if not dao.getFoodByID(fid):
            return jsonify(Error = "Food not found."), 404
        else:
            dao.delete(fid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateFood(self, fid, form):
        dao = FoodDAO()
        if not dao.getFoodByID(fid):
            return jsonify(Error = "Food not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                fid = form['fid']
                fname = form['fname']
                fexpdate = form['fexpdate']
                fbrand = form['fbrand']
                fsupplier = form['fsupplier']
                fquantity = form['fquantity']
                flocation = form['flocation']
                if fname and fexpdate and fbrand and fsupplier and fquantity and flocation:
                    dao.update(fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                    result = self.build_Food_attr(fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
                    return jsonify(Food=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
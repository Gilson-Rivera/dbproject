from flask import jsonify
from dao.food import FoodDAO

class FoodHandler:
    def build_food_dict(self, row):
        result = {}
        result['fid'] = row[0]
        result['fname'] = row[1]
        result['fexpdate'] = row[2]
        result['fnumavailable'] = row[3]
        result['fsupplier'] = row[4]
        result['fbrand'] = row[5]
        result['flocation'] = row[6]
        return result;

    def build_food_consumed_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['fid'] = row[1]
        result['cfirstname'] = row[2]
        result['clastname'] = row[3]
        result['fname'] = row[4]
        result['fbrand'] = row[5]
        result['foodconsume_price'] = row[6]
        result['foodconsume_quantity'] = row[7]
        result['foodconsume_date'] = row[8]
        return result

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
        food_list = dao.getAllFood()
        result_list = []
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food=result_list)

    def getFoodByID(self, fid):
        dao = FoodDAO()
        row = dao.getFoodByID(fid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            food = self.build_food_dict(row)
            return jsonify(Food=food)


    def searchFood(self, args):
        type = args.get("type")
        status = args.get("status")  # reserved or purchased
        location = args.get("location")
        dao = FoodDAO()
        food_list = []
        result_list = []
        if (len(args) == 1) and type:
            food_list = dao.getFoodByType(type)
            for row in food_list:
                result = self.build_food_dict(row)
                result_list.append(result)
        elif (len(args) == 1) and status:
            food_list = dao.getFoodByStatus(status)
            for row in food_list:
                result = self.build_food_consumed_dict(row)  # also need to add consumer's information
                result_list.append(result)
        elif (len(args) == 1) and location:
            food_list = dao.getFoodByLocation(location)
            for row in food_list:
                result = self.build_food_dict(row)
                result_list.append(result)
        else:
            return jsonify(Error="Malformed query string"), 400

        return jsonify(Food=result_list)


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
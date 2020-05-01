from flask import jsonify
from dao.food_supplies import FoodSuppliesDAO

class FoodSuppliesHandler:
    def build_food_supplies_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sorganization'] = row[1]
        result['fid'] = row[2]
        result['fname'] = row[3]
        result['foodsupply_price'] = row[4]
        result['foodsupply_quantity'] = row[5]
        result['foodsupply_date'] = row[6]
        return result

    def build_food_attr(self, fid, stype, foodsupply_price, foodsupply_date, foodsupply_quantity):
        result = {}
        result['fid'] = fid
        result['stype'] = stype
        result['foodsupply_price'] = foodsupply_price
        result['foodsupply_date'] = foodsupply_date
        result['foodsupply_quantity'] = foodsupply_quantity
        return result

    def getAllFoodSupplies(self):
        dao = FoodSuppliesDAO()
        food_list = dao.getAllFoodSupplies()
        result_list = []
        for row in food_list:
            result = self.build_food_supplies_dict(row)
            result_list.append(result)
        return jsonify(Food_Supplies=result_list)


    def searchFoodSupplies(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            date = args.get("date")
            price = args.get("price")
            if date:
                dao = FoodSuppliesDAO()
                result_list = dao.getFoodSupplyByDate(date)
                return jsonify(FoodSupplies=result_list)

            elif price:
                dao = FoodSuppliesDAO()
                result_list = dao.getFoodSupplyByPrice(price)
                return jsonify(FoodSupplies=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400


    def insertFoodSuppliesJson(self, json):
        foodsupply_price = json['foodsupply_price']
        foodsupply_date = json['foodsupply_date']
        foodsupply_quantity = json['foodsupply_quantity']
        if foodsupply_price and foodsupply_quantity and foodsupply_date:
            dao = FoodSuppliesDAO()
            result = dao.insert(foodsupply_price, foodsupply_quantity, foodsupply_date)
            return jsonify(Food_Supply=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
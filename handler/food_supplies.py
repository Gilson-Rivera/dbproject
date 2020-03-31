from flask import jsonify
from dao.food_supplies import FoodSuppliesDAO

class FoodSuppliesHandler:
    def build_food_supplies_dict(self, row):
        result = {}
        result['fid'] = row[0]
        result['sid'] = row[1]
        result['foodsupply_price'] = row[2]
        result['foodsupply_date'] = row[3]
        result['foodsupply_quantity'] = row[4]

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
        result_list = dao.getAllFoodSupplies()
        return jsonify(FoodSupplies=result_list)


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
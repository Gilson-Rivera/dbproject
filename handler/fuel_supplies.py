from flask import jsonify
from dao.fuel_supplies import FuelSuppliesDAO

class FuelSuppliesHandler:
    def build_fuel_supplies_dict(self, row):
        result = {}
        result['fuelid'] = row[0]
        result['sid'] = row[1]
        result['fuelsupply_price'] = row[2]
        result['fuelsupply_date'] = row[3]
        result['fuelsupply_quantity'] = row[4]

    def build_fuel_attr(self, fuid, stype, fuelsupply_price, fuelsupply_date, fuelsupply_quantity):
        result = {}
        result['fuelid'] = fuid
        result['stype'] = stype
        result['fuelsupply_price'] = fuelsupply_price
        result['fuelsupply_date'] = fuelsupply_date
        result['fuelsupply_quantity'] = fuelsupply_quantity
        return result

    def getAllFuelSupplies(self):
        dao = FuelSuppliesDAO()
        result_list = dao.getAllFuelSupplies()
        return jsonify(FuelSupplies=result_list)


    def searchFuelSupplies(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            date = args.get("date")
            price = args.get("price")
            if date:
                dao = FuelSuppliesDAO()
                result_list = dao.getFuelSupplyByDate(date)
                return jsonify(FuelSupplies=result_list)

            elif price:
                dao = FuelSuppliesDAO()
                result_list = dao.getFuelSupplyByPrice(price)
                return jsonify(FuelSupplies=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def insertFuelSuppliesJson(self, json):
        fuelsupply_price = json['fuelsupply_price']
        fuelsupply_date = json['fuelsupply_date']
        fuelsupply_quantity = json['fuelsupply_quantity']
        if fuelsupply_price and fuelsupply_quantity and fuelsupply_date:
            dao = FuelSuppliesDAO()
            result = dao.insert(fuelsupply_price, fuelsupply_quantity, fuelsupply_date)
            return jsonify(Fuel_Supply=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

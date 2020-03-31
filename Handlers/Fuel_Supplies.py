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

    # def getFuelByID(self, fuid):
    #     dao = FuelDAO()
    #     row = dao.getFuelByID(fuid)
    #     if not row:
    #         return jsonify(Error = "Fuel Not Found"), 404
    #     else:
    #         fuel = self.build_fuel_dict(row)
    #         return jsonify(Fuel = fuel)
    #
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
    #
    # def insertFuel(self, form):
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
    #             dao = FuelDAO
    #             fuid = dao.insert(fuid, ftype, fsupplier, fquantity, flocation)
    #             result = self.build_fuel_attr(fuid, ftype, fsupplier, fquantity, flocation)
    #             return jsonify(Fuel=result), 201
    #         else:
    #             return jsonify(Error="Unexpected attributes in post request"), 400
    #

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

    # def deleteFuel(self, fuid):
    #     dao = FuelDAO()
    #     if not dao.getFuelByID(fuid):
    #         return jsonify(Error = "Fuel not found."), 404
    #     else:
    #         dao.delete(fuid)
    #         return jsonify(DeleteStatus = "OK"), 200

    # def updateFuel(self, fuid, form):
    #     dao = FuelDAO()
    #     if not dao.getFuelByID(fuid):
    #         return jsonify(Error = "Fuel not found."), 404
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
    #                 result = self.build_fuel_attr(fuid, ftype, fsupplier, fquantity, flocation)
    #                 return jsonify(Fuel=result), 200
    #             else:
    #                 return jsonify(Error="Unexpected attributes in update request"), 400
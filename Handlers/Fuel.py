from flask import jsonify
from DAO.Fuel import FuelDAO

class FuelHandler:
    def build_fuel_dict(self, row):
        result = {}
        result['fuid'] = row[0]
        result['ftype'] = row[1]
        result['fsupplier'] = row[2]
        result['fquantity'] = row[3]
        result['flocation'] = row[4]

    def getAllFuel(self):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=fuel_list)


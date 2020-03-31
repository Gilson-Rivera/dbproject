from Config.dbconfig import pg_config
import psycopg2

#hardcoded DB entries, just for Phase 1, remove later!
rows, columns = (5, 7)
FoodDB = [[0 for x in range(rows)] for y in range(columns)]
FoodDB[0] = [1, 'Fruits', 'Apr 2020', 'Wal-Mart', 'Wal-Mart', 100, 'San Juan']
FoodDB[1] = [2, 'Vegetables', 'Apr 2020', 'Angel', 'Marketside', 10, 'Mayaguez']
FoodDB[2] = [3, 'Fruits', 'Apr 2020', 'Jonathan', 'Harvest Farms', 10, 'Mayaguez']
FoodDB[3] = [4, 'Rice', 'Oct 2021', 'Econo', 'Econo', 1000, 'Isabela']
FoodDB[4] = [5, 'Rice', 'Dec 2021', 'Gilson', 'Mago', 3, 'Mayaguez']

class FoodDAO:

    def getAllFood(self):
        result = []
        for row in FoodDB:
            result.append(row)
        return result

    def getFoodByID(self, fid):
        result = FoodDB[fid]
        return result

    def getFoodByType(self, fname):
        result = []
        for row in FoodDB:
            for col in row:
                if col[1] == fname:
                    result.append(row)
        return result

    def getFoodByExpDate(self, fexpdate):
        result = []
        for row in FoodDB:
            for col in row:
                if col[2] == fexpdate:
                    result.append(row)
        return result

    def getFoodBySupplier(self, fsupplier):
        result = []
        for row in FoodDB:
            for col in row:
                if col[3] == fsupplier:
                    result.append(row)
        return result

    def getFoodByBrand(self, fbrand):
        result = []
        for row in FoodDB:
            for col in row:
                if col[4] == fbrand:
                    result.append(row)
        return result

    def getFoodByQuantity(self, fquantity):
        result = []
        for row in FoodDB:
            for col in row:
                if col[5] == fquantity:
                    result.append(row)
        return result

    def getFoodByLocation(self, flocation):
        result = []
        for row in FoodDB:
            for col in row:
                if col[6] == flocation:
                    result.append(row)
        return result

    #fuid entry only for phase 1 for examples
    #Remove fuid for CRUD operations for later phases!
    #Must return the primary key as well
    def insert(self, fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation):
        FoodDB.append(fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
        return fid

    def delete(self, fid):
        FoodDB.pop(fid)
        return fid

    def update(self, fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation):
        FoodDB.append(fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation)
        return fid
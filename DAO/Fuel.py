
#hardcoded DB entries, just for Phase 1, remove later!
rows, columns = (5, 5)
FuelDB = [[0 for x in range(rows)] for y in range(columns)]
FuelDB[0] = [1, 'Gasoline', 'Wal-Mart', 30, 'San Juan']
FuelDB[1] = [2, 'Diesel', 'Amazon', 20, 'San Juan']
FuelDB[2] = [3, 'Gasoline', 'Jonathan', 3, 'Mayaguez']
FuelDB[3] = [4, 'Propane', 'Angel', 4, 'Mayaguez']
FuelDB[4] = [5, 'Diesel', 'Gilson', 30, 'Mayaguez']

class FuelDAO:

    def getAllFuel(self):
        result = []
        for row in FuelDB:
            result.append(row)
        return result

    def getFuelByID(self, fuid):
        result = FuelDB[fuid]
        return result

    def getFuelByType(self, ftype):
        result = []
        for row in FuelDB:
            for col in row:
                if col[2] == ftype:
                    result.append(row)
        return result

    def getFuelBySupplier(self, fsupplier):
        result = []
        for row in FuelDB:
            for col in row:
                if col[2] == fsupplier:
                    result.append(row)
        return result

    def getFuelByQuantity(self, fquantity):
        result = []
        for row in FuelDB:
            for col in row:
                if col[2] == fquantity:
                    result.append(row)
        return result

    def getFuelByLocation(self, flocation):
        result = []
        for row in FuelDB:
            for col in row:
                if col[2] == flocation:
                    result.append(row)
        return result

    #fuid entry only for phase 1 for examples
    #Remove fuid for CRUD operations for later phases!
    #Must return the primary key as well
    def insert(self, fuid, ftype, fsupplier, fquantity, flocation):
        FuelDB.append(fuid, ftype, fsupplier, fquantity, flocation)
        return fuid

    def delete(self, fuid):
        FuelDB.pop(fuid)
        return fuid

    def update(self, fuid, ftype, fsupplier, fquantity, flocation):
        FuelDB[fuid] = [fuid, ftype, fsupplier, fquantity, flocation]
        return fuid






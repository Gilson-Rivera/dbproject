
class FuelDAO:

    def getAllFuel(self):
        result = "This is a list of Fuel."
        return result

    def getFuelByID(self):
        result = "This is a specific Fuel."
        return result

    def getFuelByType(self, fname):
        result = "This is a list of Fuel by type."
        return result

    def getFuelBySupplier(self, fsupplier):
        result = "This is a list of Fuel by supplier."
        return result

    def getFuelByQuantity(self, fquantity):
        result = "This is a list of Fuel by quantity."
        return result

    def getFuelByLocation(self, flocation):
        result = "This is a list of Fuel by location."
        return result

    #fuid entry only for phase 1 for examples
    #Remove fuid for CRUD operations for later phases!
    #Must return the primary key as well
    def insert(self, ftype, fsupplier, fquantity, flocation):
        result = "Fuel inserted"
        return result

    def delete(self, fuid):
        fuid = "Fuel deleted"
        return fuid

    def update(self, fuid, ftype, fsupplier, fquantity, flocation):
        FuelDB[fuid] = [fuid, ftype, fsupplier, fquantity, flocation]
        return fuid

class MedDevDAO:

    def getAllMedDev(self):

        result = "This is a list of medical devices"
        return result

    def getMedDevByID(self, mdid):
        result = "This is medical device with given ID."
        return result

    def getMedDevByType(self, fname):
        result = "This is a list of medical devices by type."
        return result

    def getMedDevBySupplier(self, fsupplier):
        result = "This is a list of medical devices by supplier."
        return result

    def getMedDevByBrand(self, fbrand):
        result = "This is a list of medical devices by a specific brand."
        return result

    def getMedDevByQuantity(self, fquantity):
        result = "This is a list of medical devices by quantity."
        return result

    def getMedDevByLocation(self, mdlocation):
        result = "This is a medical device in specified location"
        return result

    #fuid entry only for phase 1 for examples
    #Remove fuid for CRUD operations for later phases!
    #Must return the primary key as well
    def insert(self, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation):
        result = "Medical device inserted"
        return result

    def delete(self, mdid):
        result = "Medical device deleted"
        return result

    def update(self, mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation):
        result = "Medical device updated"
        return result
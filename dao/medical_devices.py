
class MedDevDAO:

    def getAllMedDev(self):
        result = "This is a list of medical devices."
        return result

    def getMedDevByID(self):
        result = "This is a specific medical devices."
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

    def getMedDevByLocation(self, flocation):
        result = "This is a list of medical devices by location."
        return result

    #fuid entry only for phase 1 for examples
    #Remove fuid for CRUD operations for later phases!
    #Must return the primary key as well
    def insert(self, mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation):
        MedDevDB.append(mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation)
        return mdid

    def delete(self, mdid):
        MedDevDB.pop(mdid)
        return mdid

    def update(self, mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation):
        MedDevDB.append(mdid, mdtype, mdsupplier, mdbrand, mdquantity, mdlocation)
        return mdid
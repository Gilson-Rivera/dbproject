
class MedDAO:

    def getAllMed(self):
        result = "This is a list of medications."
        return result

    def getMedByID(self):
        result = "This is a specific medications."
        return result

    def getMedByType(self, fname):
        result = "This is a list of medications by type."
        return result

    def getMedByExpDate(self, fexpdate):
        result = "This is a list of medications by Expiration Dates."
        return result

    def getMedBySupplier(self, fsupplier):
        result = "This is a list of medications by supplier."
        return result

    def getMedByBrand(self, fbrand):
        result = "This is a list of medications by a specific brand."
        return result

    def getMedByQuantity(self, fquantity):
        result = "This is a list of medications by quantity."
        return result

    def getMedByLocation(self, flocation):
        result = "This is a list of medications by location."
        return result
    
    #fuid entry only for phase 1 for examples
    #Remove fuid for CRUD operations for later phases!
    #Must return the primary key as well
    def insert(self, fid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation):
        MedDB.append(fid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
        return fid

    def delete(self, fid):
        MedDB.pop(fid)
        return fid

    def update(self, fid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation):
        MedDB.append(fid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
        return fid
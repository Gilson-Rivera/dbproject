
class MedDAO:

    def getAllMed(self):
        result = "This is a list of medications."
        return result

    def getMedByID(self, mid):
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

    def getMedByLocation(self, mlocation):
        result = "Medication from specified location"
        return result

    def insert(self, mname, mexpdate, msupplier, mbrand, mquantity, mlocation):
        result = "Medication inserted"
        return result

    def delete(self, fid):
        result = "Medication deleted"
        return result

    def update(self, fid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation):
        result = "Medication updated"
        return result
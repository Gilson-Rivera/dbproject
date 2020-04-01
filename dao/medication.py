#hardcoded DB entries, just for Phase 1, remove later!
rows, columns = (7, 5)
MedDB = [[0 for x in range(rows)] for y in range(columns)]
MedDB[0] = [1, 'Lipitor', 'Apr 2022', 'Walgreens', 'Walgreens', 150, 'San Juan']
MedDB[1] = [2, 'Panadol', 'Apr 2022', 'Angel', 'Walgreens', 10, 'Mayaguez']
MedDB[2] = [3, 'Acetaminophen', 'Apr 2023', 'Jonathan', 'Merck', 10, 'Mayaguez']
MedDB[3] = [4, 'Norvasc', 'Oct 2025', 'Johnson & Johnson', 'Johnson & Johnson', 50, 'Isabela']
MedDB[4] = [5, 'Prilosec', 'Dec 2023', 'Gilson', 'Bayer', 5, 'Mayaguez']

class MedDAO:

    def getAllMed(self):
        result = []
        for row in MedDB:
            result.append(row)
        return result

    def getMedByID(self, mid):
        result = "Medication with specified ID"
        return result

    def getMedByType(self, mname):
        result = []
        for row in MedDB:
            for col in row:
                if col[1] == mname:
                    result.append(row)
        return result

    def getMedByExpDate(self, mexpdate):
        result = []
        for row in MedDB:
            for col in row:
                if col[2] == mexpdate:
                    result.append(row)
        return result

    def getMedBySupplier(self, msupplier):
        result = []
        for row in MedDB:
            for col in row:
                if col[3] == msupplier:
                    result.append(row)
        return result

    def getMedByBrand(self, mbrand):
        result = []
        for row in MedDB:
            for col in row:
                if col[4] == mbrand:
                    result.append(row)
        return result

    def getMedByQuantity(self, mquantity):
        result = []
        for row in MedDB:
            for col in row:
                if col[5] == mquantity:
                    result.append(row)
        return result

    def getMedByLocation(self, mlocation):
        result = "Medication from specified location"
        return result

    #fuid entry only for phase 1 for examples
    #Remove fuid for CRUD operations for later phases!
    #Must return the primary key as well
    def insert(self, mname, mexpdate, msupplier, mbrand, mquantity, mlocation):
        result = "Medication inserted"
        return result

    def delete(self, fid):
        result = "Medication deleted"
        return result

    def update(self, fid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation):
        MedDB.append(fid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation)
        return fid
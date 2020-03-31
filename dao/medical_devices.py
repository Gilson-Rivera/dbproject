#hardcoded DB entries, just for Phase 1, remove later!
rows, columns = (6, 5)
MedDevDB = [[0 for x in range(rows)] for y in range(columns)]
MedDevDB[0] = [1, 'Syringes', 'Walgreens', 'GE Healthcare', 100, 'San Juan']
MedDevDB[1] = [2, 'Bandages', 'Angel', 'Philips', 10, 'Mayaguez']
MedDevDB[2] = [3, 'Bandages', 'Jonathan', 'Philips', 10, 'Mayaguez']
MedDevDB[3] = [4, 'Thermometer', 'Johnson & Johnson', 'Johnson & Johnson', 1000, 'Isabela']
MedDevDB[4] = [5, 'Humidifier', 'Gilson', 'Medtronic', 3, 'Mayaguez']

class MedDevDAO:

    def getAllMedDev(self):
        result = []
        for row in MedDevDB:
            result.append(row)
        return result

    def getMedDevByID(self, mdid):
        result = MedDevDB[mdid]
        return result

    def getMedDevByType(self, mdtype):
        result = []
        for row in MedDevDB:
            for col in row:
                if col[1] == mdtype:
                    result.append(row)
        return result

    def getMedDevBySupplier(self, mdsupplier):
        result = []
        for row in MedDevDB:
            for col in row:
                if col[2] == mdsupplier:
                    result.append(row)
        return result

    def getMedDevByBrand(self, mdbrand):
        result = []
        for row in MedDevDB:
            for col in row:
                if col[3] == mdbrand:
                    result.append(row)
        return result

    def getMedDevByQuantity(self, mdquantity):
        result = []
        for row in MedDevDB:
            for col in row:
                if col[4] == mdquantity:
                    result.append(row)
        return result

    def getMedDevByLocation(self, mdlocation):
        result = []
        for row in MedDevDB:
            for col in row:
                if col[5] == mdlocation:
                    result.append(row)
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
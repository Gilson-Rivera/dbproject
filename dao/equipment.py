class EquipDAO:

    def getAllEquip(self):
        result = "This is a list of equipment."
        return result

    def getEquipByID(self):
        result = "This is a specific piece of equipment."
        return result

    def getEquipByType(self):
        result = "This is a list of equipment by type."
        return result

    def getEquipBySupplier(self):
        result = "This is a list of equipment by its supplier."
        return result

    def getEquipByBrand(self):
        result = "This is a list of equipment by its brand."
        return result

    def getEquipByQuantity(self):
        result = "This is a list of equipment by its quantity."
        return result

    def getEquipByLocation(self):
        result = "This is a list of equipment by its location."
        return result

    #fuid entry only for phase 1 for examples
    #Remove fuid for CRUD operations for later phases!
    #Must return the primary key as well
    def insert(self, eid, etype, esupplier, ebrand, equantity, elocation):
        EquipDB.append(eid, etype, esupplier, ebrand, equantity, elocation)
        return eid

    def delete(self, eid):
        EquipDB.pop(eid)
        return eid

    def update(self, eid, etype, esupplier, ebrand, equantity, elocation):
        EquipDB.append(eid, etype, esupplier, ebrand, equantity, elocation)
        return eid
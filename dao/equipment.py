class EquipDAO:

    def getAllEquip(self):
        result = "This is a list of equipment"
        return result

    def getEquipByID(self, eid):
        result = "Equipment with specified id"

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

    def getEquipByLocation(self, elocation):
        result = "Equipment with given location"
        return result

    #fuid entry only for phase 1 for examples
    #Remove fuid for CRUD operations for later phases!
    #Must return the primary key as well
    def insert(self, eid, etype, esupplier, ebrand, equantity, elocation):
        result = "Equipment inserted"
        return result

    def delete(self, eid):
        result = "Equipment deleted"
        return result

    def update(self, eid, etype, esupplier, ebrand, equantity, elocation):
        result = "Equipment updated"
        return result
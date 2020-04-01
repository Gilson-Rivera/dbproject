
class FoodDAO:

    def getAllFood(self):
        result = "This is a list of food"
        return result

    def getFoodByID(self, fid):
        result = "Food with specified ID"
        return result

    def getFoodByType(self, fname):
        result = "This is a list of food by type."
        return result

    def getFoodByExpDate(self, fexpdate):
        result = "This is a list of food by Expiration Dates."
        return result

    def getFoodBySupplier(self, fsupplier):
        result = "This is a list of food by supplier."
        return result

    def getFoodByBrand(self, fbrand):
        result = "This is a list of food by a specific brand."
        return result

    def getFoodByQuantity(self, fquantity):
        result = "This is a list of food by quantity."
        return result

    def getFoodByLocation(self, flocation):
        result = "This is food in a specified location"
        return result

    #fuid entry only for phase 1 for examples
    #Remove fuid for CRUD operations for later phases!
    #Must return the primary key as well
    def insert(self, fname, fexpdate, fsupplier, fbrand, fquantity, flocation):
        result = "Food inserted"
        return result

    def delete(self, fid):
        result = "Food deleted"
        return result

    def update(self, fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation):
        result = "Food deleted"
        return result
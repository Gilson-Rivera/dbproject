from config.dbconfig import pg_config
import psycopg2

class MedSuppliesDAO:

    def getAllMedSupplies(self):
        result = "This is a list of Med supplies"
        return result

    def getMedDevById(self, mid):
        result = "This is a medical device with specified ID"
        return result

    def getMedSupplyByDate(self, date):
        result = "This are Med supplies with given date"
        return result

    def getMedSupplyByPrice(self, price):
        result = "This are Med supplies with given price"
        return result

    def getMedSupplyByQuantity(self, quantity):
        result = "This are Med supplies with given quantity"
        return result

    def insert(self, Medsupply_price, Medsupply_quantity, Medsupply_date):
        result = "Med supply inserted"
        return result
    #
    def delete(self, mid):
        result = "Med supply deleted"
        return result

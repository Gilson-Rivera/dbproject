from config.dbconfig import pg_config
import psycopg2
class MDSuppliesDAO:

    def getAllMDSupplies(self):
        result = "This is a list of medical devices supplies"
        return result

    def getMDSupplyByDate(self, date):
        result = "This are medical devices supplies with given date"
        return result

    def getMDSupplyByPrice(self, price):
        result = "This are medical devices supplies with given price"
        return result

    def insert(self, fuelsupply_price, fuelsupply_quantity, fuelsupply_date):
        result = "Medical device supply inserted"
        return result
    
    def delete(self, cid):
        result = "Medical devices supplied deleted"
        return result

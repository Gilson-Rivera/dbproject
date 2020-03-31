from config.dbconfig import pg_config
import psycopg2
class MDSuppliesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

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

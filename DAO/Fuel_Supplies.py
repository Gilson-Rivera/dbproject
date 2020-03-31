from Config.dbconfig import pg_config
import psycopg2

class FuelSuppliesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFuelSupplies(self):
        result = "This is a list of fuel supplies"
        return result

    # def searchConsumerBeta(self):
    #     result = "This is a searched consumer"
    #     return result
    #
    # def getConsumerById(self, cid):
    #     result = "This is a specific consumer"
    #     return result
    #
    def getFuelSupplyByDate(self, date):
        result = "This are fuel supplies with given date"
        return result

    def getFuelSupplyByPrice(self, price):
        result = "This are fuel supplies with given price"
        return result

    def insert(self, fuelsupply_price, fuelsupply_quantity, fuelsupply_date):
        result = "fuel supply inserted"
        return result
    #
    def delete(self, cid):
        result = "Fuel supply deleted"
        return result

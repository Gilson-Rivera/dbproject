from config.dbconfig import pg_config
import psycopg2
class EquipmentSuppliesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllESupplies(self):
        result = "This is a list of equipment supplies"
        return result

    def getESupplyByDate(self, date):
        result = "This are equipment supplies with given date"
        return result

    def getESupplyByPrice(self, price):
        result = "This are equipment supplies with given price"
        return result

    def insert(self, fuelsupply_price, fuelsupply_quantity, fuelsupply_date):
        result = "Equipment supply inserted"
        return result
    
    def delete(self, cid):
        result = "Equipment supplied deleted"
        return result

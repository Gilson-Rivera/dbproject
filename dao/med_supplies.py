from config.dbconfig import pg_config
import psycopg2

class MedSuppliesDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllMedSupplies(self):
        cursor = self.conn.cursor()
        query = "select sid, sorganization, mid, mname, msupply_price, msupply_quantity, msupply_date from suppliers natural inner join medications natural inner join msupplies;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
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

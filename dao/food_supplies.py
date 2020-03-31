from config.dbconfig import pg_config
import psycopg2
class FoodSuppliesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFoodSupplies(self):
        result = "This is a list of food supplies"
        return result


    def getFoodSupplyByDate(self, date):
        result = "This are food supplies with given date"
        return result

    def getFoodSupplyByPrice(self, price):
        result = "This are food supplies with given price"
        return result


    def insert(self, foodsupply_price, foodsupply_quantity, foodsupply_date):
        result = "Food supply inserted"
        return result

    def delete(self, cid):
        result = "Food supply deleted"
        return result




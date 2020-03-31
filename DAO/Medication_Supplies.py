from Config.dbconfig import pg_config
import psycopg2
class MedSuppliesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMedicationSupplies(self):
        result = "This is a list of Medication supplies"
        return result

    # def searchConsumerBeta(self):
    #     result = "This is a searched consumer"
    #     return result
    #
    # def getConsumerById(self, cid):
    #     result = "This is a specific consumer"
    #     return result
    #
    def getMedicationSupplyByDate(self, date):
        result = "This are Medication supplies with given date"
        return result

    def getMedicationSupplyByPrice(self, price):
        result = "This are Medication supplies with given price"
        return result

    def getMedicationSupplyByQuantity(self, price):
        result = "This are Medication supplies with given quantity"
        return result

    def insert(self, Medicationsupply_price, Medicationsupply_quantity, Medicationsupply_date):
        result = "Medication supply inserted"
        return result
    #
    def delete(self, cid):
        result = "Medication supply deleted"
        return result

from Config.dbconfig import pg_config
import psycopg2

class SupplierDAO:

    def getAllSuppliers(self):
        result = "This is a list of suppliers"
        return result

    def getSupplierById(self, sid):
            result = "This is the supplier with given id"
            return result

    def getSuppliersByOrganization(self, city):
        result = "List of supplier names from a specific organization"
        return result

    def insert(self, sfirstname, slastname, sorganization, sphone, slocation):
        result = "Supplier inserted"
        return result


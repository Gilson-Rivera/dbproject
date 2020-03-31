from config.dbconfig import pg_config
import psycopg2

class SupplierDAO:

    def getAllSuppliers(self):
        result = "This is a list of suppliers"
        return result

    def getSupplierById(self, sid):
            result = "This is the supplier with given id"
            return result

    # def getPartsBySupplierId(self, sid):
    #     cursor = self.conn.cursor()
    #     query = "select pid, pname, pmaterial, pcolor, pprice, qty from parts natural inner join supplier natural inner join supplies where sid = %s;"
    #     cursor.execute(query, (sid,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

    def getSuppliersByOrganization(self, city):
        result = "List of supplier names from a specific organization"
        return result

    def insert(self, sfirstname, slastname, sorganization, sphone, slocation):
        result = "Supplier inserted"
        return result

from config.dbconfig import pg_config
import psycopg2

class SupplierDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        result = "This is a list of suppliers"
        return result

    def getSupplierById(self, sid):
            result = "This is the supplier with given id"
            return result

    def getPartsBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice, qty from parts natural inner join supplier natural inner join supplies where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByOrganization(self, city):
        result = "List of supplier names from a specific organization"
        return result

    def insert(self, sname, scity, sphone):
        result = "Supplier inserted"
        return result
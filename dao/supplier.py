from config.dbconfig import pg_config
import psycopg2

class SupplierDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from suppliers;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, sid):
        cursor = self.conn.cursor()
        query = "select * from suppliers where sid=%s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result

    def getSuppliersByOrganization(self, city):
        result = "List of supplier names from a specific organization"
        return result

    def getSuppliersByLocation(self, location):
        cursor = self.conn.cursor()
        query = "select * from suppliers where slocation=%s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, sfirstname, slastname, sorganization, slocation, sphone):
        cursor = self.conn.cursor()
        query = "insert into suppliers(sfirstname, slastname, sorganization, slocation, sphone) values (%s, %s, %s, %s, %s) returning sid;"
        cursor.execute(query, (sfirstname, slastname, sorganization, slocation, sphone,))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid

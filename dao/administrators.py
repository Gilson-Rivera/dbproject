from config.dbconfig import pg_config
import psycopg2
class AdministratorsDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAdministrators(self):
        cursor = self.conn.cursor()
        query = "select * from administrators"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchAdministratorBeta(self):
        result = "This is a searched administrator"
        return result

    def getAdministratorById(self, aid):
        cursor = self.conn.cursor()
        query = "select * from administrators where aid=%s;"
        cursor.execute(query, (aid,))
        result = cursor.fetchone()
        return result

    def getAdministratorByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from administrators where afirstname=%s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, afirstname, alastname, alocation, a_age, aphone):
        cursor = self.conn.cursor()
        query = "insert into administrators(afirstname, alastname, alocation, a_age, aphone) values (%s, %s, %s, %s, %s) returning aid;"
        cursor.execute(query, (afirstname, alastname, alocation, a_age, aphone,))
        aid = cursor.fetchone()[0]
        self.conn.commit()
        return aid

    def delete(self, aid):
        result = "Administrator deleted"
        return result

    def update(self, aid, afirstname, alastname, alocation, a_age, aphone):
        cursor = self.conn.cursor()
        query = "update Administrator set afirstname = %s, alastname = %s, alocation = %s, a_age, aphone = %s where aid = %s;"
        cursor.execute(query, (aid, afirstname, alastname, alocation, a_age, aphone,))
        self.conn.commit()
        return aid




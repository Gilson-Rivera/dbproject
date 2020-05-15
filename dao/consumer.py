from config.dbconfig import pg_config
import psycopg2
class ConsumersDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllConsumers(self):
        cursor = self.conn.cursor()
        query = "select cid, cfirstname, clastname, clocation, cage, cphone.phone from consumers natural inner join cphone;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchConsumerBeta(self):
        result = "This is a searched consumer"
        return result

    def getConsumerById(self, cid):
        cursor = self.conn.cursor()
        query = "select cid, cfirstname, clastname, clocation, cage, cphone.phone from consumers natural inner join cphone where cid = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result


    def getConsumerByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from consumers natural inner join cphone where cfirstname=%s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, cfirstname, clastname, clocation, cage):
        cursor = self.conn.cursor()
        query = "insert into consumers(cfirstname, clastname, clocation, cage) values (%s, %s, %s, %s) returning cid;"
        cursor.execute(query, (cfirstname, clastname, clocation, cage,))
        cid = cursor.fetchone()[0]
        self.conn.commit()
        return cid

    def insertPhone(self, cid, cphone):
        cursor = self.conn.cursor()
        query = "insert into cphone(cid, phone) values (%s, %s) returning cphone_id;"
        cursor.execute(query, (cid, cphone,))
        cphone_id = cursor.fetchone()[0]
        self.conn.commit()
        return cphone_id

    def delete(self, cid):
        result = "Consumer deleted"
        return result

    def update(self, cid, cfirstname, clastname, clocation, cage, cphone):
        cursor = self.conn.cursor()
        query = "update consumer set cfirstname = %s, clastname = %s, clocation = %s, cage, cphone = %s where cid = %s;"
        cursor.execute(query, (cid, cfirstname, clastname, clocation, cage, cphone,))
        self.conn.commit()
        return cid




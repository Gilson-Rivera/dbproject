from config.dbconfig import pg_config
import psycopg2
class ConsumersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllConsumers(self):
        result = "This is a list of consumers"
        return result

    def searchConsumerBeta(self):
        result = "This is a searched consumer"
        return result

    def getConsumerById(self, cid):
        result = "This is a specific consumer"
        return result

    def getConsumerByName(self, name):
        result = "This is consumer with given name"
        return result

    def insert(self, cfirstname, clastname, clocation, cage):
        result = "consumer inserted"
        return result

    def delete(self, cid):
        result = "Consumer deleted"
        return result
    #
    # def update(self, pid, pname, pcolor, pmaterial, pprice):
    #     cursor = self.conn.cursor()
    #     query = "update part set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
    #     cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
    #     self.conn.commit()
    #     return pid
    #
    # def getCountByPartId(self):
    #     cursor = self.conn.cursor()
    #     query = "select pid, pname, sum(stock) from part natural inner join supplies group by pid, pname order by pname;"
    #     cursor.execute(query)
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

from config.dbconfig import pg_config
import psycopg2
class AdministratorsDAO:

    def getAllAdministrators(self):
        result = "This is a list of administrators"
        return result

    def searchAdministratorBeta(self):
        result = "This is a searched administrator"
        return result

    def getAdministratorById(self, aid):
        result = "This is a specific administrator"
        return result

    def getAdministratorByName(self, name):
        result = "This is administrator with given name"
        return result

    def insert(self, afirstname, alastname, alocation, a_age):
        result = "Administrator inserted"
        return result

    def delete(self, aid):
        result = "Administrator deleted"
        return result

    def update(self, aid, afirstname, alastname, alocation, a_age, aphone):
        cursor = self.conn.cursor()
        query = "update Administrator set afirstname = %s, alastname = %s, alocation = %s, a_age, aphone = %s where aid = %s;"
        cursor.execute(query, (aid, afirstname, alastname, alocation, a_age, aphone,))
        self.conn.commit()
        return aid




from config.dbconfig import pg_config
import psycopg2
class FuelSuppliesDAO:

    def getAllFuelSupplies(self):
        result = "This is a list of fuel supplies"
        return result

    # def searchConsumerBeta(self):
    #     result = "This is a searched consumer"
    #     return result
    #
    # def getConsumerById(self, cid):
    #     result = "This is a specific consumer"
    #     return result
    #
    def getFuelSupplyByDate(self, date):
        result = "This are fuel supplies with given date"
        return result

    def getFuelSupplyByPrice(self, price):
        result = "This are fuel supplies with given price"
        return result

    # # def getPartsByMaterial(self, material):
    # #     cursor = self.conn.cursor()
    # #     query = "select * from part where pmaterial = %s;"
    # #     cursor.execute(query, (material,))
    # #     result = []
    # #     for row in cursor:
    # #         result.append(row)
    # #     return result
    # #
    # # def getPartsByColorAndMaterial(self, color, material):
    # #     cursor = self.conn.cursor()
    # #     query = "select * from part where pmaterial = %s and pcolor = %s;"
    # #     cursor.execute(query, (material,color))
    # #     result = []
    # #     for row in cursor:
    # #         result.append(row)
    # #     return result
    # #
    # # def getSuppliersByPartId(self, pid):
    # #     cursor = self.conn.cursor()
    # #     query = "select sid, sname, scity, sphone from part natural inner join supplier natural inner join supplies where pid = %s;"
    # #     cursor.execute(query, (pid,))
    # #     result = []
    # #     for row in cursor:
    # #         result.append(row)
    # #     return result
    # #
    def insert(self, fuelsupply_price, fuelsupply_quantity, fuelsupply_date):
        result = "fuel supply inserted"
        return result
    #
    def delete(self, cid):
        result = "Fuel supply deleted"
        return result
    # #
    # # def update(self, pid, pname, pcolor, pmaterial, pprice):
    # #     cursor = self.conn.cursor()
    # #     query = "update part set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
    # #     cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
    # #     self.conn.commit()
    # #     return pid
    # #
    # # def getCountByPartId(self):
    # #     cursor = self.conn.cursor()
    # #     query = "select pid, pname, sum(stock) from part natural inner join supplies group by pid, pname order by pname;"
    # #     cursor.execute(query)
    # #     result = []
    # #     for row in cursor:
    # #         result.append(row)
    # #     return result



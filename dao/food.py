from config.dbconfig import pg_config
import psycopg2

class FoodDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFood(self):
        cursor = self.conn.cursor()
        query = "select fid, fname, fexpdate, fnumavailable, fbrand, sorganization, flocation from food natural inner join fsupplier natural inner join suppliers natural inner join flocation;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodByID(self, fid):
        cursor = self.conn.cursor()
        query = "select fid, fname, fexpdate, fnumavailable, fbrand, sorganization, flocation from food natural inner join fsupplier natural inner join suppliers natural inner join flocation where fid = %s;"
        cursor.execute(query, (fid,))
        result = cursor.fetchone()
        return result

    def getFoodByType(self, type):
        cursor = self.conn.cursor()
        query = "select fid, fname, fexpdate, fnumavailable, fbrand, sorganization, flocation from food natural inner join fsupplier natural inner join suppliers natural inner join flocation where fname = %s;"
        cursor.execute(query, (type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodByStatus(self, status):
        cursor = self.conn.cursor()
        if(status == 'reserved'):
            query = "select cid, fid, cfirstname, clastname, fname, fbrand, foodconsume_price, foodconsume_quantity, foodconsume_date from consumers natural inner join food natural inner join food_consume where foodconsume_price = 0;"
        elif (status == 'purchased'):
            query = "select cid, fid, cfirstname, clastname, fname, fbrand, foodconsume_price, foodconsume_quantity, foodconsume_date from consumers natural inner join food natural inner join food_consume where foodconsume_price > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodByLocation(self, location):
        cursor = self.conn.cursor()
        query = "select fid, fname, fexpdate, fnumavailable, fbrand, sorganization, flocation from food natural inner join fsupplier natural inner join suppliers natural inner join flocation where flocation = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodByExpDate(self, fexpdate):
        result = "This is a list of food by Expiration Dates."
        return result

    def getFoodBySupplier(self, fsupplier):
        result = "This is a list of food by supplier."
        return result

    def getFoodByBrand(self, fbrand):
        result = "This is a list of food by a specific brand."
        return result

    def getFoodByQuantity(self, fquantity):
        result = "This is a list of food by quantity."
        return result


    #fuid entry only for phase 1 for examples
    #Remove fuid for CRUD operations for later phases!
    #Must return the primary key as well
    def insert(self, fname, fexpdate, fsupplier, fbrand, fquantity, flocation):
        result = "Food inserted"
        return result

    def delete(self, fid):
        result = "Food deleted"
        return result

    def update(self, fid, fname, fexpdate, fsupplier, fbrand, fquantity, flocation):
        result = "Food deleted"
        return result
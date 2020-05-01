from config.dbconfig import pg_config
import psycopg2

class MedDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMedications(self):
        cursor = self.conn.cursor()
        query = "select mid, mname, mexpdate, mnumavailable, mbrand, sorganization, mlocation, mispill, misliquid from medications natural inner join msupplier natural inner join suppliers natural inner join mlocation order by mname;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicationByType(self, type):
        cursor = self.conn.cursor()
        query = "select mid, mname, mexpdate, mnumavailable, mbrand, sorganization, mlocation, mispill, misliquid from medications natural inner join msupplier natural inner join suppliers natural inner join mlocation where mname = %s;"
        cursor.execute(query, (type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicationByStatus(self, status):
        cursor = self.conn.cursor()
        if(status == 'reserved'):
            query = "select cid, mid, cfirstname, clastname, mname, mbrand, mconsume_price, mconsume_quantity, mconsume_date from consumers natural inner join medications natural inner join mconsumes where mconsume_price = 0;"
        elif (status == 'purchased'):
            query = "select cid, mid, cfirstname, clastname, mname, mbrand, mconsume_price, mconsume_quantity, mconsume_date from consumers natural inner join medications natural inner join mconsumes where mconsume_price > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicationByLocation(self, location):
        cursor = self.conn.cursor()
        query = "select mid, mname, mexpdate, mnumavailable, mbrand, sorganization, mlocation, mispill, misliquid from medications natural inner join msupplier natural inner join suppliers natural inner join mlocation where mlocation = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicationByID(self, mid):
        cursor = self.conn.cursor()
        query = "select mid, mname, mexpdate, mnumavailable, mbrand, sorganization, mlocation, mispill, misliquid from medications natural inner join msupplier natural inner join suppliers natural inner join mlocation where mid = %s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    # def getMedicationByType(self, mname):
    #     result = []
    #     for row in MedDB:
    #         for col in row:
    #             if col[1] == mname:
    #                 result.append(row)
    #     return result

    # def getMedicationByExpDate(self, mexpdate):
    #     result = []
    #     for row in MedDB:
    #         for col in row:
    #             if col[2] == mexpdate:
    #                 result.append(row)
    #     return result
    #
    # def getMedicationBySupplier(self, msupplier):
    #     result = []
    #     for row in MedDB:
    #         for col in row:
    #             if col[3] == msupplier:
    #                 result.append(row)
    #     return result
    #
    # def getMedByBrand(self, mbrand):
    #     result = []
    #     for row in MedDB:
    #         for col in row:
    #             if col[4] == mbrand:
    #                 result.append(row)
    #     return result
    #
    # def getMedByQuantity(self, mquantity):
    #     result = []
    #     for row in MedDB:
    #         for col in row:
    #             if col[5] == mquantity:
    #                 result.append(row)
    #     return result
    #
    # def getMedByLocation(self, mlocation):
    #     result = "Medication from specified location"
    #     return result
    #
    # def insert(self, mname, mexpdate, msupplier, mbrand, mquantity, mlocation):
    #     result = "Medication inserted"
    #     return result
    #
    # def delete(self, fid):
    #     result = "Medication deleted"
    #     return result
    #
    # def update(self, fid, mname, mexpdate, msupplier, mbrand, mquantity, mlocation):
    #     result = "Medication updated"
    #     return result



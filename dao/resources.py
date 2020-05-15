# DAO Resources

from config.dbconfig import pg_config
import psycopg2

class ResourcesDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation from resources natural inner join rsupplier natural inner join suppliers natural inner join rlocation order by rtype;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesById(self, rid):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation from resources natural inner join rsupplier natural inner join suppliers natural inner join rlocation where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getResourcesByType(self, type):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation from resources natural inner join rsupplier natural inner join suppliers natural inner join rlocation where rtype = %s order by rtype;"
        cursor.execute(query, (type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByStatus(self, status):
        cursor = self.conn.cursor()
        if(status == 'reserved'):
            query = "select cid, rid, cfirstname, clastname, rtype, rbrand, rconsume_price, rconsume_quantity, rconsume_date, rconsume_payment_method from consumers natural inner join resources natural inner join rconsumes where rconsume_price = 0 or rconsume_payment_method = 'none' or rconsume_payment_method = 'None' or rconsume_payment_method = 'N/A';"
        elif (status == 'purchased'):
            query = "select cid, rid, cfirstname, clastname, rtype, rbrand, rconsume_price, rconsume_quantity, rconsume_date, rconsume_payment_method from consumers natural inner join resources natural inner join rconsumes where rconsume_price > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesConsumedByConsumerId(self, cid):
        cursor = self.conn.cursor()
        query = "select cid, rid, cfirstname, clastname, rtype, rbrand, rconsume_price, rconsume_quantity, rconsume_date, rconsume_payment_method from consumers natural inner join resources natural inner join rconsumes where cid = %s;"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesConsumedById(self, cid, rid):
        cursor = self.conn.cursor()
        query = "select cid, rid, cfirstname, clastname, rtype, rbrand, rconsume_price, rconsume_quantity, rconsume_date, rconsume_payment_method from consumers natural inner join resources natural inner join rconsumes where cid = %s and rid = %s;"
        cursor.execute(query, (cid, rid))
        result = cursor.fetchone()
        return result

    def getResourcesByLocation(self, location):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation from resources natural inner join rsupplier natural inner join suppliers natural inner join rlocation where rlocation = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByBrand(self, rbrand):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation from resources natural inner join rsupplier natural inner join suppliers natural inner join rlocation where rbrand = %s;"
        cursor.execute(query, (rbrand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByNumAvailable(self, rnumavailable):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation from resources natural inner join rsupplier natural inner join suppliers natural inner join rlocation where rnumavailable = %s;"
        cursor.execute(query, (rnumavailable,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByPrice(self, rprice):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation from resources natural inner join rsupplier natural inner join suppliers natural inner join rlocation where rprice = %s;"
        cursor.execute(query, (rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplier(self, rsupplier):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation from resources natural inner join rsupplier natural inner join suppliers natural inner join rlocation where rsupplier = %s;"
        cursor.execute(query, (rsupplier,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, rtype, rbrand, rnumavailable, rprice):
        cursor = self.conn.cursor()
        query = "insert into resources(rtype, rbrand, rnumavailable, rprice) values (%s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rtype, rbrand, rnumavailable, rprice,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def insertSupplier(self, rid, rsupplier):
        cursor = self.conn.cursor()
        query = "insert into rsupplier(rid, sid) values (%s, %s) returning rsupplier_id;"
        cursor.execute(query, (rid, rsupplier,))
        rsupplier_id = cursor.fetchone()[0]
        self.conn.commit()
        return rsupplier_id

    def insertLocation(self, rid, rlocation):
        cursor = self.conn.cursor()
        query = "insert into rlocation(rid, rlocation) values (%s, %s) returning rlocation_id;"
        cursor.execute(query, (rid, rlocation,))
        rlocation_id = cursor.fetchone()[0]
        self.conn.commit()
        return rlocation_id

    def insertFood(self, rid, fname, fexpdate):
        cursor = self.conn.cursor()
        query = "insert into food(rid, fname, fexpdate) values (%s, %s, %s) returning fid;"
        cursor.execute(query, (rid, fname, fexpdate,))
        fid = cursor.fetchone()[0]
        self.conn.commit()
        return fid

    def insertFuel(self, rid):
        cursor = self.conn.cursor()
        query = "insert into fuel(rid) values (%s) returning fuelid;"
        cursor.execute(query, (rid,))
        fuelid = cursor.fetchone()[0]
        self.conn.commit()
        return fuelid

    def insertEquipment(self, rid):
        cursor = self.conn.cursor()
        query = "insert into equipment(rid) values (%s) returning eid;"
        cursor.execute(query, (rid,))
        eid = cursor.fetchone()[0]
        self.conn.commit()
        return eid

    def insertMedicalDevices(self, rid):
        cursor = self.conn.cursor()
        query = "insert into medical_devices(rid) values (%s) returning mdid;"
        cursor.execute(query, (rid,))
        mdid = cursor.fetchone()[0]
        self.conn.commit()
        return mdid

    def insertWater(self, rid, wvolume, wexpdate):
        cursor = self.conn.cursor()
        query = "insert into water(rid, wvolume, wexpdate) values (%s, %s, %s) returning wid;"
        cursor.execute(query, (rid, wvolume, wexpdate,))
        wid = cursor.fetchone()[0]
        self.conn.commit()
        return wid

    def insertMedication(self, rid, mexpdate, mclass):
        cursor = self.conn.cursor()
        query = "insert into medications(rid, mexpdate, mclass) values (%s, %s, %s) returning mid;"
        cursor.execute(query, (rid, mexpdate, mclass,))
        mid = cursor.fetchone()[0]
        self.conn.commit()
        return mid

    def insertClothing(self, rid, cpiece, csex, csize):
        cursor = self.conn.cursor()
        query = "insert into clothing(rid, cpiece, csex, csize) values (%s, %s, %s, %s) returning clothes_id;"
        cursor.execute(query, (rid, cpiece, csex, csize,))
        clothes_id = cursor.fetchone()[0]
        self.conn.commit()
        return clothes_id

    def insertConsumption(self, cid, rid, rconsume_price, rconsume_quantity, rconsume_date, rconsume_payment_method):
        cursor = self.conn.cursor()
        query = "insert into rconsumes(cid, rid, rconsume_price, rconsume_quantity, rconsume_date, rconsume_payment_method) values (%s, %s, %s, %s, %s, %s) returning cid;"
        cursor.execute(query, (cid, rid, rconsume_price, rconsume_quantity, rconsume_date, rconsume_payment_method,))
        cid = cursor.fetchone()[0]
        self.conn.commit()
        return cid

    def insertRSupplies(self, sid, rid, rsupply_price, rsupply_quantity, rsupply_date):
        cursor = self.conn.cursor()
        query = "insert into rsupplies(sid, rid, rsupply_price, rsupply_quantity, rsupply_date) values (%s, %s, %s, %s, %s) returning sid;"
        cursor.execute(query, (sid, rid, rsupply_price, rsupply_quantity, rsupply_date,))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid

class FoodDAO(ResourcesDAO):
    def getAllFood(self):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, fid, fname, fexpdate from resources natural inner join rsupplier natural inner join food natural inner join suppliers natural inner join rlocation order by rtype;"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodById(self, fid):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, fid, fname, fexpdate from resources natural inner join rsupplier natural inner join food natural inner join suppliers natural inner join rlocation where fid = %s;"
        cursor.execute(query, (fid,))
        result = cursor.fetchone()
        return result

    def getFoodByName(self, fname):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, fid, fname, fexpdate from resources natural inner join rsupplier natural inner join food natural inner join suppliers natural inner join rlocation where fname = %s;"
        cursor.execute(query, (fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodByExpDate(self, fexpdate):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, fid, fname, fexpdate from resources natural inner join rsupplier natural inner join medications natural inner join suppliers natural inner join rlocation where fexpdate = %s;"
        cursor.execute(query, (fexpdate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

class EquipmentDAO(ResourcesDAO):
    def getAllEquipment(self):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, eid from resources natural inner join rsupplier natural inner join equipment natural inner join suppliers natural inner join rlocation order by rtype;"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipmentByID(self, eid):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, eid from resources natural inner join rsupplier natural inner join equipment natural inner join suppliers natural inner join rlocation where eid = %s;"
        cursor.execute(query, (eid,))
        result = cursor.fetchone()
        return result

class FuelDAO(ResourcesDAO):
    def getAllFuel(self):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, fuelid from resources natural inner join rsupplier natural inner join fuel natural inner join suppliers natural inner join rlocation order by rtype;"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelByID(self, fuid):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, fuelid from resources natural inner join rsupplier natural inner join fuel natural inner join suppliers natural inner join rlocation where fuelid = %s;"
        cursor.execute(query,(fuid,))
        result = []
        result = cursor.fetchone()
        return result

class MedDevDAO(ResourcesDAO):
    def getAllMedicalDevices(self):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, mdid from resources natural inner join rsupplier natural inner join medical_devices natural inner join suppliers natural inner join rlocation order by rtype;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicalDevicesByID(self, mdid):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, mdid from resources natural inner join rsupplier natural inner join medical_devices natural inner join suppliers natural inner join rlocation where mdid = %s;"
        cursor.execute(query, (mdid,))
        result = cursor.fetchone()
        return result

class MedicationDAO(ResourcesDAO):
    def getAllMedication(self):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, mid, mexpdate, mclass from resources natural inner join rsupplier natural inner join medications natural inner join suppliers natural inner join rlocation order by rtype;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicationByID(self, mid):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, mid, mexpdate, mclass from resources natural inner join rsupplier natural inner join medications natural inner join suppliers natural inner join rlocation where mid = %s;"
        cursor.execute(query, (mid,))
        result = []
        result = cursor.fetchone()
        return result

    def getMedicationByExpDate(self, mexpdate):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, mid, mexpdate, mclass from resources natural inner join rsupplier natural inner join medications natural inner join suppliers natural inner join rlocation where mid = %s;"
        cursor.execute(query, (mexpdate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicationByClass(self, mclass):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, mid, mexpdate, mclass from resources natural inner join rsupplier natural inner join medications natural inner join suppliers natural inner join rlocation where mclass = %s;"
        cursor.execute(query, (mclass,))
        result = []
        for row in cursor:
            result.append(row)
        return result

class WaterDAO(ResourcesDAO):
    def getAllWater(self):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, wid, wvolume, wexpdate from resources natural inner join rsupplier natural inner join water natural inner join suppliers natural inner join rlocation order by rtype;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWaterByID(self, wid):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, wid, wvolume, wexpdate from resources natural inner join rsupplier natural inner join water natural inner join suppliers natural inner join rlocation where wid = %s;"
        cursor.execute(query, (wid,))
        result = []
        result = cursor.fetchone()
        return result

    def getWaterByVolume(self, wvolume):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, wid, wvolume, wexpdate from resources natural inner join rsupplier natural inner join water natural inner join suppliers natural inner join rlocation where wvolume = %s;"
        cursor.execute(query, (wvolume,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWaterByExpDate(self, wexpdate):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, wid, wvolume, wexpdate from resources natural inner join rsupplier natural inner join water natural inner join suppliers natural inner join rlocation where wexpdate = %s;"
        cursor.execute(query, (wexpdate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

class ClothingDAO(ResourcesDAO):
    def getAllClothing(self):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, clothes_id, cpiece, csex, csize from resources natural inner join rsupplier natural inner join clothing natural inner join suppliers natural inner join rlocation order by rtype;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingByID(self, cid):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, clothes_id, cpiece, csex, csize from resources natural inner join rsupplier natural inner join clothing natural inner join suppliers natural inner join rlocation where clothes_id = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result

    def getClothingByPiece(self, cpiece):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, cid, cpiece, csex, csize from resources natural inner join rsupplier natural inner join clothing natural inner join suppliers natural inner join rlocation where cpiece = %s;"
        cursor.execute(query, (cpiece,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingBySex(self, csex):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, cid, cpiece, csex, csize from resources natural inner join rsupplier natural inner join clothing natural inner join suppliers natural inner join rlocation where csex = %s;"
        cursor.execute(query, (csex,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingBySize(self, csize):
        cursor = self.conn.cursor()
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation, cid, cpiece, csex, csize from resources natural inner join rsupplier natural inner join clothing natural inner join suppliers natural inner join rlocation where csize = %s;"
        cursor.execute(query, (csize,))
        result = []
        for row in cursor:
            result.append(row)
        return result
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
        query = "select rid, rtype, rbrand, rnumavailable, rprice, sorganization, rlocation from resources natural inner join rsupplier natural inner join suppliers natural inner join rlocation where rtype = %s;"
        cursor.execute(query, (type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByStatus(self, status):
        cursor = self.conn.cursor()
        if(status == 'reserved'):
            query = "select cid, rid, cfirstname, clastname, rtype, rbrand, rconsume_price, rconsume_quantity, rconsume_date, rconsume_payment_method from consumers natural inner join resources natural inner join rconsumes where rconsume_price = 0;"
        elif (status == 'purchased'):
            query = "select cid, rid, cfirstname, clastname, rtype, rbrand, rconsume_price, rconsume_quantity, rconsume_date, rconsume_payment_method from consumers natural inner join resources natural inner join rconsumes where rconsume_price > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesConsumedById(self, cid):
        cursor = self.conn.cursor()
        query = "select cid, rid, cfirstname, clastname, rtype, rbrand, rconsume_price, rconsume_quantity, rconsume_date, rconsume_payment_method from consumers natural inner join resources natural inner join rconsumes where cid = 5;"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
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
        result = "List of resources of a specific brand"
        return result

    def getResourcesByNumAvailable(self, rnumavailable):
        result = "Number of available resources"
        return result

    def getResourcesByPrice(self, rprice):
        result = "List of resources of specified price"
        return result

    def getResourcesBySupplier(self, rsupplier):
        result = "List of resources of a specific supplier"
        return result


    def insert(self, rtype, rbrand, rnumavailable, rprice, rsupplier, rlocation):
        result = "Supplier inserted"
        return result



class FoodDAO(ResourcesDAO):
    def getAllFood(self):
        result = "This means the refactor is working!"
        return result

    def getFoodId(self, fid):
        result = "This is the resource with given id"
        return result

    def getFoodByName(self, fname):
        result = "List of resources of a specific type"
        return result

    def getFoodByExpDate(self, fexpdate):
        result = "List of resources of a specific brand"
        return result

class EquipmentDAO(ResourcesDAO):
    def getAllEquipment(self):
        result = "This is a list of resources"
        return result

    def getEquipmentByID(self, eid):
        result = "This is a list of resources"
        return result

class FuelDAO(ResourcesDAO):
    def getAllFuel(self):
        result = "This is a list of resources"
        return result

    def getFuelByID(self, fuid):
        result = "This is a list of resources"
        return result

class MedDevDAO(ResourcesDAO):
    def getAllMedicalDevices(self):
        result = "This is a list of resources"
        return result

    def getMedicalDevicesByID(self, mdid):
        result = "This is a list of resources"
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
        result = "This is a list of resources"
        return result

    def getMedicationByExpDate(self, mexpdate):
        result = "This is a list of resources"
        return result

    def getMedicationByClass(self, mclass):
        result = "This is a list of resources"
        return result

class WaterDAO(ResourcesDAO):
    def getAllWater(self):
        result = "This is a list of resources"
        return result

    def getWaterByID(self, wid):
        result = "This is a list of resources"
        return result

    def getWaterByVolume(self, wvolume):
        result = "This is a list of resources"
        return result

    def getWaterByExpDate(self, wexpdate):
        result = "This is a list of resources"
        return result

class ClothingDAO(ResourcesDAO):
    def getAllClothing(self):
        result = "This is a list of resources"
        return result

    def getClothingByID(self, cid):
        result = "This is a list of resources"
        return result

    def getClothingByPiece(self, cpiece):
        result = "This is a list of resources"
        return result

    def getClothingBySex(self, csex):
        result = "This is a list of resources"
        return result

    def getClothingBySize(self, csize):
        result = "This is a list of resources"
        return result
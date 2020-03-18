
rows, columns = (5, 5)
FuelDB = [[0 for x in range(rows)] for y in range(columns)]
FuelDB[0] = [1, 'Gasoline', 'Wal-Mart', 30, 'San Juan']
FuelDB[1] = [2, 'Diesel', 'Amazon', 20, 'San Juan']
FuelDB[2] = [3, 'Gasoline', 'Jonathan', 3, 'Mayaguez']
FuelDB[3] = [4, 'Propane', 'Angel', 4, 'Mayaguez']
FuelDB[4] = [5, 'Diesel', 'Gilson', 30, 'Mayaguez']

class FuelDAO:

    def getAllFuel(self):
        result = []
        for row in FuelDB:
            result.append(row)
        return result





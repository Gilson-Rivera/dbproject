import psycopg2

conn = psycopg2.connect("dbname=appdb user=appusr password=ciic4060 host=127.0.0.1")
cursor = conn.cursor()
# cursor.execute("select * from part")
# cursor.execute("select * from part where pprice >= 4")
# for row in cursor:
#     print(row)
cursor.execute("select * from Suppliers")
for row in cursor:
    print(row)
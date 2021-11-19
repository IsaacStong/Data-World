import cx_Oracle

connection = cx_Oracle.connect("SCOTT/TIGER")
cursor = connection.cursor()

cursor.execute("SELECT column_name, data_type FROM USER_TAB_COLUMNS WHERE table_name = 'EMP'")
r = cursor.fetchall()
print(r)

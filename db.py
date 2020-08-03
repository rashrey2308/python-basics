import mysql.connector
conn = mysql.connector.connect(host='localhost',database='mydb',user='root',password='anvinirash')
if conn.is_connected():
    print("Connected to mysql db")
cursor = conn.cursor()
try:
    cursor.execute("insert into tourneys values('A',1,2,3,4)")
    conn.commit()
    print("Row Added")
    cursor.execute("insert into dinners values('A','1991-01-01','A','A','A')")
    conn.commit()
    print("Row Added")
except:
    conn.rollback()

#cursor.execute('select * from tourneys')
cursor.execute('select * from dinners where name="A"')

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()

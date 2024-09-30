import mysql.connector

data=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mock"
)

access=data.cursor()

query=("select * from products")
access.execute(query)
access.execute(query)

query=("select * from products")
access.execute(query)

rows=access.fetchall()
for i in rows:
    print(i)

data.commit()

access.close()
data.close()
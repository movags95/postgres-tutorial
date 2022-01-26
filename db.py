from psycopg2 import extras
import psycopg2

#connect to your db
connection = psycopg2.connect(
    host="localhost",
    database="mohitdb",
    user="postgres",
    password="postgres",
    port=5555
)

#create a cursor. the params allow for rows to be returned as a dict
cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

cursor.execute("select id, name from employees")

rows = cursor.fetchall()

for row in rows:
    # print(row)
    # print(row[0])
    # print(row[1])
    print(row['id'])
    print(row['name'])

#close the cursor
cursor.close()

#close the connection
connection.close()
### pip install psycopg2 --user
import psycopg2

conn = psycopg2.connect("host=localhost port=5432 user=docker password=XdccDa85_JK dbname=docker")

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS currencies(id SERIAL PRIMARY KEY, name VARCHAR(3))")

insert = "INSERT INTO currencies (name) VALUES (%s) RETURNING ID"

# The binding needs to be to a tuple, so the comma is important even if you have only one argument ('val',) 
cur.execute(insert, ("EUR",))
id = cur.fetchone()[0]
print('inserted ' , str(id))


cur.execute(insert, ('CHF',)) 
id = cur.fetchone()[0]
print('inserted ' , str(id))

cur.execute("SELECT id, name FROM currencies")
print("The number of currencies: ", cur.rowcount)
row = cur.fetchone()

while row is not None:
    print(row)
    row = cur.fetchone()

cur.close()
conn.close()
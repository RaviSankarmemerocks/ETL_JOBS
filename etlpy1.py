import psycopg2 
from pprint import pprint

conn = psycopg2.connect("host=localhost dbname=mydbetl user=postgres password=root")
if conn:
	print ("connected")
else:
	print("something went wrong")	
cur=conn.cursor()
table=cur.execute('select * from titanic.test')
pprint(table)
conn.commit()
one = cur.fetchone()
aall = cur.fetchall()

if cur.execute('select * from titanic.test'):
	print ("true")
else:	
	print ("false")

conn.close()

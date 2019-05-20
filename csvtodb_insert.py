import csv
import psycopg2
conn = psycopg2.connect("host=localhost dbname=mydbetl user=postgres password=root")
if conn:
	print ("success")
else:
	print ("failed")

cur = conn.cursor()
with open('cleanedship.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader) 
	for row in reader:
		cur.execute("INSERT INTO titanic VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)",row)
conn.commit()
import csv
import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=root")
if conn:
	print ("success")
else:
	print ("failed")

cur = conn.cursor()
with open('train.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader) 
	for row in reader:
		cur.execute("INSERT INTO titanic (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)",row)
conn.commit()

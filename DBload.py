import pymssql
import csv

dbserver = input('Enter hostname of DB server:')
db = input('Enter DB name:')
dbuser = input('Enter Username with DB access:')
dbpasswd = input('Enter password for above user:')
file = input('Enter the location of data dump:')


conn = pymssql.connect(dbserver, dbuser, dbpasswd, db)
cursor = conn.cursor()

with open(file) as f:
    for row in csv.DictReader(f):
         x = row['errorcode']
         y = row['description']
         z = row['solution']
         q = 'INSERT INTO testtable(errorcode, description, solution) VALUES(%s, %s, %s)'
         cursor.execute(q, (x, y, z))

conn.commit()
conn.close()



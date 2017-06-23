import pymssql
import socket

dbserver="localhost" #### This is the name of MSSQL Server
dbuser="root" #### Username that have admin privileges on DB
dbpasswd="Infy123+" #### Password of above user
db="test" #### Name of the datbase 
hostname=socket.gethostname()


with open('/root/ccmsetup.log', 'r') as f:
    for line in f:
       if "CcmSetup failed with error code" in line:
           linereq = line

errorcode = linereq.split(' ')[5].split(']')[0]

conn = pymssql.connect(dbserver, dbuser, dbpasswd, db)
cursor = conn.cursor()

#### Replace testtable with first table that you had created
sql = "SELECT solution FROM testtable\
       WHERE name = '%s'" % (errorcode)

cursor.execute(sql)

results = cursor.fetchall()
for row in results:
      solution = row[0]

#### Relace errortable with second table that you had created
q = 'INSERT INTO errortable(errorcode, hostname, solution) VALUES(%s, %s, %s)'
cursor.execute(q, (errorcode, hostname, solution))
conn.commit()
conn.close()

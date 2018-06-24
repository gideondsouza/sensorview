#!/usr/bin/python3
#import _mysql
import MySQLdb
import MySQLdb.cursors

#import _mysql.cursors
from pprint import pprint
db=MySQLdb.connect(host="localhost", user="root", passwd="amsterdam678", 
db="dataloggerDB", cursorclass=MySQLdb.cursors.DictCursor)
c = db.cursor()
c.execute("SELECT id, logtime, sensorID,messwert  FROM dataloggerDB.messwerteTBL WHERE 1")
#db.query("SELECT id, logtime, sensorID,messwert  FROM dataloggerDB.messwerteTBL WHERE 1")

#ret = db.store_result()
R = c.fetchmany(20)
print(type(R))
pprint(R[0])
pprint(R[1])



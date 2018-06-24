import logging
from flask import Blueprint, render_template
import MySQLdb
import MySQLdb.cursors
from pprint import pprint

import sys
import json 

main = Blueprint('main', __name__)


#@main.route('/')
def index():
    return "Main"

@main.route('/')
def display_books():
#import _mysql.cursors
    db=MySQLdb.connect(host="localhost", user="root", passwd="amsterdam678", 
    db="dataloggerDB", cursorclass=MySQLdb.cursors.DictCursor)
    c = db.cursor()
    c.execute("SELECT id, logtime, sensorID,messwert  FROM dataloggerDB.messwerteTBL WHERE 1")

    R = c.fetchall()
    #pprint(R)
    c.close()
    return render_template("home.html", the_data=list(R))
    
@main.route('api/data/')
def get_sensordata():
    dat= []
    return dat



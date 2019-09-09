from sense_hat         import SenseHat
from time              import sleep
import mysql.connector as mariadb

# --- configuratie
dbconfig = {
    'user':     'backend-service',
    'password': 'geheim!',
    'host':     'localhost',
    'database': 'kastje',
}


# --- static variables

hat      = SenseHat()
conn     = mariadb.connect(**dbconfig)
cursor   = conn.cursor()

# todo

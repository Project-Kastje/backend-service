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

sense    = SenseHat()
conn     = mariadb.connect(**dbconfig)
cursor   = conn.cursor()

# --- main loop

def iterate():
    accel = sense.get_accelerometer_raw()
    x = abs(accel['x'])
    y = abs(accel['x'])
    z = abs(accel['z'])
    #if x > 1 or y > 1 or z > 1:
    if x > 0.15 or y > 0.15:
        print("INDRINGER")

try:
    while True:
        iterate()

except KeyboardInterrupt:
    print("\n")

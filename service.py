from sense_hat         import SenseHat
from time              import sleep
import os
import pygame
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

# --- functies

def alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("/etc/project-kastje/backend-service/8608.wav")
    pygame.mixer.music.play()
    os.system("bash /etc/project-kastje/backend-service/push-wrapper.sh")

# --- main loop

def iterate():
    accel = sense.get_accelerometer_raw()
    x = abs(accel['x'])
    y = abs(accel['x'])
    z = abs(accel['z'])
    #if x > 1 or y > 1 or z > 1:
    if x > 0.15 or y > 0.15:
        print("INDRINGER")
        alarm()

f = open("backend-service.log", "a")
f.write("Start service")

if os.geteuid() != 0:
    f.write("ROOT NODIG!!!!!")
    f.close()
    exit("Root is nodig voor het uitvoeren van dit script!")

f.write("OK")
f.close()

try:
    while True:
        iterate()

except KeyboardInterrupt:
    print("\n")

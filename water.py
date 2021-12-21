# External module import
import RPi.GPIO as GPIO
import datetime
import time
from time import strftime
import os
import glob
import mariadb
import sys

#Variables for MySQL
conn = mariadb.connect(host="localhost", user="admin", password="admin", database="sensor") # definiálja az adatbázis kapcsolatot
cur = conn.cursor() # csatlakozik az adatbázishoz

init = False

GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme

def get_last_watered():
    try:
        f = open("last_watered.txt", "r") # megnyitja olvasásra a "last_watered.txt file-t => ha nincs ilyen nevű file, akkor crash történt eddig. Javítva.
        return f.readline() # visszaadja a file tartalmát.
    except: # ha nem sikerül végrehajtani
        f = open("last_watered.txt", "w+") # nyissa meg írásra létrehozási jogosultsággal a "last-watered.txt" file-t.
        f.write("First Start {}".format(datetime.datetime.now())) #Első futás ideje, nincs "last-watered.txt" ezért létrehozza a program a file-t a Pi-n.
        f.close() # zárja le a file-t.
    return "File Created!" # adja vissza a "File Created!" értéket.
      
def get_status(pin = 8): # nedvesség szenzor értékének lekérése / nedvesség szenzor jelenleg a 8-as PIN-re van kötve
    GPIO.setup(pin, GPIO.IN)  # GPIO konfiguráció 8 PIN/bemeneti érték 
    return GPIO.input(pin) # adja vissza a PIN logikai értékét (0 vagy 1)

def init_output(pin): #GPIO OUTPUT értékek meghatározása
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
    
def auto_water(delay = 5, pump_pin = 7, water_sensor_pin = 8): # auto_water funkció (késleltetés = 5 sec / szivattyú a 7-es GPIO PIN-re van kötve / nedvesség szenzor a 8-as GPIO PIN-re van kötve)
    consecutive_water_count = 0 #hányszor öntöztük változó "0"-ra állítása.
    init_output(pump_pin) # inicializáljuk a szivattyú GPIO PIN értékeit.
    print("Watering Started! Press CTRL+C to exit") # "Jelző Üzenet: Elkezdődött az öntözés, CTRL+C-vel meg lehet szakítani a scriptet."
    try:
        while 1 and consecutive_water_count < 10: # amíg az aktuális öntözési számláló + 1 kisebb, mint "10", fusson le a ciklus
            time.sleep(delay) # 5 sec késleltetés
            wet = get_status(pin = water_sensor_pin) == 1 # kódban a szenzor rossz értékre volt állítva, akkor nedves a talaj, ha ez az érték "1", átállítva "0"->"1"-re
            if not wet: # ha nem nedves a talaj (szenzor logikai értéke = 0)
                if consecutive_water_count < 5: # ha 5-nél kisebb az "öntözési számláló"
                    pump_on(pump_pin, 5)  #cső hosszúságtól függően lehet, hogy a "delay" értéke kevés lesz, több próbát igényel. Kapcsolja be a szivattyút (szivattyú GPIO PIN száma "7" / 5-ös késleltetés)
                consecutive_water_count += 1 # növelje az aktuális öntözések számát +1-el
                                current_time=format(datetime.datetime.now())
                watered=get_last_watered() #változóba teszi a szenzor értéket
                secs = float(time.time())  #UNIX idő formátum
                secs = secs*1000
                sql = ("INSERT INTO soil_sensor (datetime,wet,water_count,Last_Watered) VALUES (%s,%s,%s,%s)", (secs, last_reading, consecutive_water_count, watered)) # adatbázisba új bejegyzés
                try: # adatbázisra futtatni a definiált SQL query-t.
                    print ("Writing to the database...")
                    cur.execute(*sql)
                    conn.commit()
                    print ("Write complete")
                except:
                    conn.rollback()
                    print ("We have a problem")
                    cur.close()
                    conn.close()
            else: # különben 
                consecutive_water_count = 0 # 0-a értékre állítsa az aktuális öntözések számát.
    except KeyboardInterrupt: # Ha CTRL+C -t megnyomták , lépjen ki a kódból és szabadítsa fel a GPIO erőforrásokat
        GPIO.cleanup() # szabadítsa fel a GPIO erőforrásokat

def pump_on(pump_pin = 7, delay = 1): # szivattyú bekapcsolás funkció (GPIO PIN 7 * késleltetés 1)
    init_output(pump_pin) # konfigurálja a GPIO PIN-t
    f = open("last_watered.txt", "w") #nyissa meg a "last_watered.txt"-t írásra
    f.write("Last watered {}".format(datetime.datetime.now())) #írja bele az aktuális dátum&idő-t.
    f.close() # zárja le a file-t.
    GPIO.output(pump_pin, GPIO.LOW) #állítsa a szivattyú GPIO értékét "LOW"-ra.
    time.sleep(1) #1 sec késleltetés
    GPIO.output(pump_pin, GPIO.HIGH) # állítsa a szivattyú GPIO  értékét "HIH"-ra.
    

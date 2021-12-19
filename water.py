# External module imp
import RPi.GPIO as GPIO
import datetime
import time

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
      
def get_status(pin = 8):
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
    
def auto_water(delay = 5, pump_pin = 7, water_sensor_pin = 8):
    consecutive_water_count = 0
    init_output(pump_pin)
    print("Here we go! Press CTRL+C to exit")
    try:
        while 1 and consecutive_water_count < 10:
            time.sleep(delay)
            wet = get_status(pin = water_sensor_pin) == 1 # kódban a szenzor rossz értékre volt állítva, akkor nedves a talaj, ha ez az érték "1", átállítva "0"->"1"-re
            if not wet:
                if consecutive_water_count < 5:
                    pump_on(pump_pin, 1)  #cső hosszúságtól függően lehet, hogy a "delay" értéke kevés lesz, több próbát igényel.
                consecutive_water_count += 1
            else:
                consecutive_water_count = 0
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPI

def pump_on(pump_pin = 7, delay = 1):
    init_output(pump_pin)
    f = open("last_watered.txt", "w")
    f.write("Last watered {}".format(datetime.datetime.now()))
    f.close()
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pump_pin, GPIO.HIGH)
    

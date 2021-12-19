from flask import Flask, render_template, redirect, url_for # flask webserver modulok importálása
import psutil # psutil importálása
import datetime # date-time importálása
import water # water.py importálása
import os # OS modul importálása

app = Flask(__name__) 

def template(title = "HELLO!", text = ""):
    now = datetime.datetime.now()
    timeString = now
    templateDate = {
        'title' : title,
        'time' : timeString,
        'text' : text
        }
    return templateDate

@app.route("/")
def hello(): # töltsbe be a main.html file-t.
    templateData = template()
    return render_template('main.html', **templateData)

@app.route("/last_watered") # megjeleníti a "get_last_watered" funkció kimeneti értékét
def check_last_watered():
    templateData = template(text = water.get_last_watered())
    return render_template('main.html', **templateData)

@app.route("/sensor")
def action(): # nedvesség szenzor értéknek megfelelően megjelenített üzenet.
    status = water.get_status()
    message = ""
    if (status == 1):
        message = "Water me please!"
    else:
        message = "I'm a happy plant"

    templateData = template(text = message)
    return render_template('main.html', **templateData)

@app.route("/water")
def action2(): #ha megfelelő gombra nyomtunk, akkor aktiválja a szivattyút "egyszer"
    water.pump_on()
    templateData = template(text = "Watered Once")
    return render_template('main.html', **templateData)

@app.route("/auto/water/<toggle>")
def auto_water(toggle): # aktiváljuk az auto_water script-et
    running = False
    if toggle == "ON":
        templateData = template(text = "Auto Watering On")
        for process in psutil.process_iter():
            try:
                if process.cmdline()[1] == 'auto_water.py':
                    templateData = template(text = "Already running")
                    running = True
            except:
                pass
        if not running:
            os.system("python3.4 auto_water.py&")
    else:
        templateData = template(text = "Auto Watering Off")
        os.system("pkill -f water.py")

    return render_template('main.html', **templateData)

if __name__ == "__main__": #konfiguráljuk az IP-t és a port-ot
    app.run(host='0.0.0.0', port=80, debug=True)

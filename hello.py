from flask import Flask
from flask import render_template

#import des utilistaires python
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

def init_led(broche):
    #Utilisation d'une norme de nommage pour les broches
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    #initialisation de la broche en mode "sortie"
    # Le nombre passé en paramètre correspond au numéro de GPIO et non au numéro de la broche.
    GPIO.setup(broche, GPIO.OUT)
    return 0

@app.route('/')
def hello_world():
    return render_template('hello.html') 

@app.route('/on')
@app.route('/on/<int:broche>')
def lightOn(broche=None):
    #Initialisation des leds
    init_led(14)
    init_led(15)
    #Si le numero de broche n'est pas indiqué
    if broche == None:
        print("Leds On")
        GPIO.output(14, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        return "leds on"
    elif broche in [14, 15]:
        print("Led", broche, "on")
        GPIO.output(broche, GPIO.HIGH)
        return "led " + str(broche) + " on"
    else:
        print("broche non affectee")
        return "broche non affectee"

@app.route('/off')
@app.route('/off/<int:broche>')
def lightOff(broche=None):
    #Initialisation des leds
    init_led(14)
    init_led(15)
    #Si le numero de broche n'est pas indiqué
    if broche == None:
        print("Leds Off")
        GPIO.output(14, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        return "leds off"
    elif broche in [14, 15]:
        print("Led", broche, "off")
        GPIO.output(broche, GPIO.LOW)
        return "led " + str(broche) + " off"
    else:
        print("broche non affectee")
        return "broche non affectee"


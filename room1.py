import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs
room1light = 23
room1fan =  27  #24
room1aircon = 26 #21

#initialize GPIO status variables
room1lightSts = 0
room1fanSts = 0
room1airconSts = 0

# Define led pins as output
GPIO.setup(room1light, GPIO.OUT)   
GPIO.setup(room1fan, GPIO.OUT) 
GPIO.setup(room1aircon, GPIO.OUT)

# turn leds OFF 
GPIO.output(room1light, GPIO.LOW)
GPIO.output(room1fan, GPIO.LOW)
GPIO.output(room1aircon, GPIO.LOW)
    
@app.route("/")
def index():
    # Read Sensors Status
    room1lightSts = GPIO.input(room1light)
    room1fanSts = GPIO.input(room1fan)
    room1airconSts = GPIO.input(room1aircon)
    
    templateData = {
              'title' : 'GPIO Output Status!',
              
              'room1light'  : room1lightSts,
              'room1fan'  : room1fanSts,
              'room1aircon'  : room1airconSts,
        }
    return render_template('main.html', **templateData)
    
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'room1light':
        actuator = room1light
    if deviceName == 'room1fan':
        actuator = room1fan
    if deviceName == 'room1aircon':
        actuator = room1aircon
   
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
             
    room1lightSts = GPIO.input(room1light)
    room1fanSts = GPIO.input(room1fan)
    room1airconSts = GPIO.input(room1aircon)
   
    templateData = {
              'room1light'  : room1lightSts,
              'room1fan'  : room1fanSts,
              'room1aircon'  : room1airconSts,
    }
    return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)

import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs
room3light = 5
room3fan = 6
room3aircon = 21 #26 

#initialize GPIO status variables
room3lightSts = 0
room3fanSts = 0
room3airconSts = 0

# Define led pins as output
GPIO.setup(room3light, GPIO.OUT)   
GPIO.setup(room3fan, GPIO.OUT) 
GPIO.setup(room3aircon, GPIO.OUT)

# turn leds OFF 
GPIO.output(room3light, GPIO.LOW)
GPIO.output(room3fan, GPIO.LOW)
GPIO.output(room3aircon, GPIO.LOW)
    
@app.route("/")
def index():
    # Read Sensors Status
    room3lightSts = GPIO.input(room3light)
    room3fanSts = GPIO.input(room3fan)
    room3airconSts = GPIO.input(room3aircon)
    
    templateData = {
              'title' : 'GPIO Output Status!',
              
              'room3light'  : room3lightSts,
              'room3fan'  : room3fanSts,
              'room3aircon'  : room3airconSts,
        }
    return render_template('main.html', **templateData)
    
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'room3light':
        actuator = room3light
    if deviceName == 'room3fan':
        actuator = room3fan
    if deviceName == 'room3aircon':
        actuator = room3aircon
   
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
             
    room3lightSts = GPIO.input(room3light)
    room3fanSts = GPIO.input(room3fan)
    room3airconSts = GPIO.input(room3aircon)
   
    templateData = {         
              'room3light'  : room3lightSts,
              'room3fan'  : room3fanSts,
              'room3aircon'  : room3airconSts,
    }
    return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)

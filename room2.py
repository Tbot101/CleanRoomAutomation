import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs
room2light = 17
room2fan = 24 #27
room2aircon = 22 


#initialize GPIO status variables
room2lightSts = 0
room2fanSts = 0
room2airconSts = 0


# Define led pins as output
GPIO.setup(room2light, GPIO.OUT)   
GPIO.setup(room2fan, GPIO.OUT) 
GPIO.setup(room2aircon, GPIO.OUT)

# turn leds OFF 
GPIO.output(room2light, GPIO.LOW)
GPIO.output(room2fan, GPIO.LOW)
GPIO.output(room2aircon, GPIO.LOW)
    
@app.route("/")
def index():
    # Read Sensors Status    
    room2lightSts = GPIO.input(room2light)
    room2fanSts = GPIO.input(room2fan)
    room2airconSts = GPIO.input(room2aircon)
    
    templateData = {
              'title' : 'GPIO Output Status!',
              
              'room2light'  : room2lightSts,
              'room2fan'  : room2fanSts,
              'room2aircon'  : room2airconSts,
        }
    return render_template('main.html', **templateData)
    
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'room2light':
        actuator = room2light
    if deviceName == 'room2fan':
        actuator = room2fan
    if deviceName == 'room2aircon':
        actuator = room2aircon
   
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
             
    room2lightSts = GPIO.input(room2light)
    room2fanSts = GPIO.input(room2fan)
    room2airconSts = GPIO.input(room2aircon)
   
    templateData = {
              'room2light'  : room2lightSts,
              'room2fan'  : room2fanSts,
              'room2aircon'  : room2airconSts,
    }
    return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)

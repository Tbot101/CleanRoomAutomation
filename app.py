import RPi.GPIO as GPIO
from flask import Flask, render_template, request
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# define actuators GPIOs
room1light = 27
room1fan = 12  # 24
room1aircon = 26  # 21

room2light = 17
room2fan = 13  # 27
room2aircon = 22

room3light = 5
room3fan = 6
room3aircon = 21  # 26

# initialize GPIO status variables
room1lightSts = 0
room1fanSts = 0
room1airconSts = 0

room2lightSts = 0
room2fanSts = 0
room2airconSts = 0

room3lightSts = 0
room3fanSts = 0
room3airconSts = 0

# Define led pins as output
GPIO.setup(room1light, GPIO.OUT)
GPIO.setup(room1fan, GPIO.OUT)
GPIO.setup(room1aircon, GPIO.OUT)

GPIO.setup(room2light, GPIO.OUT)
GPIO.setup(room2fan, GPIO.OUT)
GPIO.setup(room2aircon, GPIO.OUT)

GPIO.setup(room3light, GPIO.OUT)
GPIO.setup(room3fan, GPIO.OUT)
GPIO.setup(room3aircon, GPIO.OUT)

# turn leds OFF
GPIO.output(room1light, GPIO.LOW)
GPIO.output(room1fan, GPIO.LOW)
GPIO.output(room1aircon, GPIO.LOW)

GPIO.output(room2light, GPIO.LOW)
GPIO.output(room2fan, GPIO.LOW)
GPIO.output(room2aircon, GPIO.LOW)

GPIO.output(room3light, GPIO.LOW)
GPIO.output(room3fan, GPIO.LOW)
GPIO.output(room3aircon, GPIO.LOW)

p1 = GPIO.PWM(room1fan, 500)
p1.start(0)
p2 = GPIO.PWM(room2fan, 500)
p2.start(0)
p3 = GPIO.PWM(room3fan, 500)
p3.start(0)

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    # Read Sensors Status
    room1lightSts = GPIO.input(room1light)
    room1fanSts = GPIO.input(room1fan)
    room1airconSts = GPIO.input(room1aircon)

    room2lightSts = GPIO.input(room2light)
    room2fanSts = GPIO.input(room2fan)
    room2airconSts = GPIO.input(room2aircon)

    room3lightSts = GPIO.input(room3light)
    room3fanSts = GPIO.input(room3fan)
    room3airconSts = GPIO.input(room3aircon)

    templateData = {
        'title': 'GPIO Output Status!',

        'room1light': room1lightSts,
        'room1fan': room1fanSts,
        'room1aircon': room1airconSts,

        'room2light': room2lightSts,
        'room2fan': room2fanSts,
        'room2aircon': room2airconSts,

        'room3light': room3lightSts,
        'room3fan': room3fanSts,
        'room3aircon': room3airconSts,
    }
    return render_template('main.html', **templateData)


@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    actuator = eval(deviceName)

    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)

    room1lightSts = GPIO.input(room1light)
    room1fanSts = GPIO.input(room1fan)
    room1airconSts = GPIO.input(room1aircon)

    room2lightSts = GPIO.input(room2light)
    room2fanSts = GPIO.input(room2fan)
    room2airconSts = GPIO.input(room2aircon)

    room3lightSts = GPIO.input(room3light)
    room3fanSts = GPIO.input(room3fan)
    room3airconSts = GPIO.input(room3aircon)

    templateData = {
        'room1light': room1lightSts,
        'room1fan': room1fanSts,
        'room1aircon': room1airconSts,

        'room2light': room2lightSts,
        'room2fan': room2fanSts,
        'room2aircon': room2airconSts,

        'room3light': room3lightSts,
        'room3fan': room3fanSts,
        'room3aircon': room3airconSts,
    }
    return render_template('main.html', **templateData)

@app.route("/testroom1", methods=["POST"])
def testroom1():

    
    room1lightSts = GPIO.input(room1light)
    room1fanSts = GPIO.input(room1fan)
    room1airconSts = GPIO.input(room1aircon)

    room2lightSts = GPIO.input(room2light)
    room2fanSts = GPIO.input(room2fan)
    room2airconSts = GPIO.input(room2aircon)

    room3lightSts = GPIO.input(room3light)
    room3fanSts = GPIO.input(room3fan)
    room3airconSts = GPIO.input(room3aircon)
    
    templateData = {
        'room1light': room1lightSts,
        'room1fan': room1fanSts,
        'room1aircon': room1airconSts,

        'room2light': room2lightSts,
        'room2fan': room2fanSts,
        'room2aircon': room2airconSts,

        'room3light': room3lightSts,
        'room3fan': room3fanSts,
        'room3aircon': room3airconSts,
    }
    
    
    # Get slider Values
    slider1 = request.form["Room_1_Fan_Slider"]
    # Change duty cycle
    p1.ChangeDutyCycle(float(slider1))
    # Give servo some time to move
    sleep(1)
    
    return render_template('main.html', **templateData)

@app.route("/testroom2", methods=["POST"])
def testroom2():


    room1lightSts = GPIO.input(room1light)
    room1fanSts = GPIO.input(room1fan)
    room1airconSts = GPIO.input(room1aircon)

    room2lightSts = GPIO.input(room2light)
    room2fanSts = GPIO.input(room2fan)
    room2airconSts = GPIO.input(room2aircon)

    room3lightSts = GPIO.input(room3light)
    room3fanSts = GPIO.input(room3fan)
    room3airconSts = GPIO.input(room3aircon)
    
    templateData = {
        'room1light': room1lightSts,
        'room1fan': room1fanSts,
        'room1aircon': room1airconSts,

        'room2light': room2lightSts,
        'room2fan': room2fanSts,
        'room2aircon': room2airconSts,

        'room3light': room3lightSts,
        'room3fan': room3fanSts,
        'room3aircon': room3airconSts,
    }
    
    # Get slider Values
    slider2 = request.form["Room_2_Fan_Slider"]
    # Change duty cycle
    p2.ChangeDutyCycle(float(slider2))
    # Give servo some time to move
    sleep(1)
    
    return render_template('main.html', **templateData)

@app.route("/testroom3", methods=["POST"])
def testroom3():
        
    # Get slider Values
    slider3 = request.form["Room_3_Fan_Slider"]
    # Change duty cycle
    p3.ChangeDutyCycle(float(slider3))
    # Give servo some time to move
    sleep(1)

    room1lightSts = GPIO.input(room1light)
    room1fanSts = GPIO.input(room1fan)
    room1airconSts = GPIO.input(room1aircon)

    room2lightSts = GPIO.input(room2light)
    room2fanSts = GPIO.input(room2fan)
    room2airconSts = GPIO.input(room2aircon)

    room3lightSts = GPIO.input(room3light)
    room3fanSts = GPIO.input(room3fan)
    room3airconSts = GPIO.input(room3aircon)
    
    templateData = {
        'room1light': room1lightSts,
        'room1fan': room1fanSts,
        'room1aircon': room1airconSts,

        'room2light': room2lightSts,
        'room2fan': room2fanSts,
        'room2aircon': room2airconSts,

        'room3light': room3lightSts,
        'room3fan': room3fanSts,
        'room3aircon': room3airconSts,
    }
    
    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
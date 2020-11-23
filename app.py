import RPi.GPIO as GPIO
from flask import Flask, render_template, request
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


roomPins = {
    # define actuators GPIOs
    'room1light': {
        'pin': 27,
        'status': 0,
    },
    'room1fan': {
        'pin': 12,
        'status': 0,
    },
    'room1aircon': {
        'pin': 26,
        'status': 0,
    },

    'room2light': {
        'pin': 17,
        'status': 0,
    },
    'room2fan': {
        'pin': 13,
        'status': 0,
    },
    'room2aircon': {
        'pin': 22,
        'status': 0,
    },

    'room3light': {
        'pin': 5,
        'status': 0,
    },
    'room3fan': {
        'pin': 6,
        'status': 0,
    },
    'room3aircon': {
        'pin': 21,
        'status': 0,
    },
}

for v in roomPins.values():
    GPIO.setup(v['pin'], GPIO.OUT)
    GPIO.output(v['pin'], GPIO.LOW)

fans = []

for k, fan in roomPins.items():
    if 'fan' in k:
         fanX = GPIO.PWM(fan['pin'], 500)
         fanX.start(0)
         fans.append(fanX)

app = Flask(__name__, static_url_path='/static')

def makeTemplateData():
    templateData = {}
    for k, v in roomPins.items():
        templateData[k] = v['status']
    return templateData

@app.route("/")
def index():
    templateData = makeTemplateData()
    return render_template('main.html', **templateData)


@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    actuator = roomPins[deviceName]['pin']

    if action == "on":
        if 'light' in deviceName:
            GPIO.output(actuator, GPIO.HIGH)
        roomPins[deviceName]['status'] = 1
    elif action == "off":
        if 'light' in deviceName:
            GPIO.output(actuator, GPIO.LOW)
        roomPins[deviceName]['status'] = 0

    templateData = makeTemplateData()

    return render_template('main.html', **templateData)

@app.route("/testroom1", methods=["POST"])
def testroom1():
    templateData = makeTemplateData()
    # Get slider Values
    slider1 = request.form["Room_1_Fan_Slider"]
    # Change duty cycle
    fans[0].ChangeDutyCycle(float(slider1))
    # Give servo some time to move
    sleep(1)
    templateData = makeTemplateData()
    return render_template('main.html', **templateData)

@app.route("/testroom2", methods=["POST"])
def testroom2():
    templateData = makeTemplateData()

    # Get slider Values
    slider2 = request.form["Room_2_Fan_Slider"]
    # Change duty cycle
    fans[1].ChangeDutyCycle(float(slider2))
    # Give servo some time to move
    sleep(1)
    templateData = makeTemplateData()
    return render_template('main.html', **templateData)

@app.route("/testroom3", methods=["POST"])
def testroom3():

    # Get slider Values
    slider3 = request.form["Room_3_Fan_Slider"]
    # Change duty cycle
    fans[2].ChangeDutyCycle(float(slider3))
    # Give servo some time to move
    sleep(1)
    templateData = makeTemplateData()

    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

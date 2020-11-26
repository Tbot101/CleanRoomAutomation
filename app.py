import RPi.GPIO as GPIO
from flask import Flask, render_template, request
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

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
        'pwm': 0,
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
        'pwm': 0,
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
        'pwm': 0,
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
        if 'fan' in deviceName:
            a = int(deviceName[4])-1
            fanvalue = roomPins[deviceName]['pwm']
            fans[a].ChangeDutyCycle(float(fanvalue))
    elif action == "off":
        if 'light' in deviceName:
            GPIO.output(actuator, GPIO.LOW)
        if 'fan' in deviceName:
            numberstr = deviceName[4]
            i = int(numberstr) - 1
            fans[i].ChangeDutyCycle(0)
        roomPins[deviceName]['status'] = 0
        
    templateData = makeTemplateData()

    return render_template('main.html', **templateData)

@app.route("/fanslider/<string:room>", methods=["POST"])
def fanslider(room):
    numberstr = room[-1]
    # Get slider Values
    slider = request.form["Room_"+numberstr+"_Fan_Slider"]
    deviceName = "room"+numberstr+"fan"
    roomPins[deviceName]['pwm'] = slider
    # Change duty cycle
    numberint = int(numberstr)
    i = numberint - 1
    fans[i].ChangeDutyCycle(float(slider))
    # Give servo some time to move
    sleep(1)
    templateData = makeTemplateData()
    return render_template('main.html', **templateData)

@app.route("/aircon/<string:room>/<string:forName>", methods=["GET"])
def aircon(room, forName):
    print(room)
    os.system("irsend SEND_ONCE MITSUBISHI "+forName)
    templateData = makeTemplateData()
    return render_template('main.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

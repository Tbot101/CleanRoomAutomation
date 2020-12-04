# CleanRoomAutomation
This project uses a flask backend and is connected to a electron front-end in order to create a 'desktop' app. Note: for the python file to run it must be done on a Raspberry Pi as the RPi.GPIO is only available on the Raspberry Pi. 

## Goal
Use a raspberry pi in order to automate certain processes in a clean room
1. Switching a light on and off
2. Switching a fan on and off and controlling its power
3. Controlling an air conditioner by using the raspberry pi to emit the infrared codes
    
Using an Electron JS frontend which has a link to the local host website hosted by the Raspberry Pi. Flask is used to communicate logic and instructions to the Raspberry Pi from the frontend. The dashboard is made dynamic and responsive to user interactions through the use of vanilla javascript.

## Electron
Run the Electron JS file which opens a desktop application. The app has one button on its homepage. This button has a link to the local host address of the Raspberry Pi. Therefore, when it is clicked it will open up the main dashboard for the Clean Rooms. However, for this to work the python file app.py has to be running as that opens up the flask website on the local host.

![Command Prompt](https://github.com/Tbot101/CleanRoomAutomation/blob/main/pictures/CommandPrompt.JPG?raw=true)

Enter the Electron directory and run `electron .` to start the Electron JS app.

![Electron JS](https://github.com/Tbot101/CleanRoomAutomation/blob/main/pictures/ElectronJS.JPG?raw=true)

This is what opens up after the above command is executed. 

![Dashboard Example](https://github.com/Tbot101/CleanRoomAutomation/blob/main/pictures/Dashboard.JPG?raw=true)

After clicking on the "Enter Control Room" button the dashboard is displayed with access to all the Clean Rooms.


## How to change the logo
HTML file main.html is stored under the templates folder. The images used in the dashboard such as the logo icon are saved under the `/static/images` folder. Change the icon image or change the image source under the main.html file. 

## How to add more rooms?

### Python:
![Python App.py](https://github.com/Tbot101/CleanRoomAutomation/blob/main/pictures/AppPY.JPG?raw=true)

1. Need to add the additional roomPins
2. Give each a standardized name such as ‘roomXlight’
3. Requires the relevant GPIO pin which it is connected to and status as 0
4. For fans will also require PWM values
    
### HTML:
![CreateHTML.py 1](https://github.com/Tbot101/CleanRoomAutomation/blob/main/pictures/CreateHTML1.JPG?raw=true)

![CreateHTML.py 2](https://github.com/Tbot101/CleanRoomAutomation/blob/main/pictures/CreateHTML2.JPG?raw=true)

1. Use the ‘createhtml.py’ file which automatically creates the main.html file
2. Here the range of rooms needs to be specified in two places

### Javascript:
![Control JS](https://github.com/Tbot101/CleanRoomAutomation/blob/main/pictures/ControlJS.JPG?raw=true)

Change the number `numRoom = 3` at the top of the file based on the number of rooms used.

### CSS:
![Styles.css](https://github.com/Tbot101/CleanRoomAutomation/blob/main/pictures/Styles.JPG?raw=true)

Need to add `.roomX{display:none;}` when each new room is added.

## Python app.py

Different app routes that correspond to url endpoints through which flask can extract data from the frontend. It uses this data to send instructions to the Raspberry Pi.

These app routes are dynamic through the use of <> and as a result it can easily scale up when there is more information or if different but similar routes added such as additional rooms. An example being `/<deviceName>/<action>`
    
`templateData = makeTemplateData()` is required to send information about the status of each pin to the frontend 

![Fan Form](https://github.com/Tbot101/CleanRoomAutomation/blob/main/pictures/AppPY_AirconSignal.JPG?raw=true)

os.system is used to send the IR signals to the air conditioner. This is done by using XMLHttpRequests and concatenating all the settings of the air conditioner such as temperature, mode and fan speed. The Flask backend reads this using URL endpoints and sends a command to the Raspberry Pi. The IR emitter then emits the relevant signal.

![Fan Form](https://github.com/Tbot101/CleanRoomAutomation/blob/main/pictures/AppPY_FanForm.JPG?raw=true)

The fanslider PWM is received from the form submission on the frontend. The pwm for the relevant fanslider is also updated which acts as a storage of latest pwm values. As a result, when the pin is switched off and then switched back on it can fetch the latest pwm value automatically from the backend making the interface dynamic.


## Python createhtml.py

This file automatically generates the HTML when more rooms are added. It is dynamic and changes the input to each function accordingly by using regex in python to change the keyword `CHANGENUMBER` to the corresponding room number. 

For example:
`Onclick=“airconoff(CHANGENUMBER)”`
Becomes `airconoff(1)`, `airconoff(2)` and so on for each room

After the python file is run there will be an HTML file as output called `newmain.html`. The contents of this file should be copied over to ‘main.html’ inside the templates folder. This will replace and update the GUI and display the desired number of rooms. Remember to similarly change the rest of the files.

## styles.css
Houses all the styling rules of the dashboard/GUI. There is one variable called `—main-box-shadow` which can be used to change all box shadows at once. There is a mixture of grid displays and flex displays as well as subgrids to make the design of the dashboard intuitive and appealing to the user. The custom slider CSS was also introduced as it is more user friendly. `overflow-x: hidden` to prevent side scroll while using interface.

## Javascript control.js
Has dynamic functions that take in input usually as ‘number’ or ‘room’ in order to manipulate DOM elements. Uses local storage extensively in order to save the latest user inputs in terms of fan pwm, aircon settings so that when the page is refreshed or if the app goes to another url endpoint the same information is still displayed. Uses cookies to swap out which room is being displayed. Furthermore, the information state for each aircon setting is saved in `condVal`. `condVal` is used to send information to the python front end in order to send IR signals.

## Potential Future Problems
1) Multiple instances of the same window being opened. This may confuse the Raspberry Pi as there is no centralized backend (controls to the Raspberry Pi are done from the frontend). Implement the changes on Python `app.py` using the `GET` method to make it more robust.
2) This may also require the program to regularly autoupdate and change the frontend to reflect values from the backend

## Miscellaneous
`mode2 -m -d /dev/lirc1` is the command to check if IR is being received on Raspberry Pi
`irsend SEND_ONCE MITSUBISHI OFF` is the format to send IR signals on the Raspberry Pi
To send multiple aircon signals the `sudo nano /boot/config.txt` file may need to be adapted (and other such files) in order to specialise where the IR signal for each room is being sent and which pin it is directed to.

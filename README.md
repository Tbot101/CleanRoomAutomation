# CleanRoomAutomation
This project uses a flask backend and is connected to a electron front-end in order to create a 'desktop' app.

Goal

Use a raspberry pi in order to automate certain processes in a clean room

    Switching a light on and off
    Switching a fan on and off and controlling its power
    Controlling an air conditioner by using the raspberry pi to emit the infrared codes
    
Using an electron js frontend which has a link to the local host website

The logic used to communicate to the raspberry pi from the frontend is done through flask in python

The dashboard is made dynamic through the use of javascript


How to add more rooms?

Python:

    Need to add the additional roomPins
    Give each a standardized name such as ‘roomXlight’
    Requires the relevant GPIO pin which it is connected to and status as 0
HTML:

    Can use the ‘createhtml.py’ file which automatically creates the main.html file
    Here the range of rooms needs to be specified in two places
Javascript:

    Define number of rooms at the top of the file
CSS:

    Need to add .roomX{display:none;} when each new room is added


Python app.py

Different app routes that correspond to url endpoints through which flask can extract data from the frontend 

It uses this data to send instructions to the raspberry pi

These app routes are dynamic through the use of <> and as a result it can easily scale up when there is more information or if different but similar routes added such as additional rooms
    An example being “/<deviceName>/<action>”
    
templateData = makeTemplateData() is required to send information about the status of each pin to the frontend 

os.system is used to send the IR signals to the air conditioner. This is done by using XMLHttpRequests and concatenating all the settings of the air conditioner such as temperature, mode and fan speed.

The fanslider PWM is received from the form submission. The pwm for the relevant fanslider is also updated which acts as a storage of latest pwm values. As a result, when the pin is switched off and then switched back on it can fetch the latest pwm value automatically


Python createhtml.py

This file automatically generates the HTML when more rooms are added

It is dynamic and changes the input to each function accordingly

It uses regex in python to change the keyword ‘CHANGENUMBER’ to the corresponding room number. 

For example:
Onclick=“airconoff(CHANGENUMBER)”
Becomes airconoff(1), airconoff(2) and so on for each room
After the python file is run there is an HTML file outputted also called newmain.html. The contents of this file should be copied over to ‘main.html’ inside the templates folder

styles.css
Houses all the styling rules of the dashboard/GUI
One variable called “—main-box-shadow” which can be used to change all box shadows at once
More variables can be implemented to make the code clean and easy to read
Overflow x is hidden to prevent having to scroll sideways
A mixture of grid and flex displays as well as subgrids.
Custom slider design as it is visually appealing 



